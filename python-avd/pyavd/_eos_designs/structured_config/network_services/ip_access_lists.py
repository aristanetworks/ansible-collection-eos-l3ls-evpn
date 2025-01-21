# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Literal

from pyavd._errors import AristaAvdError
from pyavd._utils import append_if_not_duplicate, get_ip_from_ip_prefix
from pyavd.j2filters import natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class IpAccesslistsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _acl_internet_exit_zscaler(self: AvdStructuredConfigNetworkServices) -> dict:
        return {
            "name": self.get_internet_exit_nat_acl_name("zscaler"),
            "entries": [
                {
                    "sequence": 10,
                    "action": "permit",
                    "protocol": "ip",
                    "source": "any",
                    "destination": "any",
                },
            ],
        }

    @cached_property
    def _acl_internet_exit_direct(self: AvdStructuredConfigNetworkServices) -> dict | None:
        interface_ips = set()
        for ie_policy, connections in self._filtered_internet_exit_policies_and_connections:
            if ie_policy.type == "direct":
                for connection in connections:
                    interface_ips.add(connection["source_interface_ip_address"])

        if interface_ips:
            interface_ips = sorted(interface_ips)
            entries = []
            i = 0
            for i, interface_ip in enumerate(interface_ips):
                entries.append(
                    {
                        "sequence": 10 + i * 10,
                        "action": "deny",
                        "protocol": "ip",
                        "source": get_ip_from_ip_prefix(interface_ip),
                        "destination": "any",
                    },
                )
            entries.append(
                {
                    "sequence": 20 + i * 10,
                    "action": "permit",
                    "protocol": "ip",
                    "source": "any",
                    "destination": "any",
                },
            )

            return {
                "name": self.get_internet_exit_nat_acl_name("direct"),
                "entries": entries,
            }
        return None

    def _acl_internet_exit_user_defined(self: AvdStructuredConfigNetworkServices, internet_exit_policy_type: Literal["zscaler", "direct"]) -> list[dict] | None:
        acl_name = self.get_internet_exit_nat_acl_name(internet_exit_policy_type)
        if acl_name not in self.inputs.ipv4_acls:
            # TODO: Evaluate if we should continue so we raise when there is no ACL.
            return None

        # pass substitution fields as anything to check if acl requires substitution or not
        acl = self.shared_utils.get_ipv4_acl(acl_name, "random", interface_ip="random", peer_ip="random")
        if acl.name == acl_name:
            # ACL doesn't need replacement
            return [acl._as_dict()]

        # TODO: We still have one nat for all interfaces, need to also add logic to make nat per interface
        # if acl needs substitution
        msg = f"ipv4_acls[name={acl_name}] field substitution is not supported for internet exit access lists"
        raise AristaAvdError(msg)

    def _acl_internet_exit(self: AvdStructuredConfigNetworkServices, internet_exit_policy_type: Literal["zscaler", "direct"]) -> list[dict] | None:
        acls = self._acl_internet_exit_user_defined(internet_exit_policy_type)
        if acls:
            return acls

        if internet_exit_policy_type == "zscaler":
            return [self._acl_internet_exit_zscaler]
        if internet_exit_policy_type == "direct" and (acl := self._acl_internet_exit_direct):
            return [acl]
        return None

    @cached_property
    def ip_access_lists(self: AvdStructuredConfigNetworkServices) -> list | None:
        """Return structured config for ip_access_lists."""
        ip_access_lists = []
        if self._svi_acls:
            for interface_acls in self._svi_acls.values():
                for acl in interface_acls.values():
                    append_if_not_duplicate(ip_access_lists, "name", acl, context="IPv4 Access lists for SVI", context_keys=["name"])

        if self._l3_interface_acls:
            for l3_interface_acl in self._l3_interface_acls.values():
                for acl in l3_interface_acl.values():
                    append_if_not_duplicate(ip_access_lists, "name", acl, context="IPv4 Access lists for L3 interface", context_keys=["name"])

        for ie_policy_type in self._filtered_internet_exit_policy_types:
            acls = self._acl_internet_exit(ie_policy_type)
            if acls:
                ip_access_lists.extend(acls)

        return natural_sort(ip_access_lists, "name") or None
