# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator, StructuredConfigGeneratorProtocol

from .ethernet_interfaces import EthernetInterfacesMixin
from .monitor_sessions import MonitorSessionsMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .utils import UtilsMixin


class AvdStructuredConfigConnectedEndpointsProtocol(
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    MonitorSessionsMixin,
    UtilsMixin,
    StructuredConfigGeneratorProtocol,
    Protocol,
):
    """
    Protocol for the AvdStructuredConfig Class which is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to inherit the _hostvars, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    def render(self) -> None:
        """Wrap class render function with a check if connected_endpoints feature is enabled."""
        if self.shared_utils.connected_endpoints:
            return super().render()

        return None


class AvdStructuredConfigConnectedEndpoints(StructuredConfigGenerator, AvdStructuredConfigConnectedEndpointsProtocol):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to inherit the _hostvars, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """
