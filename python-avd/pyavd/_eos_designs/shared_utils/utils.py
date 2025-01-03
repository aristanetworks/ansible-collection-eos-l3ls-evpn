# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import get, template_var

if TYPE_CHECKING:
    from typing import TypeVar

    from pyavd._eos_designs.eos_designs_facts import EosDesignsFacts
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtils

    ADAPTER_SETTINGS = TypeVar(
        "ADAPTER_SETTINGS", EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem, EosDesigns.NetworkPortsItem
    )


class UtilsMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def get_peer_facts(self: SharedUtils, peer_name: str, required: bool = True) -> EosDesignsFacts | dict | None:
        """
        util function to retrieve peer_facts for peer_name.

        returns avd_switch_facts.{peer_name}.switch

        by default required is True and so the function will raise is peer_facts cannot be found
        using the separator `..` to be able to handle hostnames with `.` inside
        """
        return get(
            self.hostvars,
            f"avd_switch_facts..{peer_name}..switch",
            separator="..",
            required=required,
            custom_error_msg=(
                f"Facts not found for node '{peer_name}'. Something in the input vars is pointing to this node. "
                f"Check that '{peer_name}' is in the inventory and is part of the group set by 'fabric_name'. Node is required."
            ),
        )

    def template_var(self: SharedUtils, template_file: str, template_vars: dict) -> str:
        """Run the simplified templater using the passed Ansible "templar" engine."""
        try:
            return template_var(template_file, template_vars, self.templar)
        except Exception as e:
            msg = f"Error during templating of template: {template_file}"
            raise AristaAvdError(msg) from e

    @lru_cache  # noqa: B019
    def get_merged_port_profile(self: SharedUtils, profile_name: str, context: str) -> EosDesigns.PortProfilesItem:
        """Return list of merged "port_profiles" where "parent_profile" has been applied."""
        if profile_name not in self.inputs.port_profiles:
            msg = f"Profile '{profile_name}' applied under '{context}' does not exist in `port_profiles`."
            raise AristaAvdInvalidInputsError(msg)

        port_profile = self.inputs.port_profiles[profile_name]
        if port_profile.parent_profile:
            if port_profile.parent_profile not in self.inputs.port_profiles:
                msg = f"Profile '{port_profile.parent_profile}' applied under port profile '{profile_name}' does not exist in `port_profiles`."
                raise AristaAvdInvalidInputsError(msg)

            parent_profile = self.inputs.port_profiles[port_profile.parent_profile]

            # Notice reuse of the same variable with the merged content.
            port_profile = port_profile._deepinherited(parent_profile)

        delattr(port_profile, "parent_profile")
        return port_profile

    def get_merged_adapter_settings(self: SharedUtils, adapter_or_network_port_settings: ADAPTER_SETTINGS) -> ADAPTER_SETTINGS:
        """
        Applies port-profiles to the given adapter_or_network_port and returns the combined result.

        Args:
            adapter_or_network_port_settings: can either be an adapter of a connected endpoint or one item under network_ports.
            context: a context string for error messages.
        """
        # Deepcopy to avoid modifying the original.
        adapter_or_network_port_settings = adapter_or_network_port_settings._deepcopy()

        if (profile_name := adapter_or_network_port_settings.profile) is None:
            # No profile to apply
            return adapter_or_network_port_settings

        adapter_profile = self.get_merged_port_profile(profile_name, adapter_or_network_port_settings._context)
        profile_as_adapter_or_network_port_settings = adapter_profile._cast_as(type(adapter_or_network_port_settings))
        adapter_or_network_port_settings._deepinherit(profile_as_adapter_or_network_port_settings)
        return adapter_or_network_port_settings
