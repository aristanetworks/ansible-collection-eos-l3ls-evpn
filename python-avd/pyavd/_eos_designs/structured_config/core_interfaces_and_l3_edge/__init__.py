# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, StructuredConfigGeneratorProtocol

from .ethernet_interfaces import EthernetInterfacesMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .router_bgp import RouterBgpMixin
from .router_ospf import RouterOspfMixin
from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

DATA_MODELS: list[Literal["core_interfaces", "l3_edge"]] = ["core_interfaces", "l3_edge"]


class AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol(
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    RouterBgpMixin,
    RouterOspfMixin,
    UtilsMixin,
    StructuredConfigGeneratorProtocol,
    Protocol,
):
    """
    Protocol for the AvdStructuredConfig Class which is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to inherit the _hostvars, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    data_model: Literal["core_interfaces", "l3_edge"]
    inputs_data: EosDesigns.CoreInterfaces | EosDesigns.L3Edge

    def render(self) -> list:
        """Render structured configs for core_interfaces and l3_Edge."""
        result_list = []

        for data_model in DATA_MODELS:
            self.data_model = data_model
            self.inputs_data = self.inputs.core_interfaces if data_model == "core_interfaces" else self.inputs.l3_edge
            result_list.append(super().render())
            self.clear_cache()

        return result_list


class AvdStructuredConfigCoreInterfacesAndL3Edge(StructuredConfigGenerator, AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to inherit the _hostvars, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """
