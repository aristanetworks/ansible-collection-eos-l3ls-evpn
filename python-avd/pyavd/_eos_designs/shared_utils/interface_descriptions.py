# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._utils import load_python_class
from pyavd.api.interface_descriptions import AvdInterfaceDescriptions

from .utils import UtilsMixin


class InterfaceDescriptionsMixin(UtilsMixin):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def interface_descriptions(self) -> AvdInterfaceDescriptions:
        """
        Load the python_module defined in `templates.interface_descriptions.python_module`.

        Return an instance of the class defined by `templates.interface_descriptions.python_class_name` as cached_property.
        """
        module_path = self.shared_utils.node_type_key_data.interface_descriptions.python_module
        if module_path is None:
            return AvdInterfaceDescriptions(hostvars=self.shared_utils._hostvars, inputs=self.inputs, shared_utils=self.shared_utils)

        cls: type[AvdInterfaceDescriptions] = load_python_class(
            module_path,
            self.shared_utils.node_type_key_data.interface_descriptions.python_class_name,
            AvdInterfaceDescriptions,
        )

        return cls(hostvars=self.shared_utils._hostvars, inputs=self.inputs, shared_utils=self)
