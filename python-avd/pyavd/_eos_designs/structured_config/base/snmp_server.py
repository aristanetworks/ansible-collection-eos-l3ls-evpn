# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from hashlib import sha1
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd.j2filters import natural_sort, snmp_hash

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigBaseProtocol


class SnmpServerMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def snmp_server(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        snmp_server set based on snmp_settings data-model, using various snmp_settings information.

        if snmp_settings.compute_local_engineid is True we will use sha1 to create a
        unique local_engine_id value based on hostname and mgmt_ip facts.

        If user.version is set to 'v3', compute_local_engineid and compute_v3_user_localized_key are set to 'True'
        we will use snmp_hash filter to create an instance of hashlib HASH corresponding to the auth_type
        value based on various snmp_settings.users information.
        """
        source_interfaces_inputs = self.inputs.source_interfaces.snmp
        snmp_settings = self.inputs.snmp_settings

        if not any([source_interfaces_inputs, snmp_settings]):
            return

        self._snmp_engine_ids(snmp_settings)
        self._snmp_location(snmp_settings)
        self._snmp_users(snmp_settings)
        self._snmp_hosts(snmp_settings)
        self._snmp_vrfs(snmp_settings)
        self._snmp_local_interfaces(source_interfaces_inputs)

        self.structured_config.snmp_server._update(
            contact=snmp_settings.contact,
            communities=snmp_settings.communities,
            ipv4_acls=snmp_settings.ipv4_acls._cast_as(EosCliConfigGen.SnmpServer.Ipv4Acls),
            ipv6_acls=snmp_settings.ipv6_acls._cast_as(EosCliConfigGen.SnmpServer.Ipv6Acls),
            views=snmp_settings.views._cast_as(EosCliConfigGen.SnmpServer.Views),
            groups=snmp_settings.groups._cast_as(EosCliConfigGen.SnmpServer.Groups),
        )
        if snmp_settings.traps.enable:
            self.structured_config.snmp_server._update(traps=snmp_settings.traps)

    def _snmp_engine_ids(self: AvdStructuredConfigBaseProtocol, snmp_settings: EosDesigns.SnmpSettings) -> None:
        """Set dict of engine ids if "snmp_settings.compute_local_engineid" is True."""
        if not snmp_settings.compute_local_engineid:
            return

        compute_source = snmp_settings.compute_local_engineid_source
        if compute_source == "hostname_and_ip":
            # Accepting SonarLint issue: The weak sha1 is not used for encryption. Just to create a unique engine id.
            local_engine_id = sha1(f"{self.shared_utils.hostname}{self.shared_utils.node_config.mgmt_ip}".encode()).hexdigest()  # NOSONAR # noqa: S324

        elif compute_source == "system_mac":
            if self.shared_utils.system_mac_address is None:
                msg = "default_engine_id_from_system_mac: true requires system_mac_address to be set."
                raise AristaAvdInvalidInputsError(msg)
            # the default engine id on switches is derived as per the following formula
            local_engine_id = f"f5717f{str(self.shared_utils.system_mac_address).replace(':', '').lower()}00"
        else:
            # Unknown mode
            msg = f"'{compute_source}' is not a valid value to compute the engine ID, accepted values are 'hostname_and_ip' and 'system_mac'"
            raise AristaAvdError(msg)

        self.structured_config.snmp_server.engine_ids.local = local_engine_id

    def _snmp_location(self: AvdStructuredConfigBaseProtocol, snmp_settings: EosDesigns.SnmpSettings) -> None:
        """Set location if "snmp_settings.location" is True."""
        if not snmp_settings.location:
            return

        location_elements = [
            self.shared_utils.fabric_name,
            self.inputs.dc_name,
            self.inputs.pod_name,
            self.shared_utils.node_config.rack,
            self.shared_utils.hostname,
        ]
        location_elements = [location for location in location_elements if location not in [None, ""]]
        self.structured_config.snmp_server.location = " ".join(location_elements)

    def _snmp_users(self: AvdStructuredConfigBaseProtocol, snmp_settings: EosDesigns.SnmpSettings) -> None:
        """
        Set users if "snmp_settings.users" is set.

        Users will have computed localized keys if configured.
        """
        if not (users := snmp_settings.users):
            # Empty list or None
            return

        engine_ids = self.structured_config.snmp_server.engine_ids
        compute_v3_user_localized_key = engine_ids and engine_ids.local and snmp_settings.compute_v3_user_localized_key
        for user in users:
            version = user.version
            user_dict = EosCliConfigGen.SnmpServer.UsersItem(
                name=user.name,
                group=user.group,
                version=version,
            )
            if version == "v3":
                if compute_v3_user_localized_key:
                    user_dict.localized = engine_ids.local

                if user.auth is not None and user.auth_passphrase is not None:
                    user_dict.auth = user.auth
                    if compute_v3_user_localized_key:
                        hash_filter = {"passphrase": user.auth_passphrase, "auth": user.auth, "engine_id": engine_ids.local}
                        user_dict.auth_passphrase = snmp_hash(hash_filter)
                    else:
                        user_dict.auth_passphrase = user.auth_passphrase

                    if user.priv is not None and user.priv_passphrase is not None:
                        user_dict.priv = user.priv
                        if compute_v3_user_localized_key:
                            hash_filter.update({"passphrase": user.priv_passphrase, "priv": user.priv})
                            user_dict.priv_passphrase = snmp_hash(hash_filter)
                        else:
                            user_dict.priv_passphrase = user.priv_passphrase

            self.structured_config.snmp_server.users.append(user_dict)

    def _snmp_hosts(self: AvdStructuredConfigBaseProtocol, snmp_settings: EosDesigns.SnmpSettings) -> None:
        """
        Set hosts if "snmp_settings.hosts" is set.

        Hosts may have management VRFs dynamically set.
        """
        snmp_hosts = EosCliConfigGen.SnmpServer.Hosts()
        if not (hosts := snmp_settings.hosts):
            return

        has_mgmt_ip = (self.shared_utils.node_config.mgmt_ip is not None) or (self.shared_utils.node_config.ipv6_mgmt_ip is not None)

        for host in natural_sort(hosts, "host"):
            host: EosDesigns.SnmpSettings.HostsItem
            vrfs = set()
            if vrf := host.vrf:
                vrfs.add(vrf)

            if (use_mgmt_interface_vrf := host.use_mgmt_interface_vrf) and has_mgmt_ip:
                vrfs.add(self.inputs.mgmt_interface_vrf)

            if (use_inband_mgmt_vrf := host.use_inband_mgmt_vrf) and self.shared_utils.inband_mgmt_interface is not None:
                # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
                vrfs.add(self.shared_utils.inband_mgmt_vrf or "default")

            if not any([vrfs, use_mgmt_interface_vrf, use_inband_mgmt_vrf]):
                # If no VRFs are defined (and we are not just ignoring missing mgmt config)
                vrfs.add("default")

            output_host = host._cast_as(EosCliConfigGen.SnmpServer.HostsItem, ignore_extra_keys=True)

            # Ensure default VRF is added first
            if "default" in vrfs:
                vrfs.remove("default")
                # Add host without VRF field
                add_host = output_host._deepcopy()
                delattr(add_host, "vrf")
                snmp_hosts.append(add_host)

            # Add host with VRF field.
            for vrf in natural_sort(vrfs):
                add_host = output_host._deepcopy()
                add_host.vrf = vrf
                snmp_hosts.append(add_host)

        self.structured_config.snmp_server.hosts = snmp_hosts

    def _snmp_local_interfaces(self: AvdStructuredConfigBaseProtocol, source_interfaces_inputs: EosDesigns.SourceInterfaces.Snmp) -> None:
        """Set local_interfaces if "source_interfaces.snmp" is set."""
        if not source_interfaces_inputs:
            # Empty dict or None
            return
        local_interfaces = self._build_source_interfaces(source_interfaces_inputs.mgmt_interface, source_interfaces_inputs.inband_mgmt_interface, "SNMP")
        for local_interface in local_interfaces:
            self.structured_config.snmp_server.local_interfaces.append(EosCliConfigGen.SnmpServer.LocalInterfacesItem(**local_interface))

    def _snmp_vrfs(self: AvdStructuredConfigBaseProtocol, snmp_settings: EosDesigns.SnmpSettings) -> None:
        """
        Set list of dicts for enabling/disabling SNMP for VRFs.

        Requires one of the following options to be set under snmp_settings:
        - vrfs
        - enable_mgmt_interface_vrf
        - enable_inband_mgmt_vrf
        """
        has_mgmt_ip = (self.shared_utils.node_config.mgmt_ip is not None) or (self.shared_utils.node_config.ipv6_mgmt_ip is not None)

        vrfs = snmp_settings.vrfs._deepcopy()
        if has_mgmt_ip and (enable_mgmt_interface_vrf := snmp_settings.enable_mgmt_interface_vrf) is not None:
            vrfs.append(EosCliConfigGen.SnmpServer.VrfsItem(name=self.inputs.mgmt_interface_vrf, enable=enable_mgmt_interface_vrf))

        if (enable_inband_mgmt_vrf := snmp_settings.enable_inband_mgmt_vrf) is not None and self.shared_utils.inband_mgmt_interface is not None:
            # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
            vrfs.append(EosCliConfigGen.SnmpServer.VrfsItem(name=self.shared_utils.inband_mgmt_vrf or "default", enable=enable_inband_mgmt_vrf))

        self.structured_config.snmp_server.vrfs = vrfs._natural_sorted()
