# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get

from ._base_classes import AntaTestInputFactory, AntaTestInputFactoryFilter

if TYPE_CHECKING:
    from anta.tests.avt import VerifyAVTRole


class VerifyAVTRoleInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyAVTRole test.

    This factory creates test inputs for AVT role verification.

    It collect the expected AVT role and resversed the role name if role is either `transit region` or `transit zone`.

    """

    # TODO: Add filter class
    class Filter(AntaTestInputFactoryFilter):
        pass

    def create(self) -> VerifyAVTRole.Input | None:
        """Create Input for the VerifyAVTRole test."""
        # Retrieve AVT role from the structured configuration
        avt_role = get(self.manager.structured_config, "router_adaptive_virtual_topology.topology_role")
        if not avt_role:
            self.logger.debug(LogMessage.NO_INPUTS)
        # Translating avt role for transit region and zone due to json output
        if avt_role in ["transit region", "transit zone"]:
            avt_role = " ".join(reversed(avt_role.split()))

        return self.test.Input(role=avt_role)
