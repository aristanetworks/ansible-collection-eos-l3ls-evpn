# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default, strip_empties_from_dict

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
            "router_id": self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None,
            "is_type": self._is_type,
            "address_family_ipv4": {"enabled": True, "maximum_paths": self.inputs.isis_maximum_paths},
        }

        if self.shared_utils.underlay_ldp is True:
            router_isis["mpls_ldp_sync_default"] = True

        # TI-LFA
        if self.inputs.isis_ti_lfa.enabled:
            router_isis["timers"] = {
                "local_convergence": {
                    "delay": self.inputs.isis_ti_lfa.local_convergence_delay,
                    "protected_prefixes": True,
                },
            }
        if self.inputs.isis_ti_lfa.protection:
            router_isis["address_family_ipv4"]["fast_reroute_ti_lfa"] = {"mode": f"{self.inputs.isis_ti_lfa.protection}-protection"}

        # Overlay protocol
        if self.shared_utils.overlay_routing_protocol == "none":
            router_isis["redistribute_routes"] = [{"source_protocol": "connected"}]

        if self.shared_utils.underlay_sr is True:
            router_isis["advertise"] = {"passive_only": self.inputs.isis_advertise_passive_only}
            # TODO: - enabling IPv6 only in SR cases as per existing behavior
            # but this could probably be taken out
            if self.shared_utils.underlay_ipv6 is True:
                router_isis["address_family_ipv6"] = {"enabled": True, "maximum_paths": self.inputs.isis_maximum_paths}
                if self.inputs.isis_ti_lfa.protection:
                    router_isis["address_family_ipv6"]["fast_reroute_ti_lfa"] = {"mode": f"{self.inputs.isis_ti_lfa.protection}-protection"}
            router_isis["segment_routing_mpls"] = {"router_id": self.shared_utils.router_id, "enabled": True}

        return strip_empties_from_dict(router_isis)

    @cached_property
    def _isis_net(self: AvdStructuredConfigUnderlay) -> str | None:
        if self.inputs.isis_system_id_format == "node_id":
            isis_system_id_prefix = self.shared_utils.node_config.isis_system_id_prefix
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

        isis_area_id = self.inputs.isis_area_id
        return f"{isis_area_id}.{system_id}.00"

    @cached_property
    def _is_type(self: AvdStructuredConfigUnderlay) -> str:
        return default(self.shared_utils.node_config.is_type, self.inputs.isis_default_is_type)

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
