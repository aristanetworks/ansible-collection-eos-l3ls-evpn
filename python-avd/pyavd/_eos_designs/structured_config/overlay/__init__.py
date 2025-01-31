# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, StructuredConfigGeneratorProtocol

from .cvx import CvxMixin
from .ip_extcommunity_lists import IpExtCommunityListsMixin
from .ip_security import IpSecurityMixin
from .management_cvx import ManagementCvxMixin
from .management_security import ManagementSecurityMixin
from .route_maps import RouteMapsMixin
from .router_adaptive_virtual_topology import RouterAdaptiveVirtualTopologyMixin
from .router_bfd import RouterBfdMixin
from .router_bgp import RouterBgpMixin
from .router_path_selection import RouterPathSelectionMixin
from .router_traffic_engineering import RouterTrafficEngineering
from .stun import StunMixin
from .utils import UtilsMixin


class AvdStructuredConfigOverlayProtocol(
    CvxMixin,
    IpExtCommunityListsMixin,
    IpSecurityMixin,
    ManagementCvxMixin,
    ManagementSecurityMixin,
    RouterAdaptiveVirtualTopologyMixin,
    RouterBfdMixin,
    RouterBgpMixin,
    RouteMapsMixin,
    RouterPathSelectionMixin,
    RouterTrafficEngineering,
    StunMixin,
    UtilsMixin,
    StructuredConfigGeneratorProtocol,
    Protocol,
):
    """
    Protocol for the AvdStructuredConfig Class which is imported used "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to get the render, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    def render(self) -> None:
        """
        Wrap class render function with a check if one of the following vars are True.

        - overlay_cvx
        - overlay_evpn
        - overlay_vpn_ipv4
        - overlay_vpn_ipv6.
        """
        if any(
            [
                self.shared_utils.overlay_cvx,
                self.shared_utils.overlay_evpn,
                self.shared_utils.overlay_vpn_ipv4,
                self.shared_utils.overlay_vpn_ipv6,
                self.shared_utils.is_wan_router,
            ],
        ):
            return super().render()
        return None


class AvdStructuredConfigOverlay(StructuredConfigGenerator, AvdStructuredConfigOverlayProtocol):
    """
    The AvdStructuredConfig Class is imported used "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to get the render, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """
