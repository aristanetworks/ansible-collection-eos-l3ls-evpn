from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.roles.eos_designs.python_modules.network_services.utils import UtilsMixin


class RouterIsisMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_isis(self) -> dict | None:
        """
        return structured config for router_isis

        Used for non-EVPN where underlay_routing_protocol is ISIS,
        static routes in VRF "default" should be redistributed into ISIS
        """

        if (
            self._network_services_l3
            and self._vrf_default_ipv4_static_routes
            and self._underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]
            and not (self._overlay_vtep and self._overlay_evpn)
        ):
            return {"redistribute_routes": [{"source_protocol": "static"}]}

        return None
