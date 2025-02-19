# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtilsProtocol


class CvTopology(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def cv_topology(self: SharedUtilsProtocol) -> EosDesigns.CvTopologyItem | None:
        """
        Returns the cv_topology for this device.

        {
            hostname: <str>,
            platform: <str | None>,
            interfaces: [
                {
                    name: <str>
                    neighbor: <str>
                    neighbor_interface: <str>
                }
            ].
        }
        """
        if not self.inputs.use_cv_topology:
            return None

        if not self.inputs.cv_topology:
            msg = "Found 'use_cv_topology:true' so 'cv_topology' is required."
            raise AristaAvdInvalidInputsError(msg)

        if self.hostname not in self.inputs.cv_topology:
            # Ignoring missing data for this device in cv_topology. Historic behavior and needed for hybrid scenarios.
            return None

        return self.inputs.cv_topology[self.hostname]

    @cached_property
    def cv_topology_platform(self: SharedUtilsProtocol) -> str | None:
        if self.cv_topology is not None:
            return self.cv_topology.platform
        return None

    @cached_property
    def cv_topology_config(self: SharedUtilsProtocol) -> dict:
        """
        Returns dict with keys derived from cv topology (or empty dict).

        {
            uplink_interfaces: list[str]
            uplink_switches: list[str]
            uplink_switch_interfaces: list[str]
            mlag_interfaces: list[str]
            mlag_peer: <str>
            mgmt_interface: <str>
        }
        """
        if self.cv_topology is None:
            return {}

        cv_interfaces = self.cv_topology.interfaces

        if not self.default_interfaces.uplink_interfaces:
            msg = "Found 'use_cv_topology:true' so 'default_interfaces.[].uplink_interfaces' is required."
            raise AristaAvdInvalidInputsError(msg)

        config = {}
        for uplink_interface in range_expand(self.default_interfaces.uplink_interfaces):
            if cv_interface := cv_interfaces.get(uplink_interface):
                config.setdefault("uplink_interfaces", []).append(cv_interface.name)
                config.setdefault("uplink_switches", []).append(cv_interface.neighbor)
                config.setdefault("uplink_switch_interfaces", []).append(cv_interface.neighbor_interface)

        if not self.mlag:
            return config

        if not self.default_interfaces.mlag_interfaces:
            msg = "Found 'use_cv_topology:true' so 'default_interfaces.[].mlag_interfaces' is required."
            raise AristaAvdInvalidInputsError(msg)

        for mlag_interface in range_expand(self.default_interfaces.mlag_interfaces):
            if cv_interface := cv_interfaces.get(mlag_interface, default=None):
                config.setdefault("mlag_interfaces", []).append(cv_interface.name)
                # TODO: Set mlag_peer once we get a user-defined var for that.
                # TODO: config["mlag_peer"] = cv_interface["neighbor"]

        for cv_interface in cv_interfaces:
            if cv_interface.name.startswith("Management"):
                config["mgmt_interface"] = cv_interface.name

        return config
