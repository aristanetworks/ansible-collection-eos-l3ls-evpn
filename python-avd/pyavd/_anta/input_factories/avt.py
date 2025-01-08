# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.avt import VerifyAVTRole

from ._base_classes import AntaTestInputFactory


class VerifyAVTRoleInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyAVTRole test.

    It collects the expected AVT topology role and reverses the role name
    if it is either `transit region` or `transit zone` to match EOS output.
    """

    def create(self) -> VerifyAVTRole.Input | None:
        """Create Input for the VerifyAVTRole test."""
        role = self.structured_config.router_adaptive_virtual_topology.topology_role
        # Reverse the role name if it is either `transit region` or `transit zone` to match EOS
        if role and role in ["transit region", "transit zone"]:
            role = " ".join(reversed(role.split()))

        return VerifyAVTRole.Input(role=role)
