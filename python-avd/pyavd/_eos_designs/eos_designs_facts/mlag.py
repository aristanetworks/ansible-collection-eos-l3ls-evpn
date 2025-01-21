# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import EosDesignsFacts


class MlagMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mlag_peer(self: EosDesignsFacts) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return self.shared_utils.mlag_peer
        return None

    @cached_property
    def mlag_port_channel_id(self: EosDesignsFacts) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return self.shared_utils.mlag_port_channel_id
        return None

    @cached_property
    def mlag_interfaces(self: EosDesignsFacts) -> list | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return self.shared_utils.mlag_interfaces
        return None

    @cached_property
    def mlag_ip(self: EosDesignsFacts) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return self.shared_utils.mlag_ip
        return None

    @cached_property
    def mlag_l3_ip(self: EosDesignsFacts) -> str | None:
        """
        Exposed in avd_switch_facts.

        Only if L3 and not running rfc5549 for both underlay and overlay
        """
        if (
            self.shared_utils.mlag_l3
            and self.shared_utils.mlag_peer_l3_vlan is not None
            and not (self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549)
        ):
            return self.shared_utils.mlag_l3_ip
        return None

    @cached_property
    def mlag_switch_ids(self: EosDesignsFacts) -> dict | None:
        """
        Exposed in avd_switch_facts.

        Returns the switch id's of both primary and secondary switches for a given node group
        {"primary": int, "secondary": int}
        """
        return self.shared_utils.mlag_switch_ids
