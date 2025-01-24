# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default, get

from .utils import UtilsMixin


class MgmtMixin(UtilsMixin):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mgmt_interface(self) -> str:
        """
        mgmt_interface.

        mgmt_interface is inherited from
        Global var mgmt_interface ->
          Platform Settings management_interface ->
            Fabric Topology data model mgmt_interface.
        """
        return default(
            self.shared_utils.node_config.mgmt_interface,
            # Notice that we actually have a default value for the next two, but the precedence order would break if we use it.
            # TODO: Evaluate if we should remove the default values from either or both.
            self.shared_utils.platform_settings._get("management_interface", None),
            self.inputs._get("mgmt_interface", None),
            get(self.shared_utils.cv_topology_config, "mgmt_interface"),
            "Management1",
        )

    @cached_property
    def mgmt_gateway(self) -> str | None:
        return default(self.shared_utils.node_config.mgmt_gateway, self.inputs.mgmt_gateway)

    @cached_property
    def ipv6_mgmt_gateway(self) -> str | None:
        return default(self.shared_utils.node_config.ipv6_mgmt_gateway, self.inputs.ipv6_mgmt_gateway)

    @cached_property
    def default_mgmt_method(self) -> str | None:
        """
        This is only executed if some protocol looks for the default value, so we can raise here to ensure a working config.

        The check for 'inband_mgmt_interface' relies on other indirect checks done in that code.
        """
        default_mgmt_method = self.inputs.default_mgmt_method
        if default_mgmt_method == "oob":
            if self.shared_utils.node_config.mgmt_ip is None and self.shared_utils.node_config.ipv6_mgmt_ip is None:
                msg = "'default_mgmt_method: oob' requires either 'mgmt_ip' or 'ipv6_mgmt_ip' to be set."
                raise AristaAvdInvalidInputsError(msg)

            return default_mgmt_method

        if default_mgmt_method == "inband":
            # Check for missing interface
            if self.shared_utils.inband_mgmt_interface is None:
                msg = "'default_mgmt_method: inband' requires 'inband_mgmt_interface' to be set."
                raise AristaAvdInvalidInputsError(msg)

            return default_mgmt_method

        return None

    @cached_property
    def default_mgmt_protocol_vrf(self) -> str | None:
        if self.default_mgmt_method == "oob":
            return self.inputs.mgmt_interface_vrf
        if self.default_mgmt_method == "inband":
            # inband_mgmt_vrf returns None for vrf default.
            return self.shared_utils.inband_mgmt_vrf or "default"

        return None

    @cached_property
    def default_mgmt_protocol_interface(self) -> str | None:
        if self.default_mgmt_method == "oob":
            return self.mgmt_interface
        if self.default_mgmt_method == "inband":
            return self.shared_utils.inband_mgmt_interface

        return None
