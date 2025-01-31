# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdMissingVariableError
from pyavd._utils import load_python_class
from pyavd.api.ip_addressing import AvdIpAddressing

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class IpAddressingMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def loopback_ipv6_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.loopback_ipv6_pool:
            msg = "loopback_ipv6_pool"
            raise AristaAvdMissingVariableError(msg)

        return self.node_config.loopback_ipv6_pool

    @cached_property
    def loopback_ipv4_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.loopback_ipv4_pool:
            msg = "loopback_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)

        return self.node_config.loopback_ipv4_pool

    @cached_property
    def vtep_loopback_ipv4_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.vtep_loopback_ipv4_pool:
            msg = "vtep_loopback_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)

        return self.node_config.vtep_loopback_ipv4_pool

    @cached_property
    def vtep_ip(self: SharedUtilsProtocol) -> str:
        """Render ipv4 address for vtep_ip using dynamically loaded python module."""
        if self.mlag is True:
            return self.ip_addressing.vtep_ip_mlag()

        return self.ip_addressing.vtep_ip()

    @cached_property
    def ip_addressing(self: SharedUtilsProtocol) -> AvdIpAddressing:
        """
        Load the python_module defined in `templates.ip_addressing.python_module`.

        Return an instance of the class defined by `templates.ip_addressing.python_class_name` as cached_property.
        """
        module_path = self.node_type_key_data.ip_addressing.python_module
        if module_path is None:
            return AvdIpAddressing(hostvars=self.hostvars, inputs=self.inputs, shared_utils=self)

        cls: type[AvdIpAddressing] = load_python_class(
            module_path,
            self.node_type_key_data.ip_addressing.python_class_name,
            AvdIpAddressing,
        )

        return cls(hostvars=self.hostvars, inputs=self.inputs, shared_utils=self)
