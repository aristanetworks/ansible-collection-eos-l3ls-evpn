# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class RouterIsisMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_isis(self: AvdStructuredConfigUnderlay) -> dict | None:
        """Return structured config for router_isis."""
        if self.shared_utils.underlay_isis is not True:
            return None

        router_isis = {
            "instance": self.shared_utils.isis_instance_name,
            "log_adjacency_changes": True,
            "net": self._isis_net,
            "router_id": self.shared_utils.router_id if not self.shared_utils.use_router_general_for_router_id else None,
            "is_type": self._is_type,
            "address_family_ipv4": {"enabled": True, "maximum_paths": get(self._hostvars, "isis_maximum_paths", default=4)},
        }

        if self.shared_utils.underlay_ldp is True:
            router_isis["mpls_ldp_sync_default"] = True

        # TI-LFA
        if get(self._hostvars, "isis_ti_lfa.enabled") is True:
            router_isis["timers"] = {
                "local_convergence": {
                    "delay": get(self._hostvars, "isis_ti_lfa.local_convergence_delay", default="10000"),
                    "protected_prefixes": True,
                },
            }
        ti_lfa_protection = get(self._hostvars, "isis_ti_lfa.protection")
        if ti_lfa_protection == "link":
            router_isis["address_family_ipv4"]["fast_reroute_ti_lfa"] = {"mode": "link-protection"}
        elif ti_lfa_protection == "node":
            router_isis["address_family_ipv4"]["fast_reroute_ti_lfa"] = {"mode": "node-protection"}

        # Overlay protocol
        if self.shared_utils.overlay_routing_protocol == "none":
            router_isis["redistribute_routes"] = [{"source_protocol": "connected"}]

        if self.shared_utils.underlay_sr is True:
            router_isis["advertise"] = {
                "passive_only": get(self._hostvars, "isis_advertise_passive_only", default=False),
            }
            # TODO: - enabling IPv6 only in SR cases as per existing behavior
            # but this could probably be taken out
            if self.shared_utils.underlay_ipv6 is True:
                router_isis["address_family_ipv6"] = {"enabled": True, "maximum_paths": get(self._hostvars, "isis_maximum_paths", default=4)}
                if ti_lfa_protection == "link":
                    router_isis["address_family_ipv6"]["fast_reroute_ti_lfa"] = {"mode": "link-protection"}
                elif ti_lfa_protection == "node":
                    router_isis["address_family_ipv6"]["fast_reroute_ti_lfa"] = {"mode": "node-protection"}
            router_isis["segment_routing_mpls"] = {"router_id": self.shared_utils.router_id, "enabled": True}

        return strip_empties_from_dict(router_isis)

    @cached_property
    def _isis_net(self: AvdStructuredConfigUnderlay) -> str | None:
        if get(self._hostvars, "isis_system_id_format") == "node_id":
            isis_system_id_prefix = get(self.shared_utils.switch_data_combined, "isis_system_id_prefix")
            if self.shared_utils.underlay_isis is True and isis_system_id_prefix is None:
                msg = (
                    f"'isis_system_id_prefix' is required when 'isis_system_id_format' is set to 'node_id'."
                    f" 'isis_system_id_prefix' was not set for '{self.shared_utils.hostname}'"
                )
                raise AristaAvdInvalidInputsError(msg)

            if self.shared_utils.id is None:
                msg = f"'id' is not set on '{self.shared_utils.hostname}' and is required to set ISIS NET address using the node ID"
                raise AristaAvdInvalidInputsError(msg)
            system_id = f"{isis_system_id_prefix}.{self.shared_utils.id:04d}"
        else:
            system_id = self.ipv4_to_isis_system_id(self.shared_utils.router_id)

        isis_area_id = get(self._hostvars, "isis_area_id", default="49.0001")
        return f"{isis_area_id}.{system_id}.00"

    @cached_property
    def _is_type(self: AvdStructuredConfigUnderlay) -> str:
        default_is_type = get(self._hostvars, "isis_default_is_type", default="level-2")
        is_type = str(get(self.shared_utils.switch_data_combined, "is_type", default=default_is_type)).lower()
        if is_type not in ["level-1", "level-2", "level-1-2"]:
            is_type = "level-2"
        return is_type

    @staticmethod
    def ipv4_to_isis_system_id(ipv4_address: str) -> str:
        """
        Converts an IPv4 address into an IS-IS system-id.

        Examples:
        192.168.0.1 -> 1921.6800.0001
        10.0.0.3 -> 0100.0000.0003
        """
        octets = str(ipv4_address).split(".")
        padded_addr = octets[0].zfill(3) + octets[1].zfill(3) + octets[2].zfill(3) + octets[3].zfill(3)
        return ".".join(padded_addr[i : i + 4] for i in range(0, len(padded_addr), 4))
