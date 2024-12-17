# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_designs.avdfacts import AvdFacts
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default, get, strip_empties_from_dict, strip_null_from_data
from pyavd.j2filters import natural_sort

from .ntp import NtpMixin
from .router_general import RouterGeneralMixin
from .snmp_server import SnmpServerMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns


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
        return self.inputs.is_deployed

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

        platform_bgp_update_wait_for_convergence = self.shared_utils.platform_settings.feature_support.bgp_update_wait_for_convergence
        platform_bgp_update_wait_install = self.shared_utils.platform_settings.feature_support.bgp_update_wait_install

        if self.shared_utils.is_wan_router:
            # Special defaults for WAN routers
            default_maximum_paths = 16
            default_ecmp = None
        else:
            default_maximum_paths = 4
            default_ecmp = 4

        router_bgp = {
            "as": self.shared_utils.bgp_as,
            "router_id": self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None,
            "distance": self.inputs.bgp_distance._as_dict() or None,
            "bgp_defaults": self.shared_utils.node_config.bgp_defaults._as_list() or None,
            "bgp": {
                "default": {
                    "ipv4_unicast": self.inputs.bgp_default_ipv4_unicast,
                },
            },
            "maximum_paths": {
                "paths": self.inputs.bgp_maximum_paths or default_maximum_paths,
                "ecmp": self.inputs.bgp_ecmp or default_ecmp,
            },
            "redistribute": self._router_bgp_redistribute_routes,
        }

        if self.inputs.bgp_update_wait_for_convergence and platform_bgp_update_wait_for_convergence:
            router_bgp.setdefault("updates", {})["wait_for_convergence"] = True

        if self.inputs.bgp_update_wait_install and platform_bgp_update_wait_install:
            router_bgp.setdefault("updates", {})["wait_install"] = True

        if self.inputs.bgp_graceful_restart.enabled:
            router_bgp.update(
                {
                    "graceful_restart": {
                        "enabled": True,
                        "restart_time": self.inputs.bgp_graceful_restart.restart_time,
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
                "rcf_in": get(neighbor_info, "rcf_in"),
                "rcf_out": get(neighbor_info, "rcf_out"),
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

        if self.inputs.mgmt_destination_networks:
            return [
                {
                    "vrf": self.inputs.mgmt_interface_vrf,
                    "destination_address_prefix": mgmt_destination_network,
                    "gateway": self.shared_utils.mgmt_gateway,
                }
                for mgmt_destination_network in self.inputs.mgmt_destination_networks
            ]

        return [
            {
                "vrf": self.inputs.mgmt_interface_vrf,
                "destination_address_prefix": "0.0.0.0/0",
                "gateway": self.shared_utils.mgmt_gateway,
            }
        ]

    @cached_property
    def ipv6_static_routes(self) -> list | None:
        """ipv6_static_routes set based on ipv6_mgmt_gateway, ipv6_mgmt_destination_networks and mgmt_interface_vrf."""
        if self.shared_utils.ipv6_mgmt_gateway is None or self.shared_utils.node_config.ipv6_mgmt_ip is None:
            return None

        if self.inputs.ipv6_mgmt_destination_networks:
            return [
                {
                    "vrf": self.inputs.mgmt_interface_vrf,
                    "destination_address_prefix": mgmt_destination_network,
                    "gateway": self.shared_utils.ipv6_mgmt_gateway,
                }
                for mgmt_destination_network in self.inputs.ipv6_mgmt_destination_networks
            ]

        return [
            {
                "vrf": self.inputs.mgmt_interface_vrf,
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
        if not self.shared_utils.underlay_router and not self.shared_utils.node_config.always_configure_ip_routing:
            return None

        if self.ip_routing_ipv6_interfaces is True:
            return None
        return True

    @cached_property
    def ipv6_unicast_routing(self) -> bool | None:
        """ipv6_unicast_routing set based on underlay_rfc5549 and underlay_ipv6."""
        if not self.shared_utils.underlay_router and not self.shared_utils.node_config.always_configure_ip_routing:
            return None

        if self.inputs.underlay_rfc5549 or self.shared_utils.underlay_ipv6:
            return True
        return None

    @cached_property
    def ip_routing_ipv6_interfaces(self) -> bool | None:
        """ip_routing_ipv6_interfaces set based on underlay_rfc5549 variable."""
        if not self.shared_utils.underlay_router and not self.shared_utils.node_config.always_configure_ip_routing:
            return None

        if self.inputs.underlay_rfc5549:
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
        return self.inputs.hardware_counters._as_dict() or None

    @cached_property
    def hardware(self) -> dict | None:
        """
        hardware set based on platform_speed_groups variable and switch.platform fact.

        Converting nested dict to list of dict to support avd_v4.0.
        """
        platform_speed_groups = self.inputs.platform_speed_groups
        switch_platform = self.shared_utils.platform
        if not platform_speed_groups or switch_platform is None:
            return None

        if switch_platform not in platform_speed_groups:
            return None

        tmp_speed_groups = {}
        for speed in platform_speed_groups[switch_platform].speeds._natural_sorted():
            for speed_group in speed.speed_groups:
                tmp_speed_groups[speed_group] = speed.speed

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
        cvp_instance_ip_list = self.inputs.cvp_instance_ips
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
                    "token_file": self.inputs.cvp_token_file or "/tmp/cv-onboarding-token",  # NOSONAR # noqa: S108
                }
            else:
                # updating for cvp_on_prem_ips
                cv_address = f"{cvp_instance_ip}:{self.inputs.terminattr_ingestgrpcurl_port}"
                daemon_terminattr["cvaddrs"].append(cv_address)
                if (cvp_ingestauth_key := self.inputs.cvp_ingestauth_key) is not None:
                    daemon_terminattr["cvauth"] = {
                        "method": "key",
                        "key": cvp_ingestauth_key,
                    }
                else:
                    daemon_terminattr["cvauth"] = {
                        "method": "token",
                        # Ignoring sonar-lint false positive for tmp path since this is config for EOS
                        "token_file": self.inputs.cvp_token_file or "/tmp/token",  # NOSONAR # noqa: S108
                    }

        daemon_terminattr["cvvrf"] = self.inputs.mgmt_interface_vrf
        daemon_terminattr["smashexcludes"] = self.inputs.terminattr_smashexcludes
        daemon_terminattr["ingestexclude"] = self.inputs.terminattr_ingestexclude
        daemon_terminattr["disable_aaa"] = self.inputs.terminattr_disable_aaa

        return daemon_terminattr

    @cached_property
    def vlan_internal_order(self) -> dict | None:
        """vlan_internal_order set based on internal_vlan_order data-model."""
        if self.shared_utils.wan_role:
            return None

        return self.inputs.internal_vlan_order._as_dict()

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
        """event_monitor set based on event_monitor data-model. TODO: add to schema."""
        if get(self._hostvars, "event_monitor") is True:
            return {"enabled": "true"}
        return None

    @cached_property
    def event_handlers(self) -> list | None:
        """event_handlers set based on event_handlers data-model."""
        return self.inputs.event_handlers._as_list() or None

    @cached_property
    def load_interval(self) -> dict | None:
        """load_interval set based on load_interval_default variable. TODO: add to schema."""
        if (load_interval_default := get(self._hostvars, "load_interval_default")) is not None:
            return {"default": load_interval_default}
        return None

    @cached_property
    def queue_monitor_length(self) -> dict | None:
        """queue_monitor_length set based on queue_monitor_length data-model and platform_settings.feature_support.queue_monitor_length_notify fact."""
        if not self.inputs.queue_monitor_length:
            return None

        # Remove notifying key if not supported by the platform settings.
        queue_monitor_length = self.inputs.queue_monitor_length._as_dict()
        if not self.shared_utils.platform_settings.feature_support.queue_monitor_length_notify:
            queue_monitor_length.pop("notifying", None)

        return queue_monitor_length

    @cached_property
    def ip_name_servers(self) -> list | None:
        """ip_name_servers set based on name_servers data-model and mgmt_interface_vrf."""
        ip_name_servers = [
            {
                "ip_address": name_server,
                "vrf": self.inputs.mgmt_interface_vrf,
            }
            for name_server in self.inputs.name_servers
        ]

        return ip_name_servers or None

    @cached_property
    def redundancy(self) -> dict | None:
        """Redundancy set based on redundancy data-model."""
        if self.inputs.redundancy.protocol:
            return {"protocol": self.inputs.redundancy.protocol}
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

        spanning_tree_root_super = self.shared_utils.node_config.spanning_tree_root_super
        spanning_tree_mode = self.shared_utils.node_config.spanning_tree_mode
        if spanning_tree_root_super is not True and spanning_tree_mode is None:
            return None

        spanning_tree = {}
        if spanning_tree_root_super is True:
            spanning_tree["root_super"] = True

        if spanning_tree_mode is not None:
            spanning_tree["mode"] = spanning_tree_mode
            priority = self.shared_utils.node_config.spanning_tree_priority
            # "rapid-pvst" is not included below. Per vlan spanning-tree priorities are set under network-services.
            if spanning_tree_mode == "mstp":
                spanning_tree["mst_instances"] = [{"id": "0", "priority": priority}]
            elif spanning_tree_mode == "rstp":
                spanning_tree["rstp_priority"] = priority

        return spanning_tree

    @cached_property
    def service_unsupported_transceiver(self) -> dict | None:
        """service_unsupported_transceiver based on unsupported_transceiver data-model. TODO: Add to schema - maybe as hidden."""
        if (unsupported_transceiver := get(self._hostvars, "unsupported_transceiver")) is not None:
            return {"license_name": unsupported_transceiver.get("license_name"), "license_key": unsupported_transceiver.get("license_key")}

        return None

    @cached_property
    def local_users(self) -> list | None:
        """local_users set based on local_users data model."""
        if not self.inputs.local_users:
            return None

        return [user._as_dict() for user in self.inputs.local_users._natural_sorted()]

    @cached_property
    def clock(self) -> dict | None:
        """Clock set based on timezone variable."""
        if self.inputs.timezone:
            return {"timezone": self.inputs.timezone}
        return None

    @cached_property
    def vrfs(self) -> list:
        """Vrfs set based on mgmt_interface_vrf variable."""
        vrf_settings = {
            "name": self.inputs.mgmt_interface_vrf,
            "ip_routing": self.inputs.mgmt_vrf_routing,
        }
        if self.shared_utils.node_config.ipv6_mgmt_ip is not None:
            vrf_settings["ipv6_routing"] = self.inputs.mgmt_vrf_routing
        return [vrf_settings]

    @cached_property
    def management_interfaces(self) -> list | None:
        """management_interfaces set based on mgmt_interface, mgmt_ip, ipv6_mgmt_ip facts, mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables."""
        if self.shared_utils.node_config.mgmt_ip or self.shared_utils.node_config.ipv6_mgmt_ip:
            interface_settings = {
                "name": self.shared_utils.mgmt_interface,
                "description": self.inputs.mgmt_interface_description,
                "shutdown": False,
                "vrf": self.inputs.mgmt_interface_vrf,
                "ip_address": self.shared_utils.node_config.mgmt_ip,
                "gateway": self.shared_utils.mgmt_gateway,
                "type": "oob",
            }
            """
            inserting ipv6 variables if ipv6_mgmt_ip is set
            """
            if self.shared_utils.node_config.ipv6_mgmt_ip:
                interface_settings.update(
                    {
                        "ipv6_enable": True,
                        "ipv6_address": self.shared_utils.node_config.ipv6_mgmt_ip,
                        "ipv6_gateway": self.shared_utils.ipv6_mgmt_gateway,
                    },
                )

            return [strip_empties_from_dict(interface_settings)]

        return None

    @cached_property
    def management_security(self) -> dict | None:
        """Return structured config for management_security."""
        if entropy_sources := self.shared_utils.platform_settings.security_entropy_sources:
            return {"entropy_sources": entropy_sources._as_dict(include_default_values=True)}

        return None

    @cached_property
    def tcam_profile(self) -> dict | None:
        """tcam_profile set based on platform_settings.tcam_profile fact."""
        if tcam_profile := self.shared_utils.platform_settings.tcam_profile:
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
        if (lag_hardware_only := self.shared_utils.platform_settings.lag_hardware_only) is not None:
            platform["sand"] = {"lag": {"hardware_only": lag_hardware_only}}

        trident_forwarding_table_partition = self.shared_utils.platform_settings.trident_forwarding_table_partition
        if trident_forwarding_table_partition and self.shared_utils.evpn_multicast:
            platform["trident"] = {"forwarding_table_partition": trident_forwarding_table_partition}

        if (cpu_max_allocation := self.shared_utils.node_config.data_plane_cpu_allocation_max) is not None:
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
        if self.inputs.mac_address_table.aging_time is not None:
            return {"aging_time": self.inputs.mac_address_table.aging_time}
        return None

    @cached_property
    def queue_monitor_streaming(self) -> dict | None:
        """queue_monitor_streaming set based on queue_monitor_streaming data-model. TODO: Add to schema."""
        enable = get(self._hostvars, "queue_monitor_streaming.enable")
        vrf = get(self._hostvars, "queue_monitor_streaming.vrf")
        if enable is not True or vrf is None:
            # TODO: Fix bug where queue monitor enable without VRF will not return any config.
            return None

        queue_monitor = {}
        if enable is True:
            queue_monitor["enable"] = enable

        queue_monitor["vrf"] = vrf

        return queue_monitor

    @cached_property
    def management_api_http(self) -> dict:
        """management_api_http set based on management_eapi data-model."""
        return strip_empties_from_dict(
            {
                "enable_vrfs": [{"name": self.inputs.mgmt_interface_vrf}],
                "enable_http": self.inputs.management_eapi.enable_http or None,
                "enable_https": self.inputs.management_eapi.enable_https or None,
                "default_services": self.inputs.management_eapi.default_services,
            }
        )

    @cached_property
    def link_tracking_groups(self) -> list | None:
        """link_tracking_groups."""
        return self.shared_utils.link_tracking_groups

    @cached_property
    def lacp(self) -> dict | None:
        """Lacp set based on lacp_port_id_range."""
        lacp_port_id_range = self.shared_utils.node_config.lacp_port_id_range
        if not lacp_port_id_range.enabled:
            return None

        if (switch_id := self.shared_utils.id) is None:
            msg = f"'id' is not set on '{self.shared_utils.hostname}' to set LACP port ID ranges"
            raise AristaAvdInvalidInputsError(msg)

        node_group_length = max(len(self.shared_utils.node_group_config.nodes), 1) if self.shared_utils.node_group_config is not None else 1

        begin = 1 + (((switch_id - 1) % node_group_length) * lacp_port_id_range.size) + lacp_port_id_range.offset
        end = (((switch_id - 1) % node_group_length + 1) * lacp_port_id_range.size) + lacp_port_id_range.offset

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
        default_ptp_domain = self.inputs.ptp_settings.domain
        default_ptp_priority1 = self.shared_utils.node_type_key_data.default_ptp_priority1
        default_clock_identity = None

        priority1 = default(self.shared_utils.node_config.ptp.priority1, default_ptp_priority1)
        priority2 = self.shared_utils.node_config.ptp.priority2
        if priority2 is None:
            if self.shared_utils.id is None:
                msg = f"'id' must be set on '{self.shared_utils.hostname}' to set ptp priority2"
                raise AristaAvdInvalidInputsError(msg)

            priority2 = self.shared_utils.id % 256
        if default(self.shared_utils.node_config.ptp.auto_clock_identity, self.inputs.ptp_settings.auto_clock_identity):
            clock_identity_prefix = self.shared_utils.node_config.ptp.clock_identity_prefix
            default_clock_identity = f"{clock_identity_prefix}:{priority1:02x}:00:{priority2:02x}"

        ptp = {
            "mode": self.shared_utils.node_config.ptp.mode,
            "mode_one_step": self.shared_utils.node_config.ptp.mode_one_step or None,  # Historic output is without false
            "forward_unicast": self.shared_utils.node_config.ptp.forward_unicast or None,  # Historic output is without false
            "clock_identity": default(self.shared_utils.node_config.ptp.clock_identity, default_clock_identity),
            "source": {"ip": self.shared_utils.node_config.ptp.source_ip},
            "priority1": priority1,
            "priority2": priority2,
            "ttl": self.shared_utils.node_config.ptp.ttl,
            "domain": default(self.shared_utils.node_config.ptp.domain, default_ptp_domain),
            "message_type": {
                "general": {
                    "dscp": self.shared_utils.node_config.ptp.dscp.general_messages,
                },
                "event": {
                    "dscp": self.shared_utils.node_config.ptp.dscp.event_messages,
                },
            },
            "monitor": self.shared_utils.node_config.ptp.monitor._as_dict(include_default_values=True),
        }
        return strip_null_from_data(ptp, (None, {}))

    @cached_property
    def eos_cli(self) -> str | None:
        """Aggregate the values of raw_eos_cli and platform_settings.platform_raw_eos_cli facts."""
        return "\n".join(filter(None, [self.shared_utils.node_config.raw_eos_cli, self.shared_utils.platform_settings.raw_eos_cli])) or None

    @cached_property
    def ip_radius_source_interfaces(self) -> list | None:
        """Parse source_interfaces.radius and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.radius):
            return None

        if source_interfaces := self._build_source_interfaces(inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP Radius"):
            return source_interfaces

        return None

    @cached_property
    def ip_tacacs_source_interfaces(self) -> list | None:
        """Parse source_interfaces.tacacs and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.tacacs):
            return None

        if source_interfaces := self._build_source_interfaces(inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP Tacacs"):
            return source_interfaces

        return None

    @cached_property
    def ip_ssh_client_source_interfaces(self) -> list | None:
        """Parse source_interfaces.ssh_client and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.ssh_client):
            return None

        if source_interfaces := self._build_source_interfaces(inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP SSH Client"):
            return source_interfaces

        return None

    @cached_property
    def ip_domain_lookup(self) -> dict | None:
        """Parse source_interfaces.domain_lookup and return dict with nested source_interfaces list."""
        if not (inputs := self.inputs.source_interfaces.domain_lookup):
            return None

        if source_interfaces := self._build_source_interfaces(inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP Domain Lookup"):
            return {"source_interfaces": source_interfaces}

        return None

    @cached_property
    def ip_http_client_source_interfaces(self) -> list | None:
        """Parse source_interfaces.http_client and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.http_client):
            return None

        if source_interfaces := self._build_source_interfaces(inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP HTTP Client"):
            return source_interfaces

        return None

    @cached_property
    def prefix_lists(self) -> list | None:
        prefix_lists = []
        prefix_lists_in_use = set()
        for neighbor in self.shared_utils.l3_interfaces_bgp_neighbors:
            if (prefix_list_in := get(neighbor, "ipv4_prefix_list_in")) and prefix_list_in not in prefix_lists_in_use:
                pfx_list = self._get_prefix_list(prefix_list_in)._as_dict()
                prefix_lists.append(pfx_list)
                prefix_lists_in_use.add(prefix_list_in)

            if (prefix_list_out := get(neighbor, "ipv4_prefix_list_out")) and prefix_list_out not in prefix_lists_in_use:
                pfx_list = self._get_prefix_list(prefix_list_out)._as_dict()
                prefix_lists.append(pfx_list)
                prefix_lists_in_use.add(prefix_list_out)

        return prefix_lists or None

    def _get_prefix_list(self, name: str) -> EosDesigns.Ipv4PrefixListCatalogItem:
        if name not in self.inputs.ipv4_prefix_list_catalog:
            msg = f"ipv4_prefix_list_catalog[name={name}]"
            raise AristaAvdMissingVariableError(msg)
        return self.inputs.ipv4_prefix_list_catalog[name]

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
        if self.shared_utils.platform_settings.structured_config:
            return [self.shared_utils.platform_settings.structured_config._as_dict()]

        return None
