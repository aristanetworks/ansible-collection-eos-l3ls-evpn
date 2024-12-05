# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections import ChainMap, defaultdict
from collections.abc import Callable
from logging import getLogger
from typing import Literal, TypeVar

from typing_extensions import Self

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils

from .structured_config_generator import StructuredConfigGenerator

Tenant = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem
Vrf = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem
L2Vlan = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem
Svi = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
Execution = Literal["pre", "per_tenant", "per_vrf", "per_svi", "per_l2vlan", "per_vlan", "post"]

T_StructuredConfigGenerator = TypeVar("T_StructuredConfigGenerator", bound=StructuredConfigGenerator)

LOGGER = getLogger(__name__)


class RegisterForExecution:
    """Decorator of class method."""

    execution: Execution
    func: Callable

    def __init__(self, execution: Execution) -> None:
        """
        Register a class method for execution.

        Args:
            execution: Instruction on when the call this method.
                - 'pre' will be called before network services are parsed.
                - 'per_tenant' will be called once per Tenant with the Tenant as argument.
                  The call is _after_ all per-VRF and per-L2VLAN executions
                - 'per_vrf' will be called once per Tenant per VRF with the VRF and Tenant as arguments.
                  If the same VRF is defined across multiple Tenants the method will be called multiple times.
                  The call is _after_ all per-SVI executions.
                - 'per_svi' will be called once per SVI with the SVI, VRF and Tenant as arguments.
                - 'per_l2vlan' will be called once per L2VLAN with the L2VLAN and Tenant as arguments.
                - 'post' will be called after network services have been parsed.
        """
        self.execution = execution

    def __call__(self, func: Callable) -> Self:
        """This is called as the method is being decorated on the class."""
        self.func = func
        return self

    def __set_name__(self, owner: type[T_StructuredConfigGenerator], name: str) -> None:
        """This is called when the decorated method is applied to the class (not the instance)."""
        LOGGER.debug("Registering '%s' execution of method '%s' on structured config generator '%s'", self.execution, name, owner.__name__)
        # Set the original function back as the method of the class - removing this decorator.
        setattr(owner, name, self.func)
        # Register the method in the class registry. This will be picked up by __init__ of StructuredConfigGenerator base class.
        if not hasattr(owner, "_cls_method_execution_registry"):
            owner._cls_method_execution_registry = defaultdict(list)
        owner._cls_method_execution_registry[self.execution].append(name)


