# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class NtpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ntp(self: AvdStructuredConfigBaseProtocol) -> None:
        """Ntp set based on "ntp_settings" data-model."""
        if not (ntp_settings := self.inputs.ntp_settings):
            return

        # Since the eos_cli_config_gen data model almost matches, we can copy most data directly.
        self.structured_config.ntp._update(
            authenticate=ntp_settings.authenticate,
            authenticate_servers_only=ntp_settings.authenticate_servers_only,
            trusted_keys=ntp_settings.trusted_keys,
        )
        self.structured_config.ntp.authentication_keys = ntp_settings.authentication_keys._cast_as(EosCliConfigGen.Ntp.AuthenticationKeys)

        if not ntp_settings.servers:
            # Quick return if we have no servers.
            return

        # Get server_vrf from ntp_settings and configure with the relevant VRF.
        # Also set relevant local interface.
        server_vrf = ntp_settings.server_vrf
        if server_vrf is None:
            server_vrf = self.shared_utils.default_mgmt_protocol_vrf
            self.structured_config.ntp.local_interface.name = self.shared_utils.default_mgmt_protocol_interface
            self.structured_config.ntp.local_interface.vrf = server_vrf

        if server_vrf == "use_mgmt_interface_vrf":
            has_mgmt_ip = (self.shared_utils.node_config.mgmt_ip is not None) or (self.shared_utils.node_config.ipv6_mgmt_ip is not None)
            if not has_mgmt_ip:
                msg = "'ntp_settings.server_vrf' is set to 'use_mgmt_interface_vrf' but this node is missing an 'mgmt_ip'"
                raise AristaAvdError(msg)
            # Replacing server_vrf with mgmt_interface_vrf
            server_vrf = self.inputs.mgmt_interface_vrf
            self.structured_config.ntp.local_interface.name = self.shared_utils.mgmt_interface
            self.structured_config.ntp.local_interface.vrf = server_vrf

        elif server_vrf == "use_inband_mgmt_vrf":
            if self.shared_utils.inband_mgmt_interface is None:
                msg = "'ntp_settings.server_vrf' is set to 'use_inband_mgmt_vrf' but this node is missing configuration for inband management"
                raise AristaAvdError(msg)
            # self.shared_utils.inband_mgmt_vrf returns None for the default VRF.
            # Replacing server_vrf with inband_mgmt_vrf or "default"
            server_vrf = self.shared_utils.inband_mgmt_vrf or "default"
            self.structured_config.ntp.local_interface.name = self.shared_utils.inband_mgmt_interface
            self.structured_config.ntp.local_interface.vrf = server_vrf

        # First server is set with preferred
        first = True
        for server in ntp_settings.servers:
            ntp_server = server._cast_as(EosCliConfigGen.Ntp.ServersItem)
            ntp_server.vrf = server_vrf
            if first:
                ntp_server.preferred = True
                first = False
            self.structured_config.ntp.servers.append(ntp_server)
