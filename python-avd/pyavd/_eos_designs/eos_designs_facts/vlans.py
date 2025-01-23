# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd.j2filters import list_compress

from .utils import UtilsMixin


class VlansMixin(UtilsMixin):
    """
    Mixin Class used to generate some of the EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def vlans(self) -> str:
        """
        Exposed in avd_switch_facts.

        Return the compressed list of vlans to be defined on this switch

        Ex. "1-100, 201-202"

        This excludes the optional "uplink_native_vlan" if that vlan is not used for anything else.
        This is to ensure that native vlan is not necessarily permitted on the uplink trunk.
        """
        return list_compress(self._vlans)

    @cached_property
    def local_endpoint_trunk_groups(self) -> list[str]:
        """
        Return list of trunk_groups in use by endpoints connected to this switch only.

        Used for only applying the trunk groups in config that are relevant on this device
        This is a subset of endpoint_trunk_groups which is used for filtering.
        """
        if self.shared_utils.only_local_vlan_trunk_groups:
            _, local_endpoint_trunk_groups = self._local_endpoint_vlans_and_trunk_groups
            return list(local_endpoint_trunk_groups)

        return []

    @cached_property
    def endpoint_trunk_groups(self) -> list[str]:
        """
        Return list of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer.

        Used for filtering which vlans we configure on the device. This is a superset of local_endpoint_trunk_groups.
        """
        return list(self._endpoint_trunk_groups)
