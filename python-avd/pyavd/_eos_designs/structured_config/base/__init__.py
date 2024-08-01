# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._eos_designs.avdfacts import AvdFacts
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get, get_item, strip_empties_from_dict, strip_null_from_data
from pyavd.j2filters import natural_sort

from .ntp import NtpMixin
from .router_general import RouterGeneralMixin
from .snmp_server import SnmpServerMixin


class AvdStructuredConfigBase(AvdFacts, NtpMixin, SnmpServerMixin, RouterGeneralMixin):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses AvdFacts, as the base class, to inherit the _hostvars, keys and other attributes.
    Other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    @cached_property
    def hostname(self) -> str:
        return self.shared_utils.hostname

    @cached_property
    def is_deployed(self) -> bool:
        return self.shared_utils.is_deployed

    @cached_property
    def serial_number(self) -> str | None:
        """serial_number variable set based on serial_number fact."""
        return self.shared_utils.serial_number

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        Structured config for router_bgp.

        router_bgp set based on switch.bgp_as, switch.bgp_defaults, router_id facts and aggregating the values of bgp_maximum_paths and bgp_ecmp variables.
        """
        if self.shared_utils.bgp_as is None:
            return None

        platform_bgp_update_wait_for_convergence = (
            get(self.shared_utils.platform_settings, "feature_support.bgp_update_wait_for_convergence", default=True) is True
        )
        platform_bgp_update_wait_install = get(self.shared_utils.platform_settings, "feature_support.bgp_update_wait_install", default=True) is True

        if self.shared_utils.is_wan_router:
            # Special defaults for WAN routers
            default_maximum_paths = 16
            default_ecmp = None
        else:
            default_maximum_paths = 4
            default_ecmp = 4

        router_bgp = {
            "as": self.shared_utils.bgp_as,
            "router_id": self.shared_utils.router_id if not self.shared_utils.use_router_general_for_router_id else None,
            "distance": get(self._hostvars, "bgp_distance"),
            "bgp_defaults": get(self.shared_utils.switch_data_combined, "bgp_defaults"),
            "bgp": {
                "default": {
                    "ipv4_unicast": get(self._hostvars, "bgp_default_ipv4_unicast", default=False),
                },
            },
            "maximum_paths": {
                "paths": get(self._hostvars, "bgp_maximum_paths", default=default_maximum_paths),
                "ecmp": get(self._hostvars, "bgp_ecmp", default=default_ecmp),
            },
            "redistribute": self._router_bgp_redistribute_routes,
        }

        if get(self._hostvars, "bgp_update_wait_for_convergence", default=False) is True and platform_bgp_update_wait_for_convergence:
            router_bgp.setdefault("updates", {})["wait_for_convergence"] = True

        if get(self._hostvars, "bgp_update_wait_install", default=True) is True and platform_bgp_update_wait_install:
            router_bgp.setdefault("updates", {})["wait_install"] = True

        if get(self._hostvars, "bgp_graceful_restart.enabled") is True:
            router_bgp.update(
                {
                    "graceful_restart": {
                        "enabled": True,
                        "restart_time": get(self._hostvars, "bgp_graceful_restart.restart_time", default=300),
                    },
                },
            )

        l3_interfaces_neighbors = []
        for neighbor_info in self.shared_utils.l3_interfaces_bgp_neighbors:
            neighbor = {
                "ip_address": neighbor_info["ip_address"],
                "remote_as": neighbor_info["remote_as"],
                "description": neighbor_info["description"],
                "route_map_in": get(neighbor_info, "route_map_in"),
                "route_map_out": get(neighbor_info, "route_map_out"),
            }
            l3_interfaces_neighbors.append(strip_empties_from_dict(neighbor))

        if l3_interfaces_neighbors:
            router_bgp.update(
                {
                    "neighbors": l3_interfaces_neighbors,
                    "address_family_ipv4": {
                        "neighbors": [{"ip_address": neighbor["ip_address"], "activate": True} for neighbor in l3_interfaces_neighbors],
                    },
                }
            )

        return strip_null_from_data(router_bgp)

    @cached_property
    def static_routes(self) -> list | None:
        """static_routes set based on mgmt_gateway, mgmt_destination_networks and mgmt_interface_vrf."""
        if self.shared_utils.mgmt_gateway is None:
            return None

        if (mgmt_destination_networks := get(self._hostvars, "mgmt_destination_networks")) is not None:
            return [
                {
                    "vrf": self.shared_utils.mgmt_interface_vrf,
                    "destination_address_prefix": mgmt_destination_network,
                    "gateway": self.shared_utils.mgmt_gateway,
                }
                for mgmt_destination_network in mgmt_destination_networks
            ]

        return [
            {
                "vrf": self.shared_utils.mgmt_interface_vrf,
                "destination_address_prefix": "0.0.0.0/0",
                "gateway": self.shared_utils.mgmt_gateway,
            }
        ]

    @cached_property
    def ipv6_static_routes(self) -> list | None:
        """ipv6_static_routes set based on ipv6_mgmt_gateway, ipv6_mgmt_destination_networks and mgmt_interface_vrf."""
        if self.shared_utils.ipv6_mgmt_gateway is None or self.shared_utils.ipv6_mgmt_ip is None:
            return None

        if (ipv6_mgmt_destination_networks := get(self._hostvars, "ipv6_mgmt_destination_networks")) is not None:
            return [
                {
                    "vrf": self.shared_utils.mgmt_interface_vrf,
                    "destination_address_prefix": mgmt_destination_network,
                    "gateway": self.shared_utils.ipv6_mgmt_gateway,
                }
                for mgmt_destination_network in ipv6_mgmt_destination_networks
            ]

        return [
            {
                "vrf": self.shared_utils.mgmt_interface_vrf,
                "destination_address_prefix": "::/0",
                "gateway": self.shared_utils.ipv6_mgmt_gateway,
            },
        ]

    @cached_property
    def service_routing_protocols_model(self) -> str:
        """service_routing_protocols_model set to 'multi-agent'."""
        return "multi-agent"

    @cached_property
    def ip_routing(self) -> bool | None:
        """
        For l3 devices, configure ip routing unless ip_routing_ipv6_interfaces is True.

        For other devices only configure if "always_configure_ip_routing" is True.
        """
        if not self.shared_utils.underlay_router and not self.shared_utils.always_configure_ip_routing:
            return None

        if self.ip_routing_ipv6_interfaces is True:
            return None
        return True

    @cached_property
    def ipv6_unicast_routing(self) -> bool | None:
        """ipv6_unicast_routing set based on underlay_rfc5549 and underlay_ipv6."""
        if not self.shared_utils.underlay_router and not self.shared_utils.always_configure_ip_routing:
            return None

        if self.shared_utils.underlay_rfc5549 or self.shared_utils.underlay_ipv6:
            return True
        return None

    @cached_property
    def ip_routing_ipv6_interfaces(self) -> bool | None:
        """ip_routing_ipv6_interfaces set based on underlay_rfc5549 variable."""
        if not self.shared_utils.underlay_router and not self.shared_utils.always_configure_ip_routing:
            return None

        if self.shared_utils.underlay_rfc5549:
            return True
        return None

    @cached_property
    def router_multicast(self) -> dict | None:
        """router_multicast set based on underlay_multicast, underlay_router and switch.evpn_multicast facts."""
        if not self.shared_utils.underlay_multicast:
            return None

        router_multicast = {"ipv4": {"routing": True}}
        if self.shared_utils.evpn_multicast:
            router_multicast["ipv4"]["software_forwarding"] = "sfe"

        return router_multicast

    @cached_property
    def hardware_counters(self) -> dict | None:
        """hardware_counters set based on hardware_counters.features variable."""
        return get(self._hostvars, "hardware_counters")

    @cached_property
    def hardware(self) -> dict | None:
        """
        hardware set based on platform_speed_groups variable and switch.platform fact.

        Converting nested dict to list of dict to support avd_v4.0.
        """
        platform_speed_groups = get(self._hostvars, "platform_speed_groups")
        switch_platform = self.shared_utils.platform
        if platform_speed_groups is None or switch_platform is None:
            return None

        tmp_speed_groups = {}
        for platform_item in platform_speed_groups:
            if platform_item["platform"] == switch_platform:
                speeds = platform_item.get("speeds")
                for speed in natural_sort(speeds, "speed"):
                    for speed_group in speed["speed_groups"]:
                        tmp_speed_groups[speed_group] = speed["speed"]

        if tmp_speed_groups:
            hardware = {"speed_groups": []}
            for speed_group in natural_sort(tmp_speed_groups):
                hardware["speed_groups"].append({"speed_group": speed_group, "serdes": tmp_speed_groups[speed_group]})
            return hardware
        return None

    @cached_property
    def daemon_terminattr(self) -> dict | None:
        """
        daemon_terminattr set based on cvp_instance_ips.

        Updating cvaddrs and cvauth considering conditions for cvaas and cvp_on_prem IPs

            if 'arista.io' in cvp_instance_ips:
                 <updating as cvaas_ip>
            else:
                 <updating as cvp_on_prem ip>
        """
        cvp_instance_ip_list = get(self._hostvars, "cvp_instance_ips", [])
        if not cvp_instance_ip_list:
            return None

        daemon_terminattr = {"cvaddrs": []}
        for cvp_instance_ip in cvp_instance_ip_list:
            if "arista.io" in cvp_instance_ip:
                # updating for cvaas_ips
                daemon_terminattr["cvaddrs"].append(f"{cvp_instance_ip}:443")
                daemon_terminattr["cvauth"] = {
                    "method": "token-secure",
                    # Ignoring sonar-lint false positive for tmp path since this is config for EOS
                    "token_file": get(self._hostvars, "cvp_token_file", "/tmp/cv-onboarding-token"),  # NOSONAR # noqa: S108
                }
            else:
                # updating for cvp_on_prem_ips
                cv_address = f"{cvp_instance_ip}:{get(self._hostvars, 'terminattr_ingestgrpcurl_port', default=9910)}"
                daemon_terminattr["cvaddrs"].append(cv_address)
                if (cvp_ingestauth_key := get(self._hostvars, "cvp_ingestauth_key")) is not None:
                    daemon_terminattr["cvauth"] = {
                        "method": "key",
                        "key": cvp_ingestauth_key,
                    }
                else:
                    daemon_terminattr["cvauth"] = {
                        "method": "token",
                        # Ignoring sonar-lint false positive for tmp path since this is config for EOS
                        "token_file": get(self._hostvars, "cvp_token_file", "/tmp/token"),  # NOSONAR # noqa: S108
                    }

        daemon_terminattr["cvvrf"] = self.shared_utils.mgmt_interface_vrf
        daemon_terminattr["smashexcludes"] = get(self._hostvars, "terminattr_smashexcludes", default="ale,flexCounter,hardware,kni,pulse,strata")
        daemon_terminattr["ingestexclude"] = get(self._hostvars, "terminattr_ingestexclude", default="/Sysdb/cell/1/agent,/Sysdb/cell/2/agent")
        daemon_terminattr["disable_aaa"] = get(self._hostvars, "terminattr_disable_aaa", False)

        return daemon_terminattr

    @cached_property
    def vlan_internal_order(self) -> dict | None:
        """vlan_internal_order set based on internal_vlan_order data-model."""
        if self.shared_utils.wan_role:
            return None

        default_internal_vlan_order = {
            "allocation": "ascending",
            "range": {
                "beginning": 1006,
                "ending": 1199,
            },
        }
        return get(self._hostvars, "internal_vlan_order", default=default_internal_vlan_order)

    @cached_property
    def aaa_root(self) -> dict:
        """aaa_root.disable is always set to match EOS default config and historic configs."""
        return {"disabled": True}

    @cached_property
    def config_end(self) -> bool:
        """config_end is always set to match EOS default config and historic configs."""
        return True

    @cached_property
    def enable_password(self) -> dict:
        """enable_password.disable is always set to match EOS default config and historic configs."""
        return {"disabled": True}

    @cached_property
    def transceiver_qsfp_default_mode_4x10(self) -> bool:
        """
        transceiver_qsfp_default_mode_4x10 is on for all devices except WAN routers.

        TODO: Add platform_setting to control this.
        """
        return not self.shared_utils.is_wan_router

    @cached_property
    def event_monitor(self) -> dict | None:
        """event_monitor set based on event_monitor data-model."""
        if get(self._hostvars, "event_monitor") is True:
            return {"enabled": "true"}
        return None

    @cached_property
    def event_handlers(self) -> list | None:
        """event_handlers set based on event_handlers data-model."""
        return get(self._hostvars, "event_handlers")

    @cached_property
    def load_interval(self) -> dict | None:
        """load_interval set based on load_interval_default variable."""
        if (load_interval_default := get(self._hostvars, "load_interval_default")) is not None:
            return {"default": load_interval_default}
        return None

    @cached_property
    def queue_monitor_length(self) -> dict | None:
        """queue_monitor_length set based on queue_monitor_length data-model and platform_settings.feature_support.queue_monitor_length_notify fact."""
        if (queue_monitor_length := get(self._hostvars, "queue_monitor_length")) is None:
            return None

        # Remove notifying key if not supported by the platform settings.
        if not self.shared_utils.platform_settings_feature_support_queue_monitor_length_notify:
            queue_monitor_length.pop("notifying", None)

        return queue_monitor_length

    @cached_property
    def ip_name_servers(self) -> list | None:
        """ip_name_servers set based on name_servers data-model and mgmt_interface_vrf."""
        ip_name_servers = [
            {
                "ip_address": name_server,
                "vrf": self.shared_utils.mgmt_interface_vrf,
            }
            for name_server in get(self._hostvars, "name_servers", default=[])
        ]
        if ip_name_servers:
            return ip_name_servers

        return None

    @cached_property
    def redundancy(self) -> dict | None:
        """Redundancy set based on redundancy data-model."""
        if get(self._hostvars, "redundancy") is not None:
            return {"protocol": get(self._hostvars, "redundancy.protocol")}
        return None

    @cached_property
    def interface_defaults(self) -> dict | None:
        """interface_defaults set based on default_interface_mtu."""
        if self.shared_utils.default_interface_mtu is not None:
            return {
                "mtu": self.shared_utils.default_interface_mtu,
            }
        return None

    @cached_property
    def spanning_tree(self) -> dict | None:
        """spanning_tree set based on spanning_tree_root_super, spanning_tree_mode and spanning_tree_priority."""
        if not self.shared_utils.network_services_l2:
            return {"mode": "none"}

        spanning_tree_root_super = get(self.shared_utils.switch_data_combined, "spanning_tree_root_super")
        spanning_tree_mode = get(self.shared_utils.switch_data_combined, "spanning_tree_mode")
        if spanning_tree_root_super is not True and spanning_tree_mode is None:
            return None

        spanning_tree = {}
        if spanning_tree_root_super is True:
            spanning_tree["root_super"] = True

        if spanning_tree_mode is not None:
            spanning_tree["mode"] = spanning_tree_mode
            priority = get(self.shared_utils.switch_data_combined, "spanning_tree_priority", default=32768)
            # "rapid-pvst" is not included below. Per vlan spanning-tree priorities are set under network-services.
            if spanning_tree_mode == "mstp":
                spanning_tree["mst_instances"] = [{"id": "0", "priority": priority}]
            elif spanning_tree_mode == "rstp":
                spanning_tree["rstp_priority"] = priority

        return spanning_tree

    @cached_property
    def service_unsupported_transceiver(self) -> dict | None:
        """service_unsupported_transceiver based on unsupported_transceiver data-model."""
        if (unsupported_transceiver := get(self._hostvars, "unsupported_transceiver")) is not None:
            return {"license_name": unsupported_transceiver.get("license_name"), "license_key": unsupported_transceiver.get("license_key")}

        return None

    @cached_property
    def local_users(self) -> list | None:
        """local_users set based on local_users data model."""
        if (local_users := get(self._hostvars, "local_users")) is None:
            return None

        return natural_sort(local_users, "name")

    @cached_property
    def clock(self) -> dict | None:
        """Clock set based on timezone variable."""
        if (timezone := get(self._hostvars, "timezone")) is not None:
            return {"timezone": timezone}
        return None

    @cached_property
    def vrfs(self) -> list:
        """Vrfs set based on mgmt_interface_vrf variable."""
        mgmt_vrf_routing = get(self._hostvars, "mgmt_vrf_routing", default=False)
        vrf_settings = {
            "name": self.shared_utils.mgmt_interface_vrf,
            "ip_routing": mgmt_vrf_routing,
        }
        if self.shared_utils.ipv6_mgmt_ip is not None:
            vrf_settings["ipv6_routing"] = mgmt_vrf_routing
        return [vrf_settings]

    @cached_property
    def management_interfaces(self) -> list | None:
        """management_interfaces set based on mgmt_interface, mgmt_ip, ipv6_mgmt_ip facts, mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables."""
        mgmt_interface = self.shared_utils.mgmt_interface
        if (
            mgmt_interface is not None
            and self.shared_utils.mgmt_interface_vrf is not None
            and (self.shared_utils.mgmt_ip is not None or self.shared_utils.ipv6_mgmt_ip is not None)
        ):
            interface_settings = {
                "name": mgmt_interface,
                "description": get(self._hostvars, "mgmt_interface_description", default="OOB_MANAGEMENT"),
                "shutdown": False,
                "vrf": self.shared_utils.mgmt_interface_vrf,
                "ip_address": self.shared_utils.mgmt_ip,
                "gateway": self.shared_utils.mgmt_gateway,
                "type": "oob",
            }
            """
            inserting ipv6 variables if ipv6_mgmt_ip is set
            """
            if self.shared_utils.ipv6_mgmt_ip is not None:
                interface_settings.update(
                    {
                        "ipv6_enable": True,
                        "ipv6_address": self.shared_utils.ipv6_mgmt_ip,
                        "ipv6_gateway": self.shared_utils.ipv6_mgmt_gateway,
                    },
                )

            return [interface_settings]

        return None

    @cached_property
    def management_security(self) -> dict | None:
        """Return structured config for management_security."""
        if (entropy_sources := get(self.shared_utils.platform_settings, "security_entropy_sources")) is not None:
            return {"entropy_sources": entropy_sources}

        return None

    @cached_property
    def tcam_profile(self) -> dict | None:
        """tcam_profile set based on platform_settings.tcam_profile fact."""
        if (tcam_profile := get(self.shared_utils.platform_settings, "tcam_profile")) is not None:
            return {"system": tcam_profile}
        return None

    @cached_property
    def platform(self) -> dict | None:
        """
        platform set based on.

        * platform_settings.lag_hardware_only,
        * platform_settings.trident_forwarding_table_partition and switch.evpn_multicast facts
        * data_plane_cpu_allocation_max.
        """
        platform = {}
        if (lag_hardware_only := get(self.shared_utils.platform_settings, "lag_hardware_only")) is not None:
            platform["sand"] = {"lag": {"hardware_only": lag_hardware_only}}

        trident_forwarding_table_partition = get(self.shared_utils.platform_settings, "trident_forwarding_table_partition")
        if trident_forwarding_table_partition is not None and self.shared_utils.evpn_multicast:
            platform["trident"] = {"forwarding_table_partition": trident_forwarding_table_partition}

        if (cpu_max_allocation := get(self.shared_utils.switch_data_combined, "data_plane_cpu_allocation_max")) is not None:
            platform["sfe"] = {"data_plane_cpu_allocation_max": cpu_max_allocation}
        elif self.shared_utils.is_wan_server:
            # For AutoVPN Route Reflectors and Pathfinders, running on CloudEOS, setting
            # this value is required for the solution to work.
            msg = "For AutoVPN RRs and Pathfinders, 'data_plane_cpu_allocation_max' must be set"
            raise AristaAvdInvalidInputsError(msg)

        if platform:
            return platform
        return None

    @cached_property
    def mac_address_table(self) -> dict | None:
        """mac_address_table set based on mac_address_table data-model."""
        if (aging_time := get(self._hostvars, "mac_address_table.aging_time")) is not None:
            return {"aging_time": aging_time}
        return None

    @cached_property
    def queue_monitor_streaming(self) -> dict | None:
        """queue_monitor_streaming set based on queue_monitor_streaming data-model."""
        enable = get(self._hostvars, "queue_monitor_streaming.enable")
        vrf = get(self._hostvars, "queue_monitor_streaming.vrf")
        if enable is not True or vrf is None:
            # TODO: Fix bug where queue monitor enable without VRF will not return any config.
            return None

        queue_monitor = {}
        if enable is True:
            queue_monitor["enable"] = enable

        if vrf is not None:
            queue_monitor["vrf"] = vrf

        return queue_monitor

    @cached_property
    def management_api_http(self) -> dict | None:
        """management_api_http set based on management_eapi data-model."""
        if (management_eapi := get(self._hostvars, "management_eapi", default={"enable_https": True})) is None:
            return None

        management_api_http = {"enable_vrfs": [{"name": self.shared_utils.mgmt_interface_vrf}]}
        management_api = management_eapi.fromkeys(["enable_http", "enable_https", "default_services"])
        for key in dict(management_api):
            if (value := management_eapi.get(key)) is not None:
                management_api[key] = value
            else:
                del management_api[key]

        management_api_http.update(management_api)
        return management_api_http

    @cached_property
    def link_tracking_groups(self) -> list | None:
        """link_tracking_groups."""
        return self.shared_utils.link_tracking_groups

    @cached_property
    def lacp(self) -> dict | None:
        """Lacp set based on lacp_port_id_range."""
        lacp_port_id_range = get(self.shared_utils.switch_data_combined, "lacp_port_id_range", default={})
        if lacp_port_id_range.get("enabled") is not True:
            return None

        if (switch_id := self.shared_utils.id) is None:
            msg = f"'id' is not set on '{self.shared_utils.hostname}' to set LACP port ID ranges"
            raise AristaAvdInvalidInputsError(msg)

        node_group_length = max(len(self.shared_utils.switch_data_node_group_nodes), 1)
        port_range = int(get(lacp_port_id_range, "size", default=128))
        port_offset = int(get(lacp_port_id_range, "offset", default=0))

        begin = 1 + (((switch_id - 1) % node_group_length) * port_range) + port_offset
        end = (((switch_id - 1) % node_group_length + 1) * port_range) + port_offset

        return {
            "port_id": {
                "range": {
                    "begin": begin,
                    "end": end,
                },
            },
        }

    @cached_property
    def ptp(self) -> dict | None:
        """
        Generates PTP config on node level as well as for interfaces, using various defaults.

        - The following are set in default node_type_keys for design "l3ls-evpn":
                spine:
                  default_ptp_priority1: 20
                l3leaf:
                  default_ptp_priority1: 30
        PTP priority2 is set in the code below, calculated based on the node id:
            default_priority2 = self.id % 256.
        """
        if not self.shared_utils.ptp_enabled:
            return None
        default_ptp_domain = get(self._hostvars, "ptp_settings.domain", default=127)
        default_ptp_priority1 = get(self.shared_utils.node_type_key_data, "default_ptp_priority1", default=127)
        default_clock_identity = None

        priority1 = get(self.shared_utils.switch_data_combined, "ptp.priority1", default=default_ptp_priority1)
        priority2 = get(self.shared_utils.switch_data_combined, "ptp.priority2")
        if priority2 is None:
            if self.shared_utils.id is None:
                msg = f"'id' must be set on '{self.shared_utils.hostname}' to set ptp priority2"
                raise AristaAvdInvalidInputsError(msg)

            priority2 = self.shared_utils.id % 256
        default_auto_clock_identity = get(self._hostvars, "ptp_settings.auto_clock_identity", default=True)
        if get(self.shared_utils.switch_data_combined, "ptp.auto_clock_identity", default=default_auto_clock_identity) is True:
            clock_identity_prefix = get(self.shared_utils.switch_data_combined, "ptp.clock_identity_prefix", default="00:1C:73")
            default_clock_identity = f"{clock_identity_prefix}:{priority1:02x}:00:{priority2:02x}"

        ptp = {
            "mode": get(self.shared_utils.switch_data_combined, "ptp.mode", default="boundary"),
            "mode_one_step": get(self.shared_utils.switch_data_combined, "ptp.mode_one_step"),
            "forward_unicast": get(self.shared_utils.switch_data_combined, "ptp.forward_unicast"),
            "clock_identity": get(self.shared_utils.switch_data_combined, "ptp.clock_identity", default=default_clock_identity),
            "source": {"ip": get(self.shared_utils.switch_data_combined, "ptp.source_ip")},
            "priority1": priority1,
            "priority2": priority2,
            "ttl": get(self.shared_utils.switch_data_combined, "ptp.ttl"),
            "domain": get(self.shared_utils.switch_data_combined, "ptp.domain", default=default_ptp_domain),
            "message_type": {
                "general": {
                    "dscp": get(self.shared_utils.switch_data_combined, "ptp.dscp.general_messages"),
                },
                "event": {
                    "dscp": get(self.shared_utils.switch_data_combined, "ptp.dscp.event_messages"),
                },
            },
            "monitor": {
                "enabled": get(self.shared_utils.switch_data_combined, "ptp.monitor.enabled", default=True),
                "threshold": {
                    "offset_from_master": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.offset_from_master", default=250),
                    "mean_path_delay": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.mean_path_delay", default=1500),
                    "drop": {
                        "offset_from_master": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.drop.offset_from_master"),
                        "mean_path_delay": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.drop.mean_path_delay"),
                    },
                },
                "missing_message": {
                    "intervals": {
                        "announce": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.intervals.announce"),
                        "follow_up": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.intervals.follow_up"),
                        "sync": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.intervals.sync"),
                    },
                    "sequence_ids": {
                        "enabled": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.enabled", default=True),
                        "announce": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.announce", default=3),
                        "delay_resp": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.delay_resp", default=3),
                        "follow_up": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.follow_up", default=3),
                        "sync": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.sync", default=3),
                    },
                },
            },
        }
        return strip_null_from_data(ptp, (None, {}))

    @cached_property
    def eos_cli(self) -> str | None:
        """Aggregate the values of raw_eos_cli and platform_settings.platform_raw_eos_cli facts."""
        raw_eos_cli = get(self.shared_utils.switch_data_combined, "raw_eos_cli")
        platform_raw_eos_cli = get(self.shared_utils.platform_settings, "raw_eos_cli")
        if raw_eos_cli is not None or platform_raw_eos_cli is not None:
            return "\n".join(filter(None, [raw_eos_cli, platform_raw_eos_cli]))
        return None

    @cached_property
    def ip_radius_source_interfaces(self) -> list | None:
        """Parse source_interfaces.radius and return list of source_interfaces."""
        if (inputs := self._source_interfaces.get("radius")) is None:
            return None

        if source_interfaces := self._build_source_interfaces(inputs.get("mgmt_interface", False), inputs.get("inband_mgmt_interface", False), "IP Radius"):
            return source_interfaces

        return None

    @cached_property
    def ip_tacacs_source_interfaces(self) -> list | None:
        """Parse source_interfaces.tacacs and return list of source_interfaces."""
        if (inputs := self._source_interfaces.get("tacacs")) is None:
            return None

        if source_interfaces := self._build_source_interfaces(inputs.get("mgmt_interface", False), inputs.get("inband_mgmt_interface", False), "IP Tacacs"):
            return source_interfaces

        return None

    @cached_property
    def ip_ssh_client_source_interfaces(self) -> list | None:
        """Parse source_interfaces.ssh_client and return list of source_interfaces."""
        if (inputs := self._source_interfaces.get("ssh_client")) is None:
            return None

        if source_interfaces := self._build_source_interfaces(inputs.get("mgmt_interface", False), inputs.get("inband_mgmt_interface", False), "IP SSH Client"):
            return source_interfaces

        return None

    @cached_property
    def ip_domain_lookup(self) -> dict | None:
        """Parse source_interfaces.domain_lookup and return dict with nested source_interfaces list."""
        if (inputs := self._source_interfaces.get("domain_lookup")) is None:
            return None

        if source_interfaces := self._build_source_interfaces(
            inputs.get("mgmt_interface", False),
            inputs.get("inband_mgmt_interface", False),
            "IP Domain Lookup",
        ):
            return {"source_interfaces": source_interfaces}

        return None

    @cached_property
    def ip_http_client_source_interfaces(self) -> list | None:
        """Parse source_interfaces.http_client and return list of source_interfaces."""
        if (inputs := self._source_interfaces.get("http_client")) is None:
            return None

        if source_interfaces := self._build_source_interfaces(
            inputs.get("mgmt_interface", False),
            inputs.get("inband_mgmt_interface", False),
            "IP HTTP Client",
        ):
            return source_interfaces

        return None

    @cached_property
    def prefix_lists(self) -> list | None:
        prefix_lists = []
        prefix_lists_in_use = set()
        for neighbor in self.shared_utils.l3_interfaces_bgp_neighbors:
            if (prefix_list_in := get(neighbor, "ipv4_prefix_list_in")) and prefix_list_in not in prefix_lists_in_use:
                pfx_list = self._get_prefix_list(prefix_list_in)
                prefix_lists.append(pfx_list)
                prefix_lists_in_use.add(prefix_list_in)

            if (prefix_list_out := get(neighbor, "ipv4_prefix_list_out")) and prefix_list_out not in prefix_lists_in_use:
                pfx_list = self._get_prefix_list(prefix_list_out)
                prefix_lists.append(pfx_list)
                prefix_lists_in_use.add(prefix_list_out)

        return prefix_lists or None

    def _get_prefix_list(self, name: str) -> dict:
        return get_item(self.shared_utils.ipv4_prefix_list_catalog, "name", name, required=True, var_name=f"ipv4_prefix_list_catalog[name={name}]")

    @cached_property
    def route_maps(self) -> list | None:
        route_maps = []
        for neighbor in self.shared_utils.l3_interfaces_bgp_neighbors:
            # RM-BGP-<PEER-IP>-IN
            if prefix_list_in := get(neighbor, "ipv4_prefix_list_in"):
                sequence_numbers = [
                    {
                        "sequence": 10,
                        "type": "permit",
                        "match": [f"ip address prefix-list {prefix_list_in}"],
                    },
                ]
                # set no advertise is set only for WAN neighbors, which will also have prefix_list_in
                if neighbor.get("set_no_advertise"):
                    sequence_numbers[0]["set"] = ["community no-advertise additive"]

                route_maps.append({"name": neighbor["route_map_in"], "sequence_numbers": sequence_numbers})

            # RM-BGP-<PEER-IP>-OUT
            if prefix_list_out := get(neighbor, "ipv4_prefix_list_out"):
                sequence_numbers = [
                    {
                        "sequence": 10,
                        "type": "permit",
                        "match": [f"ip address prefix-list {prefix_list_out}"],
                    },
                    {
                        "sequence": 20,
                        "type": "deny",
                    },
                ]
            else:
                sequence_numbers = [
                    {
                        "sequence": 10,
                        "type": "deny",
                    },
                ]

            route_maps.append({"name": neighbor["route_map_out"], "sequence_numbers": sequence_numbers})

        return route_maps or None

    @cached_property
    def struct_cfgs(self) -> list | None:
        if (struct_cfg := get(self.shared_utils.platform_settings, "structured_config")) is not None:
            return [struct_cfg]

        return None
