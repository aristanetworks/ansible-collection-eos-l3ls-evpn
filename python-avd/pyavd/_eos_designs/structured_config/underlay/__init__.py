# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, StructuredConfigGeneratorProtocol

from .agents import AgentsMixin
from .as_path import AsPathMixin
from .dhcp_servers import DhcpServersMixin
from .ethernet_interfaces import EthernetInterfacesMixin
from .ip_access_lists import IpAccesslistsMixin
from .loopback_interfaces import LoopbackInterfacesMixin
from .mpls import MplsMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .prefix_lists import PrefixListsMixin
from .route_maps import RouteMapsMixin
from .router_bgp import RouterBgpMixin
from .router_isis import RouterIsisMixin
from .router_msdp import RouterMsdpMixin
from .router_ospf import RouterOspfMixin
from .router_pim_sparse_mode import RouterPimSparseModeMixin
from .standard_access_lists import StandardAccessListsMixin
from .static_routes import StaticRoutesMixin
from .utils import UtilsMixin
from .vlans import VlansMixin


class AvdStructuredConfigUnderlayProtocol(
    VlansMixin,
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    LoopbackInterfacesMixin,
    RouterBgpMixin,
    AsPathMixin,
    RouterOspfMixin,
    PrefixListsMixin,
    RouteMapsMixin,
    RouterIsisMixin,
    RouterMsdpMixin,
    RouterPimSparseModeMixin,
    StandardAccessListsMixin,
    StaticRoutesMixin,
    MplsMixin,
    AgentsMixin,
    IpAccesslistsMixin,
    DhcpServersMixin,
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


class AvdStructuredConfigUnderlay(StructuredConfigGenerator, AvdStructuredConfigUnderlayProtocol):
    """
    The AvdStructuredConfig Class is imported used "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to get the render, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """
