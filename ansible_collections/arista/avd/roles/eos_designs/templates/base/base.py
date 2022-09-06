from ansible_collections.arista.avd.plugins.module_utils.eos_designs import AvdFacts
from functools import cached_property
from ansible_collections.arista.avd.plugins.module_utils.utils import get
from ansible_collections.arista.avd.plugins.filter.snmp_hash import hash_passphrase
from hashlib import sha1


class AVDStructConfig(AvdFacts):

    @cached_property
    def _mgmt_interface_vrf(self):
        return get(self._hostvars, 'mgmt_interface_vrf')

    @cached_property
    def _mgmt_gateway(self):
        return get(self._hostvars, 'mgmt_gateway')

    @cached_property
    def _switch(self):
        return get(self._hostvars, 'switch', required=True)

    @cached_property
    def _internal_vlan_order(self):
        return get(self._hostvars, 'internal_vlan_order')

    @cached_property
    def _platform_settings(self):
        return get(self._switch, 'platform_settings')

    @cached_property
    def _mgmt_ip(self):
        return get(self._switch, 'mgmt_ip')

    @cached_property
    def _hostname(self):
        """
        hostname variable set based on switch.hostname fact
        """
        return get(self._switch, "hostname", required=True)

    @cached_property
    def router_bgp(self):
        if (bgp_as := get(self._switch, "bgp_as")) is None:
            return None

        bgp_defaults = get(self._switch, 'bgp_defaults')
        if (bgp_maximum_paths := get(self._hostvars, 'bgp_maximum_paths')) is not None:
            max_paths_str = f"maximum-paths {bgp_maximum_paths}"
            if (bgp_ecmp := get(self._hostvars, 'bgp_ecmp')) is not None:
                max_paths_str += f" ecmp {bgp_ecmp}"
            bgp_defaults.append(max_paths_str)
        return {
            'as': bgp_as,
            'router_id': get(self._switch, 'router_id'),
            'bgp_defaults': bgp_defaults,
        }

    @cached_property
    def static_routes(self):
        if self._mgmt_gateway is None:
            return None

        static_routes = []
        if (mgmt_destination_networks := get(self._hostvars, 'mgmt_destination_networks')) is not None:
            for mgmt_destination_network in mgmt_destination_networks:
                static_routes.append({
                    'vrf': self._mgmt_interface_vrf,
                    'destination_address_prefix': mgmt_destination_network,
                    'gateway': self._mgmt_gateway,
                })
        else:
            static_routes.append({
                'vrf': self._mgmt_interface_vrf,
                'destination_address_prefix': '0.0.0.0/0',
                'gateway': self._mgmt_gateway,
            })
        return static_routes

    @cached_property
    def service_routing_protocols_model(self):
        return 'multi-agent'

    @cached_property
    def ip_routing(self):
        return True

    @cached_property
    def ipv6_unicast_routing(self):
        if (
                get(self._hostvars, 'underlay_rfc5549') is not True and
                get(self._switch, 'underlay_ipv6') is not True
        ):
            return None
        return True

    @cached_property
    def ip_routing_ipv6_interfaces(self):
        if get(self._hostvars, 'underlay_rfc5549') is not True:
            return None
        return True

    @cached_property
    def router_multicast(self):
        if (
                get(self._switch, 'underlay_multicast') is not True or
                get(self._switch, 'underlay_router') is not True
        ):
            return None
        router_multicast = {
            'ipv4': {
                'routing': True
            }
        }
        if get(self._switch, 'evpn_multicast') is True:
            router_multicast['ipv4']['software_forwarding'] = 'sfe'
        return router_multicast

    @cached_property
    def hardware_counters(self):
        if (hardware_counter_features := get(self._hostvars, 'hardware_counters.features')) is None:
            return None
        features = [{feature: direction} for feature, direction in hardware_counter_features.items()]
        return {"features": features}

    @cached_property
    def hardware(self):
        if (platform_speed_groups := get(self._hostvars, 'platform_speed_groups')) is None:
            return None

        tmp_speed_groups = {}
        if (switch_platform := get(self._switch, 'platform')) is not None:
            platform_speed_groups = self._convert_dicts(platform_speed_groups, 'platform', 'speeds')
            for platform_item in platform_speed_groups:
                if platform_item['platform'] == switch_platform:
                    speeds = self._convert_dicts(platform_item.get('speeds'), 'speed', 'speed_groups')
                    for speed in self._natural_sort(speeds, 'speed'):
                        for speed_group in speed['speed_groups']:
                            tmp_speed_groups[speed_group] = speed['speed']
        if tmp_speed_groups:
            hardware = {'speed_groups': {}}
            for speed_group in self._natural_sort(tmp_speed_groups):
                hardware['speed_groups'][speed_group] = {'serdes': tmp_speed_groups[speed_group]}
            return hardware

    @cached_property
    def daemon_terminattr(self):
        cvp_instance_ip = get(self._hostvars, 'cvp_instance_ip')
        cvp_instance_ips = get(self._hostvars, 'cvp_instance_ips')
        if cvp_instance_ip is None and cvp_instance_ips is None:
            return None
        cvp_instance_ip_list = []
        if cvp_instance_ip is not None:
            cvp_instance_ip_list.append(cvp_instance_ip)
        elif cvp_instance_ips is not None:
            for cvp_ip in cvp_instance_ips:
                cvp_instance_ip_list.append(cvp_ip)

        if cvp_instance_ip_list:
            daemon_terminattr = {'cvaddrs': []}
            for cvp_instance_ip in cvp_instance_ip_list:
                if "arista.io" in cvp_instance_ip:
                    # updating for cvaas_ips
                    daemon_terminattr['cvaddrs'].append(f"{cvp_instance_ip}:443")
                    daemon_terminattr['cvauth'] = {
                        'method': 'token-secure',
                        'token_file': get(self._hostvars, 'cvp_token_file', '/tmp/cv-onboarding-token'),
                    }
                else:
                    # updating for cvp_on_prem_ips
                    cv_address = f"{cvp_instance_ip}:{get(self._hostvars, 'terminattr_ingestgrpcurl_port')}"
                    daemon_terminattr['cvaddrs'].append(cv_address)
                    daemon_terminattr['cvauth'] = {
                        'method': 'key',
                        'key': get(self._hostvars, 'cvp_ingestauth_key'),
                    }
        daemon_terminattr['cvvrf'] = self._mgmt_interface_vrf
        daemon_terminattr['smashexcludes'] = get(self._hostvars, 'terminattr_smashexcludes')
        daemon_terminattr['ingestexclude'] = get(self._hostvars, 'terminattr_ingestexclude')
        daemon_terminattr['disable_aaa'] = get(self._hostvars, 'terminattr_disable_aaa', False)
        return daemon_terminattr

    @cached_property
    def vlan_internal_order(self):
        return {
            'allocation': get(self._internal_vlan_order, 'allocation'),
            'range': {
                'beginning': get(self._internal_vlan_order, 'range.beginning'),
                'ending': get(self._internal_vlan_order, 'range.ending')
            }
        }

    @cached_property
    def event_monitor(self):
        if get(self._hostvars, 'event_monitor') is not True:
            return None
        return {'enabled': 'true'}

    @cached_property
    def event_handlers(self):
        if (event_handlers := get(self._hostvars, 'event_handlers')) is None:
            return None
        event_handlers = self._convert_dicts(event_handlers, 'name')
        event_handler = {}
        for handler in event_handlers:
            handler_name = get(handler, 'name')
            event_handler[handler_name] = {}
            action = handler.get('action')
            action_type = handler.get('action_type')
            if action is not None and action_type is not None:
                event_handler[handler_name]['action_type'] = action_type
                event_handler[handler_name]['action'] = action
            if (delay := handler.get('delay')) is not None:
                event_handler[handler_name]['delay'] = delay
            if get(handler, 'asynchronous') is True:
                event_handler[handler_name]['asynchronous'] = 'handler.asynchronous'
            if (trigger := handler.get('trigger')) is not None:
                event_handler[handler_name]['trigger'] = trigger
            if (regex := handler.get('regex')) is not None:
                event_handler[handler_name]['regex'] = regex
        return event_handler

    @cached_property
    def load_interval(self):
        if (load_interval_default := get(self._hostvars, 'load_interval_default')) is None:
            return None
        return {'default': load_interval_default}

    @cached_property
    def queue_monitor_length(self):
        if (queue_monitor_length := get(self._hostvars, 'queue_monitor_length')) is None:
            return None

        queue_monitor_length_dict = {'enabled': True}
        queue_monitor_length_notifying = get(queue_monitor_length, 'notifying')
        notify_supported = get(self._platform_settings, "feature_support.queue_monitor_length_notify")
        if (
                queue_monitor_length_notifying is not None and
                notify_supported is not False
        ):
            queue_monitor_length_dict['notifying'] = queue_monitor_length_notifying
        if get(queue_monitor_length, 'log') is not None:
            queue_monitor_length_dict['log'] = queue_monitor_length.get('log')
        return queue_monitor_length_dict

    @cached_property
    def name_server(self):
        if (name_servers := get(self._hostvars, 'name_servers')) is None:
            return None
        return {
            'source':
                {
                    'vrf': self._mgmt_interface_vrf
                },
            'nodes': name_servers
        }

    @cached_property
    def redundancy(self):
        if get(self._hostvars, 'redundancy') is None:
            return None
        return {'protocol': get(self._hostvars, 'redundancy.protocol')}

    @cached_property
    def snmp_server(self):
        if (snmp_settings := get(self._hostvars, 'snmp_settings')) is None:
            return None
        snmp_server = {}

        if (compute_local_engineid := snmp_settings.get('compute_local_engineid')) is True:
            local_engine_id = sha1(f"{self._hostname}{self._mgmt_ip}".encode('utf-8')).hexdigest()
            snmp_server['engineid'] = {'local': local_engine_id}
        if (contact := snmp_settings.get('contact')) is not None:
            snmp_server['contact'] = contact
        if snmp_settings.get('location') is not None:
            location_elements = [get(self._hostvars, 'fabric_name'),
                                 get(self._hostvars, 'dc_name'),
                                 get(self._hostvars, 'pod_name'),
                                 get(self._switch, 'rack'),
                                 self._hostname]
            location_elements = [location for location in location_elements if location is not None]
            snmp_location = " ".join(location_elements)
            snmp_server['location'] = snmp_location
        users = snmp_settings.get('users')
        if users is not None:
            snmp_server['users']: []
            for user in users:
                version = get(user, 'version')
                user_dict = {
                    'name': get(user, 'name'),
                    'group': get(user, 'group'),
                    'version': version
                }
                compute_v3_user_localized_key = snmp_settings.get('compute_v3_user_localized_key')

                if version == 'v3':
                    if (
                            compute_local_engineid is True and
                            compute_v3_user_localized_key is True
                    ):
                        user_dict['localized'] = local_engine_id
                        auth = user.get('auth')
                        auth_passphrase = user.get('auth_passphrase')
                        if (
                                auth is not None and
                                auth_passphrase is not None
                        ):
                            user_dict['auth'] = auth
                            hash_filter = {"passphrase": auth_passphrase, "auth": auth, "engine_id": local_engine_id}
                            user_dict['auth_passphrase'] = hash_passphrase(hash_filter)

                            priv = user.get('priv')
                            priv_passphrase = user.get('priv_passphrase')
                            if (
                                    priv is not None and
                                    priv_passphrase is not None
                            ):
                                user_dict['priv'] = priv
                                hash_filter["passphrase"] = priv_passphrase,
                                hash_filter["priv"] = priv
                                user_dict['priv_passphrase'] = hash_passphrase(hash_filter)
                    else:
                        auth = user.get('auth')
                        auth_passphrase = user.get('auth_passphrase')
                        if (
                                auth is not None and
                                auth_passphrase is not None
                        ):
                            user_dict['auth'] = auth
                            user_dict['auth_passphrase'] = auth_passphrase
                            priv = user.get('priv')
                            priv_passphrase = user.get('priv_passphrase')
                            if (
                                    priv is not None and
                                    priv_passphrase is not None
                            ):
                                user_dict['priv'] = priv
                                user_dict['priv_passphrase'] = priv_passphrase
                snmp_server['users'].append(user_dict)
        return snmp_server

    @cached_property
    def spanning_tree(self):
        spanning_tree_root_super = get(self._switch, 'spanning_tree_root_super')
        spanning_tree_mode = get(self._switch, 'spanning_tree_mode')
        if spanning_tree_root_super is False and spanning_tree_mode is None:
            return None
        spanning_tree = {}
        if spanning_tree_root_super is True:
            spanning_tree['root_super'] = True
        if spanning_tree_mode is not None:
            spanning_tree['mode'] = spanning_tree_mode
            priority = get(self._switch, 'spanning_tree_priority', '32768')
            if spanning_tree_mode == "mstp":
                spanning_tree['mst_instances'] = {
                    "0": {
                        'priority': priority
                    }
                }
            elif spanning_tree_mode == "rapid-pvst":
                spanning_tree['rapid_pvst_instances'] = {
                    "1-4094": {
                        'priority': priority
                    }
                }
            elif spanning_tree_mode == "rstp":
                spanning_tree['rstp_priority'] = priority
        return spanning_tree

    @cached_property
    def service_unsupported_transceiver(self):
        if (unsupported_transceiver := get(self._hostvars, 'unsupported_transceiver')) is None:
            return None
        return {
            'license_name': unsupported_transceiver.get('license_name'),
            'license_key': unsupported_transceiver.get('license_key')
        }

    @cached_property
    def local_users(self):
        if (local_users := get(self._hostvars, 'local_users')) is None:
            return None
        local_users = self._convert_dicts(local_users, 'name')
        local_users_dict = {}
        for local_user in self._natural_sort(local_users, 'name'):
            name = local_user.get('name')
            local_users_dict[name] = {'privilege': get(local_user, 'privilege')}
            if (role := local_user.get('role')) is not None:
                local_users_dict[name]['role'] = role
            if (sha512_password := local_user.get('sha512_password')) is not None:
                local_users_dict[name]['sha512_password'] = sha512_password
            elif (no_password := local_user.get('no_password')) is not None:
                local_users_dict[name]['no_password'] = no_password
            if (ssh_key := local_user.get('ssh_key')) is not None:
                local_users_dict[name]['ssh_key'] = ssh_key
        return local_users_dict

    @cached_property
    def clock(self):
        if (timezone := get(self._hostvars, 'timezone')) is None:
            return None
        return {'timezone': timezone}

    @cached_property
    def vrfs(self):
        return {
            self._mgmt_interface_vrf: {
                'ip_routing': get(self._hostvars, 'mgmt_vrf_routing')
            }
        }

    @cached_property
    def management_interfaces(self):
        mgmt_interface = get(self._switch, 'mgmt_interface')
        if (
                mgmt_interface is None or
                self._mgmt_ip is None or
                self._mgmt_interface_vrf is None or
                self._mgmt_gateway is None
        ):
            return None
        return {
            mgmt_interface: {
                'description': 'oob_management',
                'shutdown': False,
                'vrf': self._mgmt_interface_vrf,
                'ip_address': self._mgmt_ip,
                'gateway': self._mgmt_gateway,
                'type': 'oob'
            }
        }

    @cached_property
    def tcam_profile(self):
        if (tcam_profile := get(self._platform_settings, 'tcam_profile')) is None:
            return None
        return {'system': tcam_profile}

    @cached_property
    def platform(self):
        platform = {}
        if (lag_hardware_only := get(self._platform_settings, 'lag_hardware_only')) is not None:
            platform['sand'] = {'lag': {'hardware_only': lag_hardware_only}}
        if (
                get(self._platform_settings, 'trident_forwarding_table_partition') is not None and
                get(self._switch, 'evpn_multicast') is True
        ):
            platform['trident'] = {'forwarding_table_partition': get(self._platform_settings,
                                                                     'trident_forwarding_table_partition')}
        if platform:
            return platform
        return None

    @cached_property
    def mac_address_table(self):
        if aging_time := get(self._hostvars, 'mac_address_table.aging_time') is None:
            return None
        return {'aging_time': aging_time}

    @cached_property
    def queue_monitor_streaming(self):
        enable = get(self._hostvars, 'queue_monitor_streaming.enable')
        vrf = get(self._hostvars, 'queue_monitor_streaming.vrf')
        if(
                enable is not True or
                vrf is None
        ):
            return None

        queue_monitor = {}
        if enable is True:
            queue_monitor['enable'] = enable
        if vrf is not None:
            queue_monitor['vrf'] = vrf
        return queue_monitor

    @cached_property
    def management_api_http(self):
        if (management_eapi := get(self._hostvars, 'management_eapi')) is None:
            return None
        management_api_http = {'enable_vrfs': {self._mgmt_interface_vrf: {}}}
        management_api = management_eapi.fromkeys(['enable_http', 'enable_https', 'default_services'])
        for key in dict(management_api).keys():
            if (value := management_eapi.get(key)) is not None:
                management_api[key] = value
            else:
                del management_api[key]
        management_api_http.update(management_api)
        return management_api_http

    @cached_property
    def link_tracking_groups(self):
        if (link_tracking_groups := get(self._switch, 'link_tracking_groups')) is None:
            return None
        return link_tracking_groups

    @cached_property
    def lacp(self):
        begin = get(self._switch, 'lacp_port_id.begin')
        end = get(self._switch, 'lacp_port_id.end')
        if begin is None or end is None:
            return None
        return {
            'port_id':
                {'range':
                    {'begin': begin,
                     'end': end,
                     }
                 }
        }

    @cached_property
    def eos_cli(self):
        raw_eos_cli = get(self._switch, 'raw_eos_cli')
        platform_raw_eos_cli = get(self._platform_settings, 'raw_eos_cli')
        if (
                raw_eos_cli is None and
                platform_raw_eos_cli is None
        ):
            return None
        return "\n".join(filter(None, [raw_eos_cli, platform_raw_eos_cli]))

    @cached_property
    def struct_cfg(self):
        if (struct_cfg := get(self._switch, 'struct_cfg')) is None:
            return None
        return struct_cfg
