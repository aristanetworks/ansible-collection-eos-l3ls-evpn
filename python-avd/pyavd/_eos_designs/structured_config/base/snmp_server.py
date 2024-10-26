# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from hashlib import sha1
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import get, replace_or_append_item, strip_null_from_data
from pyavd.j2filters import natural_sort, snmp_hash

from .utils import UtilsMixin

if TYPE_CHECKING:
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
        source_interfaces_inputs = self._source_interfaces.get("snmp")
        snmp_settings = get(self._hostvars, "snmp_settings", {})

        if not any([source_interfaces_inputs, snmp_settings]):
            return None

        # Set here so we can reuse it.
        engine_ids = self._snmp_engine_ids(snmp_settings)

        # Pass through most settings with no abstraction.
        # Use other functions for abstraction.
        return strip_null_from_data(
            {
                "engine_ids": engine_ids,
                "contact": snmp_settings.get("contact"),
                "location": self._snmp_location(snmp_settings),
                "users": self._snmp_users(snmp_settings, engine_ids),
                "hosts": self._snmp_hosts(snmp_settings),
                "vrfs": self._snmp_vrfs(snmp_settings),
                "local_interfaces": self._snmp_local_interfaces(source_interfaces_inputs),
                "communities": snmp_settings.get("communities"),
                "ipv4_acls": snmp_settings.get("ipv4_acls"),
                "ipv6_acls": snmp_settings.get("ipv6_acls"),
                "views": snmp_settings.get("views"),
                "groups": snmp_settings.get("groups"),
                "traps": snmp_settings.get("traps"),
            },
        )

    def _snmp_engine_ids(self: AvdStructuredConfigBase, snmp_settings: dict) -> dict | None:
        """
        Return dict of engine ids if "snmp_settings.compute_local_engineid" is True.

        Otherwise return None.
        """
        if snmp_settings.get("compute_local_engineid") is not True:
            return None

        compute_source = get(snmp_settings, "compute_local_engineid_source", default="hostname_and_ip")
        if compute_source == "hostname_and_ip":
            # Accepting SonarLint issue: The weak sha1 is not used for encryption. Just to create a unique engine id.
            local_engine_id = sha1(f"{self.shared_utils.hostname}{self.shared_utils.mgmt_ip}".encode()).hexdigest()  # NOSONAR # noqa: S324
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

    def _snmp_location(self: AvdStructuredConfigBase, snmp_settings: dict) -> str | None:
        """
        Return location if "snmp_settings.location" is True.

        Otherwise return None.
        """
        if snmp_settings.get("location") is not True:
            return None

        location_elements = [
            self.shared_utils.fabric_name,
            self.shared_utils.dc_name,
            self.shared_utils.pod_name,
            self.shared_utils.rack,
            self.shared_utils.hostname,
        ]
        location_elements = [location for location in location_elements if location not in [None, ""]]
        return " ".join(location_elements)

    def _snmp_users(self: AvdStructuredConfigBase, snmp_settings: dict, engine_ids: dict | None) -> list | None:
        """
        Return users if "snmp_settings.users" is set.

        Otherwise return None.

        Users will have computed localized keys if configured.
        """
        if not (users := snmp_settings.get("users")):
            # Empty list or None
            return None

        snmp_users = []
        compute_v3_user_localized_key = (
            (engine_ids is not None) and (engine_ids.get("local") is not None) and (snmp_settings.get("compute_v3_user_localized_key") is True)
        )
        for user in users:
            version = user.get("version")
            user_dict = {
                "name": user.get("name"),
                "group": user.get("group"),
                "version": version,
            }
            if version == "v3":
                if compute_v3_user_localized_key:
                    user_dict["localized"] = engine_ids["local"]

                auth = user.get("auth")
                auth_passphrase = user.get("auth_passphrase")
                if auth is not None and auth_passphrase is not None:
                    user_dict["auth"] = auth
                    if compute_v3_user_localized_key:
                        hash_filter = {"passphrase": auth_passphrase, "auth": auth, "engine_id": engine_ids["local"]}
                        user_dict["auth_passphrase"] = snmp_hash(hash_filter)
                    else:
                        user_dict["auth_passphrase"] = auth_passphrase

                    priv = user.get("priv")
                    priv_passphrase = user.get("priv_passphrase")
                    if priv is not None and priv_passphrase is not None:
                        user_dict["priv"] = priv
                        if compute_v3_user_localized_key:
                            hash_filter.update({"passphrase": priv_passphrase, "priv": priv})
                            user_dict["priv_passphrase"] = snmp_hash(hash_filter)
                        else:
                            user_dict["priv_passphrase"] = priv_passphrase

            snmp_users.append(user_dict)

        return snmp_users or None

    def _snmp_hosts(self: AvdStructuredConfigBase, snmp_settings: dict) -> list | None:
        """
        Return hosts if "snmp_settings.hosts" is set.

        Otherwise return None.

        Hosts may have management VRFs dynamically set.
        """
        if not (hosts := snmp_settings.get("hosts")):
            # Empty list or None
            return None

        snmp_hosts = []

        has_mgmt_ip = (self.shared_utils.mgmt_ip is not None) or (self.shared_utils.ipv6_mgmt_ip is not None)

        for host in natural_sort(hosts, "host"):
            vrfs = set()
            if (vrf := host.pop("vrf", None)) is not None:
                vrfs.add(vrf)

            if (use_mgmt_interface_vrf := host.pop("use_mgmt_interface_vrf", False)) is True and has_mgmt_ip:
                vrfs.add(self.shared_utils.mgmt_interface_vrf)

            if (use_inband_mgmt_vrf := host.pop("use_inband_mgmt_vrf", False)) is True and self.shared_utils.inband_mgmt_interface is not None:
                # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
                vrfs.add(self.shared_utils.inband_mgmt_vrf or "default")

            if not any([vrfs, use_mgmt_interface_vrf, use_inband_mgmt_vrf]):
                # If no VRFs are defined (and we are not just ignoring missing mgmt config)
                vrfs.add("default")

            # Ensure default VRF is added first
            if "default" in vrfs:
                vrfs.remove("default")
                # Add host without VRF field
                snmp_hosts.append(host)

            # Add host with VRF field.
            snmp_hosts.extend({**host, "vrf": vrf} for vrf in natural_sort(vrfs))

        return snmp_hosts or None

    def _snmp_local_interfaces(self: AvdStructuredConfigBase, source_interfaces_inputs: dict | None) -> list | None:
        """
        Return local_interfaces if "source_interfaces.snmp" is set.

        Otherwise return None.
        """
        if not source_interfaces_inputs:
            # Empty dict or None
            return None

        local_interfaces = self._build_source_interfaces(
            source_interfaces_inputs.get("mgmt_interface", False),
            source_interfaces_inputs.get("inband_mgmt_interface", False),
            "SNMP",
        )
        return local_interfaces or None

    def _snmp_vrfs(self: AvdStructuredConfigBase, snmp_settings: dict | None) -> list | None:
        """
        Return list of dicts for enabling/disabling SNMP for VRFs.

        Requires one of the following options to be set under snmp_settings:
        - vrfs
        - enable_mgmt_interface_vrf
        - enable_inband_mgmt_vrf
        Otherwise return None.
        """
        if snmp_settings is None:
            return None

        has_mgmt_ip = (self.shared_utils.mgmt_ip is not None) or (self.shared_utils.ipv6_mgmt_ip is not None)

        # Initialize a set with all vrfs (Catching None value with or [])
        vrfs = get(snmp_settings, "vrfs", default=[])
        if has_mgmt_ip and (enable_mgmt_interface_vrf := snmp_settings.get("enable_mgmt_interface_vrf")) is not None:
            vrf = {
                "name": self.shared_utils.mgmt_interface_vrf,
                "enable": enable_mgmt_interface_vrf,
            }
            replace_or_append_item(vrfs, "name", vrf)

        if (enable_inband_mgmt_vrf := snmp_settings.get("enable_inband_mgmt_vrf")) is not None and self.shared_utils.inband_mgmt_interface is not None:
            # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
            vrf = {
                "name": self.shared_utils.inband_mgmt_vrf or "default",
                "enable": enable_inband_mgmt_vrf,
            }
            replace_or_append_item(vrfs, "name", vrf)

        return natural_sort(vrfs, "name") or None
