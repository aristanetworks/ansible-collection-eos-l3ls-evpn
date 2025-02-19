# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class ManagementSecurityMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def management_security(self: AvdStructuredConfigOverlayProtocol) -> None:
        """
        Set the structured config for management_security.

        Currently only relevant on WAN routers where STUN DTLS has not been disabled.
        """
        if (profile_name := self.shared_utils.wan_stun_dtls_profile_name) is None:
            return

        ssl_profile = EosCliConfigGen.ManagementSecurity.SslProfilesItem(
            name=profile_name,
            tls_versions="1.2",
        )
        ssl_profile.certificate._update(file=f"{profile_name}.crt", key=f"{profile_name}.key")
        ssl_profile.trust_certificate.certificates.append("aristaDeviceCertProvisionerDefaultRootCA.crt")
        self.structured_config.management_security.ssl_profiles.append(ssl_profile)
