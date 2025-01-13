<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "<node_type_keys.key>.defaults.ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.ptp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "<node_type_keys.key>.defaults.ptp.profile") | String |  |  |  | Default available profiles are:<br>  - "aes67"<br>  - "aes67-r16-2016"<br>  - "smpte2059-2" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.defaults.ptp.mlag") | Boolean |  | `False` |  | Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "<node_type_keys.key>.defaults.ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "<node_type_keys.key>.defaults.ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "<node_type_keys.key>.defaults.ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "<node_type_keys.key>.defaults.ptp.auto_clock_identity") | Boolean |  |  |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "<node_type_keys.key>.defaults.ptp.clock_identity_prefix") | String |  | `00:1C:73` |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "<node_type_keys.key>.defaults.ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "<node_type_keys.key>.defaults.ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.defaults.ptp.mode") | String |  | `boundary` | Valid Values:<br>- <code>boundary</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode_one_step</samp>](## "<node_type_keys.key>.defaults.ptp.mode_one_step") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "<node_type_keys.key>.defaults.ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "<node_type_keys.key>.defaults.ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "<node_type_keys.key>.defaults.ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "<node_type_keys.key>.defaults.ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "<node_type_keys.key>.defaults.ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "<node_type_keys.key>.defaults.ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.defaults.ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.profile") | String |  |  |  | Default available profiles are:<br>  - "aes67"<br>  - "aes67-r16-2016"<br>  - "smpte2059-2" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.mlag") | Boolean |  | `False` |  | Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.auto_clock_identity") | Boolean |  |  |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.clock_identity_prefix") | String |  | `00:1C:73` |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.mode") | String |  | `boundary` | Valid Values:<br>- <code>boundary</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode_one_step</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.mode_one_step") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "<node_type_keys.key>.node_groups.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].ptp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "<node_type_keys.key>.node_groups.[].ptp.profile") | String |  |  |  | Default available profiles are:<br>  - "aes67"<br>  - "aes67-r16-2016"<br>  - "smpte2059-2" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.node_groups.[].ptp.mlag") | Boolean |  | `False` |  | Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "<node_type_keys.key>.node_groups.[].ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "<node_type_keys.key>.node_groups.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "<node_type_keys.key>.node_groups.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "<node_type_keys.key>.node_groups.[].ptp.auto_clock_identity") | Boolean |  |  |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "<node_type_keys.key>.node_groups.[].ptp.clock_identity_prefix") | String |  | `00:1C:73` |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "<node_type_keys.key>.node_groups.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "<node_type_keys.key>.node_groups.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].ptp.mode") | String |  | `boundary` | Valid Values:<br>- <code>boundary</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode_one_step</samp>](## "<node_type_keys.key>.node_groups.[].ptp.mode_one_step") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "<node_type_keys.key>.node_groups.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "<node_type_keys.key>.node_groups.[].ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "<node_type_keys.key>.node_groups.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "<node_type_keys.key>.node_groups.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "<node_type_keys.key>.node_groups.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.node_groups.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "<node_type_keys.key>.nodes.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].ptp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "<node_type_keys.key>.nodes.[].ptp.profile") | String |  |  |  | Default available profiles are:<br>  - "aes67"<br>  - "aes67-r16-2016"<br>  - "smpte2059-2" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "<node_type_keys.key>.nodes.[].ptp.mlag") | Boolean |  | `False` |  | Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "<node_type_keys.key>.nodes.[].ptp.domain") | Integer |  | `127` | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority1</samp>](## "<node_type_keys.key>.nodes.[].ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 | default -> automatically set based on node_type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority2</samp>](## "<node_type_keys.key>.nodes.[].ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 | default -> (node_id modulus 256).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_clock_identity</samp>](## "<node_type_keys.key>.nodes.[].ptp.auto_clock_identity") | Boolean |  |  |  | If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.<br>default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity_prefix</samp>](## "<node_type_keys.key>.nodes.[].ptp.clock_identity_prefix") | String |  | `00:1C:73` |  | PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".<br>By default the 3-byte prefix is "00:1C:73".<br>This can be overridden if auto_clock_identity is set to true (which is the default).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clock_identity</samp>](## "<node_type_keys.key>.nodes.[].ptp.clock_identity") | String |  |  |  | Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ip</samp>](## "<node_type_keys.key>.nodes.[].ptp.source_ip") | String |  |  |  | By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.<br>This can be set manually if required, for example, to a value of "10.1.2.3".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.nodes.[].ptp.mode") | String |  | `boundary` | Valid Values:<br>- <code>boundary</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode_one_step</samp>](## "<node_type_keys.key>.nodes.[].ptp.mode_one_step") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "<node_type_keys.key>.nodes.[].ptp.ttl") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_unicast</samp>](## "<node_type_keys.key>.nodes.[].ptp.forward_unicast") | Boolean |  | `False` |  | Enable PTP unicast forwarding.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "<node_type_keys.key>.nodes.[].ptp.dscp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;general_messages</samp>](## "<node_type_keys.key>.nodes.[].ptp.dscp.general_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event_messages</samp>](## "<node_type_keys.key>.nodes.[].ptp.dscp.event_messages") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.threshold.offset_from_master") | Integer |  | `250` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.threshold.mean_path_delay") | Integer |  | `1500` | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.sequence_ids.announce") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  | `3` | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "<node_type_keys.key>.nodes.[].ptp.monitor.missing_message.sequence_ids.sync") | Integer |  | `3` | Min: 2<br>Max: 255 |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:
        ptp:
          enabled: <bool>

          # Default available profiles are:
          #   - "aes67"
          #   - "aes67-r16-2016"
          #   - "smpte2059-2"
          profile: <str>

          # Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel.
          mlag: <bool; default=False>
          domain: <int; 0-255; default=127>

          # default -> automatically set based on node_type.
          priority1: <int; 0-255>

          # default -> (node_id modulus 256).
          priority2: <int; 0-255>

          # If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.
          # default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).
          auto_clock_identity: <bool>

          # PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
          # By default the 3-byte prefix is "00:1C:73".
          # This can be overridden if auto_clock_identity is set to true (which is the default).
          clock_identity_prefix: <str; default="00:1C:73">

          # Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
          clock_identity: <str>

          # By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.
          # This can be set manually if required, for example, to a value of "10.1.2.3".
          source_ip: <str>
          mode: <str; "boundary"; default="boundary">
          mode_one_step: <bool; default=False>
          ttl: <int>

          # Enable PTP unicast forwarding.
          forward_unicast: <bool; default=False>
          dscp:
            general_messages: <int>
            event_messages: <int>
          monitor:
            enabled: <bool; default=True>
            threshold:
              offset_from_master: <int; 0-1000000000; default=250>
              mean_path_delay: <int; 0-1000000000; default=1500>
              drop:
                offset_from_master: <int; 0-1000000000>
                mean_path_delay: <int; 0-1000000000>
            missing_message:
              intervals:
                announce: <int; 2-255>
                follow_up: <int; 2-255>
                sync: <int; 2-255>
              sequence_ids:
                enabled: <bool; default=True>
                announce: <int; 2-255; default=3>
                delay_resp: <int; 2-255; default=3>
                follow_up: <int; 2-255; default=3>
                sync: <int; 2-255; default=3>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>
              ptp:
                enabled: <bool>

                # Default available profiles are:
                #   - "aes67"
                #   - "aes67-r16-2016"
                #   - "smpte2059-2"
                profile: <str>

                # Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel.
                mlag: <bool; default=False>
                domain: <int; 0-255; default=127>

                # default -> automatically set based on node_type.
                priority1: <int; 0-255>

                # default -> (node_id modulus 256).
                priority2: <int; 0-255>

                # If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.
                # default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).
                auto_clock_identity: <bool>

                # PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
                # By default the 3-byte prefix is "00:1C:73".
                # This can be overridden if auto_clock_identity is set to true (which is the default).
                clock_identity_prefix: <str; default="00:1C:73">

                # Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
                clock_identity: <str>

                # By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.
                # This can be set manually if required, for example, to a value of "10.1.2.3".
                source_ip: <str>
                mode: <str; "boundary"; default="boundary">
                mode_one_step: <bool; default=False>
                ttl: <int>

                # Enable PTP unicast forwarding.
                forward_unicast: <bool; default=False>
                dscp:
                  general_messages: <int>
                  event_messages: <int>
                monitor:
                  enabled: <bool; default=True>
                  threshold:
                    offset_from_master: <int; 0-1000000000; default=250>
                    mean_path_delay: <int; 0-1000000000; default=1500>
                    drop:
                      offset_from_master: <int; 0-1000000000>
                      mean_path_delay: <int; 0-1000000000>
                  missing_message:
                    intervals:
                      announce: <int; 2-255>
                      follow_up: <int; 2-255>
                      sync: <int; 2-255>
                    sequence_ids:
                      enabled: <bool; default=True>
                      announce: <int; 2-255; default=3>
                      delay_resp: <int; 2-255; default=3>
                      follow_up: <int; 2-255; default=3>
                      sync: <int; 2-255; default=3>
          ptp:
            enabled: <bool>

            # Default available profiles are:
            #   - "aes67"
            #   - "aes67-r16-2016"
            #   - "smpte2059-2"
            profile: <str>

            # Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel.
            mlag: <bool; default=False>
            domain: <int; 0-255; default=127>

            # default -> automatically set based on node_type.
            priority1: <int; 0-255>

            # default -> (node_id modulus 256).
            priority2: <int; 0-255>

            # If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.
            # default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).
            auto_clock_identity: <bool>

            # PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
            # By default the 3-byte prefix is "00:1C:73".
            # This can be overridden if auto_clock_identity is set to true (which is the default).
            clock_identity_prefix: <str; default="00:1C:73">

            # Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
            clock_identity: <str>

            # By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.
            # This can be set manually if required, for example, to a value of "10.1.2.3".
            source_ip: <str>
            mode: <str; "boundary"; default="boundary">
            mode_one_step: <bool; default=False>
            ttl: <int>

            # Enable PTP unicast forwarding.
            forward_unicast: <bool; default=False>
            dscp:
              general_messages: <int>
              event_messages: <int>
            monitor:
              enabled: <bool; default=True>
              threshold:
                offset_from_master: <int; 0-1000000000; default=250>
                mean_path_delay: <int; 0-1000000000; default=1500>
                drop:
                  offset_from_master: <int; 0-1000000000>
                  mean_path_delay: <int; 0-1000000000>
              missing_message:
                intervals:
                  announce: <int; 2-255>
                  follow_up: <int; 2-255>
                  sync: <int; 2-255>
                sequence_ids:
                  enabled: <bool; default=True>
                  announce: <int; 2-255; default=3>
                  delay_resp: <int; 2-255; default=3>
                  follow_up: <int; 2-255; default=3>
                  sync: <int; 2-255; default=3>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>
          ptp:
            enabled: <bool>

            # Default available profiles are:
            #   - "aes67"
            #   - "aes67-r16-2016"
            #   - "smpte2059-2"
            profile: <str>

            # Configure PTP on the MLAG peer-link port-channel when PTP is enabled. By default PTP will not be configured on the MLAG peer-link port-channel.
            mlag: <bool; default=False>
            domain: <int; 0-255; default=127>

            # default -> automatically set based on node_type.
            priority1: <int; 0-255>

            # default -> (node_id modulus 256).
            priority2: <int; 0-255>

            # If you prefer to have PTP clock identity be the system MAC-address of the switch, which is the default EOS behaviour, simply disable the automatic PTP clock identity.
            # default -> (clock_identity_prefix = 00:1C:73 (default)) + (PTP priority 1 as HEX) + ":00:" + (PTP priority 2 as HEX).
            auto_clock_identity: <bool>

            # PTP clock idetentiy 3-byte prefix. i.e. "01:02:03".
            # By default the 3-byte prefix is "00:1C:73".
            # This can be overridden if auto_clock_identity is set to true (which is the default).
            clock_identity_prefix: <str; default="00:1C:73">

            # Set PTP clock identity manually. 6-byte value i.e. "01:02:03:04:05:06".
            clock_identity: <str>

            # By default in EOS, PTP packets are sourced with an IP address from the routed port or from the relevant SVI, which is the recommended behaviour.
            # This can be set manually if required, for example, to a value of "10.1.2.3".
            source_ip: <str>
            mode: <str; "boundary"; default="boundary">
            mode_one_step: <bool; default=False>
            ttl: <int>

            # Enable PTP unicast forwarding.
            forward_unicast: <bool; default=False>
            dscp:
              general_messages: <int>
              event_messages: <int>
            monitor:
              enabled: <bool; default=True>
              threshold:
                offset_from_master: <int; 0-1000000000; default=250>
                mean_path_delay: <int; 0-1000000000; default=1500>
                drop:
                  offset_from_master: <int; 0-1000000000>
                  mean_path_delay: <int; 0-1000000000>
              missing_message:
                intervals:
                  announce: <int; 2-255>
                  follow_up: <int; 2-255>
                  sync: <int; 2-255>
                sequence_ids:
                  enabled: <bool; default=True>
                  announce: <int; 2-255; default=3>
                  delay_resp: <int; 2-255; default=3>
                  follow_up: <int; 2-255; default=3>
                  sync: <int; 2-255; default=3>
    ```
