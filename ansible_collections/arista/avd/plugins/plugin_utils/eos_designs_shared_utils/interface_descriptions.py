from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, load_python_class
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions.avdinterfacedescriptions import AvdInterfaceDescriptions

if TYPE_CHECKING:
    from .shared_utils import SharedUtils

DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE = "ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions"
DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME = "AvdInterfaceDescriptions"


class InterfaceDescriptionsMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using quoted type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def interface_descriptions(self: "SharedUtils") -> AvdInterfaceDescriptions:
        """
        Load the python_module defined in `templates.interface_descriptions.python_module`
        Return an instance of the class defined by `templates.interface_descriptions.python_class_name` as cached_property
        """
        module_path = self.interface_descriptions_templates.get("python_module", DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE)
        class_name = self.interface_descriptions_templates.get("python_class_name", DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME)

        cls = load_python_class(
            module_path,
            class_name,
            AvdInterfaceDescriptions,
        )

        return cls(hostvars=self.hostvars, shared_utils=self)

    @cached_property
    def interface_descriptions_templates(self: "SharedUtils") -> dict:
        """
        Return dict with interface_descriptions templates set based on
        templates.interface_descriptions.* combined with (overridden by)
        node_type_keys.<node_type_key>.interface_descriptions.*
        """
        hostvar_templates = get(self.hostvars, "templates.interface_descriptions", default={})
        node_type_templates = get(self.node_type_key_data, "interface_descriptions", default={})
        if hostvar_templates or node_type_templates:
            return merge(hostvar_templates, node_type_templates, list_merge="replace", destructive_merge=False)
        else:
            return {}
