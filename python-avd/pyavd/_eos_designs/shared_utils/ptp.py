# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtilsProtocol


class PtpMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def ptp_enabled(self: SharedUtilsProtocol) -> bool:
        default_ptp_enabled = self.inputs.ptp_settings.enabled
        return bool(default(self.node_config.ptp.enabled, default_ptp_enabled))

    @cached_property
    def ptp_profile_name(self: SharedUtilsProtocol) -> str:
        default_ptp_profile = self.inputs.ptp_settings.profile
        return self.node_config.ptp.profile or default_ptp_profile

    @cached_property
    def ptp_profile(self: SharedUtilsProtocol) -> EosDesigns.PtpProfilesItem:
        if self.ptp_profile_name not in self.inputs.ptp_profiles:
            msg = f"PTP Profile '{self.ptp_profile_name}' referenced under `ptp.profile` node variables does not exist in `ptp_profiles`."
            raise AristaAvdInvalidInputsError(msg)

        return self.inputs.ptp_profiles[self.ptp_profile_name]
