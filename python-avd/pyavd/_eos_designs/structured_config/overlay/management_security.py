# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class ManagementSecurityMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def management_security(self: AvdStructuredConfigOverlay) -> dict | None:
        """
        Return structured config for management_security.

        Currently only relevant on WAN routers where STUN DTLS has not been disabled.
        """
        if (profile_name := self.shared_utils.wan_stun_dtls_profile_name) is None:
            return None

        return {
            "ssl_profiles": [
                {
                    "name": profile_name,
                    "certificate": {
                        "file": f"{profile_name}.crt",
                        "key": f"{profile_name}.key",
                    },
                    "trust_certificate": {"certificates": ["aristaDeviceCertProvisionerDefaultRootCA.crt"]},
                    "tls_versions": "1.2",
                },
            ],
        }
