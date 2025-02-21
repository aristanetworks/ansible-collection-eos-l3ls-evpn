# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError
from pyavd._utils import get_ip_from_ip_prefix
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class IpAccesslistsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _acl_internet_exit_zscaler(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        ip_access_list = EosCliConfigGen.IpAccessListsItem(name=self.get_internet_exit_nat_acl_name("zscaler"))
        ip_access_list.entries.append_new(sequence=10, action="permit", protocol="ip", source="any", destination="any")
        self.structured_config.ip_access_lists.append(ip_access_list)

    def _acl_internet_exit_direct(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        interface_ips = set()
        for ie_policy, connections in self._filtered_internet_exit_policies_and_connections:
            if ie_policy.type == "direct":
                for connection in connections:
                    interface_ips.add(connection["source_interface_ip_address"])

        if interface_ips:
            acl = EosCliConfigGen.IpAccessListsItem(name=self.get_internet_exit_nat_acl_name("direct"))
            interface_ips = sorted(interface_ips)
            i = 0
            for i, interface_ip in enumerate(interface_ips):
                acl.entries.append_new(sequence=10 + i * 10, action="deny", protocol="ip", source=get_ip_from_ip_prefix(interface_ip), destination="any")
            acl.entries.append_new(
                sequence=20 + i * 10,
                action="permit",
                protocol="ip",
                source="any",
                destination="any",
            )

            self.structured_config.ip_access_lists.append(acl)

    def _acl_internet_exit_user_defined(
        self: AvdStructuredConfigNetworkServicesProtocol, internet_exit_policy_type: Literal["zscaler", "direct"]
    ) -> list[dict] | None:
        acl_name = self.get_internet_exit_nat_acl_name(internet_exit_policy_type)
        if acl_name not in self.inputs.ipv4_acls:
            # TODO: Evaluate if we should continue so we raise when there is no ACL.
            return None

        # pass substitution fields as anything to check if acl requires substitution or not
        acl = self.shared_utils.get_ipv4_acl(acl_name, "random", interface_ip="random", peer_ip="random")
        if acl.name == acl_name:
            # ACL doesn't need replacement
            return acl

        # TODO: We still have one nat for all interfaces, need to also add logic to make nat per interface
        # if acl needs substitution
        msg = f"ipv4_acls[name={acl_name}] field substitution is not supported for internet exit access lists"
        raise AristaAvdError(msg)

    def _acl_internet_exit(self: AvdStructuredConfigNetworkServicesProtocol, internet_exit_policy_type: Literal["zscaler", "direct"]) -> None:
        acls = self._acl_internet_exit_user_defined(internet_exit_policy_type)
        if acls:
            self.structured_config.ip_access_lists.append(acls)

        elif internet_exit_policy_type == "zscaler":
            self._acl_internet_exit_zscaler()
        elif internet_exit_policy_type == "direct":
            self._acl_internet_exit_direct()

    @structured_config_contributor
    def ip_access_lists(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set the structured config for ip_access_lists."""
        if self._svi_acls:
            for interface_acls in self._svi_acls.values():
                for acl in interface_acls.values():
                    self.structured_config.ip_access_lists.append(acl)

        if self._l3_interface_acls:
            for l3_interface_acl in self._l3_interface_acls.values():
                for acl in l3_interface_acl.values():
                    self.structured_config.ip_access_lists.append(acl)

        for ie_policy_type in self._filtered_internet_exit_policy_types:
            self._acl_internet_exit(ie_policy_type)

        self.structured_config.ip_access_lists = EosCliConfigGen.IpAccessLists(natural_sort(self.structured_config.ip_access_lists, sort_key="name"))