class StructuredConfigExecutor:
    _shared_utils: SharedUtils
    _method_execution_registry: defaultdict[str, list[tuple[StructuredConfigGenerator, str]]]

    def __init__(
        self,
        hostvars: dict | ChainMap,
        inputs: EosDesigns,
        structured_config: EosCliConfigGen,  # TODO: Remove and sort out inside once all code use this.
        custom_structured_configurations: list[EosCliConfigGen],  # TODO: Remove and sort out inside once all code use this.
        shared_utils: SharedUtils,  # TODO: Remove and sort out inside once all code use this.
        classes: tuple[type[T_StructuredConfigGenerator], ...],
    ) -> None:
        """
        Build structured configuration using subclasses of StructuredConfigGenerator.

        Args:
            hostvars: Raw input variables - still used to get facts and exposed in some custom templating.
            inputs: EosDesigns instance containing all the inputs.
            structured_config: EosCliConfigGen instance to be updated.
                Can also be inspected to get output of previous generators.
            custom_structured_configurations: List of custom structured configurations.
                The class can either append extra structured configurations or apply them to the given structured_configuration instance.
            shared_utils: SharedUtils instance containing data to be reused between Structured Config generators.
            classes: Tuple of StructuredConfigGenerator subclasses to generate.
        """
        self._shared_utils = shared_utils
        self._method_execution_registry = defaultdict(list)
        for cls in classes:
            LOGGER.debug("Initializing structured config generator: %s", cls)
            # As we initialize each class they will register into _method_execution_registry of this Executor instance
            cls(
                hostvars=hostvars,
                inputs=inputs,
                structured_config=structured_config,
                custom_structured_configurations=custom_structured_configurations,
                shared_utils=shared_utils,
                executor=self,
            )

    def execute(self) -> None:
        """Execute the methods as registered."""
        LOGGER.debug("Starting execution of structured config generators.")
        self._execute_pre()
        for tenant in self._shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    self._execute_per_svi(svi, vrf, tenant)
                self._execute_per_vrf(vrf, tenant)
            for l2vlan in tenant.l2vlans:
                self._execute_per_l2vlan(l2vlan, tenant)
            self._execute_per_tenant(tenant)
        self._execute_post()

    def graph(self) -> str:
        """
        Generate a mermaid graph of the execution order.

        This requires python-mermaid to be installed. We only expect to call this during development workflows.
        """
        from python_mermaid.diagram import MermaidDiagram, Node, Link  # pylint: disable=import-outside-toplevel  # noqa: I001

        start_node = Node(id="start", content="Build Structured Config")
        nodes = [start_node]
        links: list[Link] = []

        for instance, method in self._method_execution_registry["pre"]:
            cls = type(instance)
            nodes.append(Node(id=f"{cls.__name__}.{method}", content=f"{cls.__name__}.{method}()"))
            links.append(Link(origin=start_node, end=nodes[-1]))

        per_tenant_node = Node("loop_tenants", content="Loop over filtered Tenants")
        nodes.append(per_tenant_node)
        links.append(Link(start_node, end=nodes[-1]))
        for instance, method in self._method_execution_registry["per_tenant"]:
            cls = type(instance)
            nodes.append(Node(id=f"{cls.__name__}.{method}", content=f"{cls.__name__}.{method}(tenant)"))
            links.append(Link(origin=per_tenant_node, end=nodes[-1], message="Call per Tenant"))

        per_vrf_node = Node("loop_vrfs", content="Loop over filtered VRFs")
        nodes.append(per_vrf_node)
        links.append(Link(origin=per_tenant_node, end=per_vrf_node, message="Call per Tenant"))
        for instance, method in self._method_execution_registry["per_vrf"]:
            cls = type(instance)
            nodes.append(Node(id=f"{cls.__name__}.{method}", content=f"{cls.__name__}.{method}(vrf, tenant)"))
            links.append(Link(origin=per_vrf_node, end=nodes[-1], message="Call per VRF"))

        per_svi_node = Node("loop_svis", content="Loop over filtered SVIs")
        nodes.append(per_svi_node)
        links.append(Link(origin=per_vrf_node, end=per_svi_node, message="Call per VRF"))
        for instance, method in self._method_execution_registry["per_svi"]:
            cls = type(instance)
            nodes.append(Node(id=f"{cls.__name__}.{method}", content=f"{cls.__name__}.{method}(svi, vrf, tenant)"))
            links.append(Link(origin=per_svi_node, end=nodes[-1], message="Call per SVI"))

        per_l2vlan_node = Node("loop_l2vlan", content="Loop over filtered L2VLANs")
        nodes.append(per_l2vlan_node)
        links.append(Link(origin=per_tenant_node, end=per_l2vlan_node, message="Call per Tenant"))
        for instance, method in self._method_execution_registry["per_l2vlan"]:
            cls = type(instance)
            nodes.append(Node(id=f"{cls.__name__}.{method}", content=f"{cls.__name__}.{method}(l2vlan, tenant)"))
            links.append(Link(origin=per_l2vlan_node, end=nodes[-1], message="Call per L2VLAN"))

        for instance, method in self._method_execution_registry["post"]:
            cls = type(instance)
            nodes.append(Node(id=f"{cls.__name__}.{method}", content=f"{cls.__name__}.{method}()"))
            links.append(Link(origin=per_tenant_node, end=nodes[-1]))

        flowchart = MermaidDiagram("AVD eos_designs execution", nodes=nodes, links=links)
        return str(flowchart)

    def register_generator_methods(self, instance: StructuredConfigGenerator, cls_method_execution_registry: defaultdict[Execution, list[str]]) -> None:
        """
        Register methods of one StructuredConfigGenerator for execution.

        This is called during __init__ of each StructuredConfigGenerator.
        """
        for execution, methods in cls_method_execution_registry.items():
            LOGGER.debug("Registering '%s' methods for structured config generator '%s'", execution, type(instance).__name__)
            self._method_execution_registry[execution].extend((instance, method) for method in methods)

    def _execute_pre(self) -> None:
        for instance, method in self._method_execution_registry["pre"]:
            LOGGER.debug("Executing 'pre' method '%s' on structured config generator '%s'", method, type(instance))
            getattr(instance, method)()

    def _execute_per_tenant(self, tenant: Tenant) -> None:
        for instance, method in self._method_execution_registry["per_tenant"]:
            LOGGER.debug("Executing 'per_tenant' method '%s' on structured config generator '%s' for Tenant '%s'", method, type(instance), tenant.name)
            getattr(instance, method)(tenant)

    def _execute_per_vrf(self, vrf: Vrf, tenant: Tenant) -> None:
        LOGGER.debug("foo")
        for instance, method in self._method_execution_registry["per_vrf"]:
            LOGGER.debug(
                "Executing 'per_vrf' method '%s' on structured config generator '%s' for VRF '%s' in Tenant '%s'", method, type(instance), vrf.name, tenant.name
            )
            getattr(instance, method)(vrf, tenant)

    def _execute_per_svi(self, svi: Svi, vrf: Vrf, tenant: Tenant) -> None:
        for instance, method in self._method_execution_registry["per_svi"]:
            LOGGER.debug(
                "Executing 'per_svi' method '%s' on structured config generator '%s' for SVI '%s' in VRF '%s' in Tenant '%s'",
                method,
                type(instance),
                svi.id,
                vrf.name,
                tenant.name,
            )
            getattr(instance, method)(svi, vrf, tenant)

    def _execute_per_l2vlan(self, l2vlan: L2Vlan, tenant: Tenant) -> None:
        for instance, method in self._method_execution_registry["per_l2vlan"]:
            LOGGER.debug(
                "Executing 'per_svi' method '%s' on structured config generator '%s' for L2VLAN '%s' in Tenant '%s'",
                method,
                type(instance),
                l2vlan.id,
                tenant.name,
            )
            getattr(instance, method)(l2vlan, tenant)

    def _execute_post(self) -> None:
        for instance, method in self._method_execution_registry["post"]:
            LOGGER.debug("Executing 'post' method '%s' on structured config generator '%s'", method, type(instance))
            getattr(instance, method)()
