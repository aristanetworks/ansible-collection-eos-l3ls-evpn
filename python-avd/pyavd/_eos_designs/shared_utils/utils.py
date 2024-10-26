# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import get, get_item, merge, template_var

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts import EosDesignsFacts

    from . import SharedUtils


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
    def get_merged_port_profile(self: SharedUtils, profile_name: str, context: str) -> list:
        """Return list of merged "port_profiles" where "parent_profile" has been applied."""
        msg = f"Profile '{profile_name}' applied under '{context}' does not exist in `port_profiles`."
        port_profile = get_item(self.port_profiles, "profile", profile_name, required=True, custom_error_msg=msg)
        if "parent_profile" in port_profile:
            msg = f"Profile '{port_profile['parent_profile']}' applied under port profile '{profile_name}' does not exist in `port_profiles`."
            parent_profile = get_item(self.port_profiles, "profile", port_profile["parent_profile"], required=True, custom_error_msg=msg)
            # Notice reuse of the same variable with the merged content.
            port_profile = merge(parent_profile, port_profile, list_merge="replace", destructive_merge=False)
            port_profile.pop("parent_profile")

        return port_profile

    def get_merged_adapter_settings(self: SharedUtils, adapter_or_network_port_settings: dict) -> dict:
        """
        Applies port-profiles to the given adapter_or_network_port and returns the combined result.

        Args:
            adapter_or_network_port_settings: can either be an adapter of a connected endpoint or one item under network_ports.
            context: a context string for error messages.
        """
        if (profile_name := adapter_or_network_port_settings.get("profile")) is None:
            # No profile to apply
            return adapter_or_network_port_settings

        adapter_profile = self.get_merged_port_profile(profile_name, adapter_or_network_port_settings["context"])
        return merge(adapter_profile, adapter_or_network_port_settings, list_merge="replace", destructive_merge=False)
