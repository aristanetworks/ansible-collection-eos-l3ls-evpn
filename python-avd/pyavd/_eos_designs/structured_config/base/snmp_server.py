# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from hashlib import sha1
from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import strip_null_from_data
from pyavd.j2filters import natural_sort, snmp_hash

from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigBase


class SnmpServerMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def snmp_server(self: AvdStructuredConfigBase) -> dict | None:
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
            return None

        # Set here so we can reuse it.
        engine_ids = self._snmp_engine_ids(snmp_settings)

        # Pass through most settings with no abstraction.
        # Use other functions for abstraction.
        # return strip_null_from_data(
        return strip_null_from_data(
            {
                "engine_ids": engine_ids,
                "contact": snmp_settings.contact,
                "location": self._snmp_location(snmp_settings),
                "users": self._snmp_users(snmp_settings, engine_ids),
                "hosts": self._snmp_hosts(snmp_settings)._as_list() or None,
                "vrfs": self._snmp_vrfs(snmp_settings)._as_list() or None,
                "local_interfaces": self._snmp_local_interfaces(source_interfaces_inputs),
                "communities": snmp_settings.communities._as_list() or None,
                "ipv4_acls": snmp_settings.ipv4_acls._as_list() or None,
                "ipv6_acls": snmp_settings.ipv6_acls._as_list() or None,
                "views": snmp_settings.views._as_list() or None,
                "groups": snmp_settings.groups._as_list() or None,
                "traps": snmp_settings.traps._as_dict() if snmp_settings.traps.enable else None,
            },
        )

    def _snmp_engine_ids(self: AvdStructuredConfigBase, snmp_settings: EosDesigns.SnmpSettings) -> dict | None:
        """
        Return dict of engine ids if "snmp_settings.compute_local_engineid" is True.

        Otherwise return None.
        """
        if not snmp_settings.compute_local_engineid:
            return None

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

        return {"local": local_engine_id}

    def _snmp_location(self: AvdStructuredConfigBase, snmp_settings: EosDesigns.SnmpSettings) -> str | None:
        """
        Return location if "snmp_settings.location" is True.

        Otherwise return None.
        """
        if not snmp_settings.location:
            return None

        location_elements = [
            self.shared_utils.fabric_name,
            self.inputs.dc_name,
            self.inputs.pod_name,
            self.shared_utils.node_config.rack,
            self.shared_utils.hostname,
        ]
        location_elements = [location for location in location_elements if location not in [None, ""]]
        return " ".join(location_elements)

    def _snmp_users(self: AvdStructuredConfigBase, snmp_settings: EosDesigns.SnmpSettings, engine_ids: dict | None) -> list | None:
        """
        Return users if "snmp_settings.users" is set.

        Otherwise return None.

        Users will have computed localized keys if configured.
        """
        if not (users := snmp_settings.users):
            # Empty list or None
            return None

        snmp_users = []
        compute_v3_user_localized_key = (engine_ids is not None) and (engine_ids.get("local") is not None) and snmp_settings.compute_v3_user_localized_key
        for user in users:
            version = user.version
            user_dict = {
                "name": user.name,
                "group": user.group,
                "version": version,
            }
            if version == "v3":
                if compute_v3_user_localized_key:
                    user_dict["localized"] = engine_ids["local"]

                if user.auth is not None and user.auth_passphrase is not None:
                    user_dict["auth"] = user.auth
                    if compute_v3_user_localized_key:
                        hash_filter = {"passphrase": user.auth_passphrase, "auth": user.auth, "engine_id": engine_ids["local"]}
                        user_dict["auth_passphrase"] = snmp_hash(hash_filter)
                    else:
                        user_dict["auth_passphrase"] = user.auth_passphrase

                    if user.priv is not None and user.priv_passphrase is not None:
                        user_dict["priv"] = user.priv
                        if compute_v3_user_localized_key:
                            hash_filter.update({"passphrase": user.priv_passphrase, "priv": user.priv})
                            user_dict["priv_passphrase"] = snmp_hash(hash_filter)
                        else:
                            user_dict["priv_passphrase"] = user.priv_passphrase

            snmp_users.append(user_dict)

        return snmp_users or None

    def _snmp_hosts(self: AvdStructuredConfigBase, snmp_settings: EosDesigns.SnmpSettings) -> EosCliConfigGen.SnmpServer.Hosts:
        """
        Return hosts if "snmp_settings.hosts" is set.

        Hosts may have management VRFs dynamically set.
        """
        snmp_hosts = EosCliConfigGen.SnmpServer.Hosts()
        if not (hosts := snmp_settings.hosts):
            return snmp_hosts

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

        return snmp_hosts

    def _snmp_local_interfaces(self: AvdStructuredConfigBase, source_interfaces_inputs: EosDesigns.SourceInterfaces.Snmp) -> list | None:
        """
        Return local_interfaces if "source_interfaces.snmp" is set.

        Otherwise return None.
        """
        if not source_interfaces_inputs:
            # Empty dict or None
            return None

        local_interfaces = self._build_source_interfaces(source_interfaces_inputs.mgmt_interface, source_interfaces_inputs.inband_mgmt_interface, "SNMP")
        return local_interfaces or None

    def _snmp_vrfs(self: AvdStructuredConfigBase, snmp_settings: EosDesigns.SnmpSettings) -> EosDesigns.SnmpSettings.Vrfs:
        """
        Return list of dicts for enabling/disabling SNMP for VRFs.

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

        return vrfs._natural_sorted()
