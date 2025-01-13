<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Gives the ability to monitor and react to Syslog messages.<br>Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,<br>customize the system behavior, and implement workarounds to problems discovered in the field.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;actions</samp>](## "event_handlers.[].actions") | Dictionary |  |  |  | Note: `bash_command` and `log` are mutually exclusive. `bash_command` takes precedence over `log`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bash_command</samp>](## "event_handlers.[].actions.bash_command") | String |  |  |  | Define BASH command action. Command could be multiline also. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "event_handlers.[].actions.log") | Boolean |  |  |  | Log a message when the event is triggered. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;increment_device_health_metric</samp>](## "event_handlers.[].actions.increment_device_health_metric") | String |  |  |  | Name of device-health metric. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- <code>on-boot</code><br>- <code>on-counters</code><br>- <code>on-intf</code><br>- <code>on-logging</code><br>- <code>on-maintenance</code><br>- <code>on-startup-config</code><br>- <code>vm-tracer vm</code> | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_counters</samp>](## "event_handlers.[].trigger_on_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;condition</samp>](## "event_handlers.[].trigger_on_counters.condition") | String |  |  |  | Set the logical expression to evaluate. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;granularity_per_source</samp>](## "event_handlers.[].trigger_on_counters.granularity_per_source") | Boolean |  |  |  | Set the granularity of event counting for a wildcarded condition.<br>Example -<br>  condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )<br>  [* wildcard is used here] |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poll_interval</samp>](## "event_handlers.[].trigger_on_counters.poll_interval") | Integer |  |  | Min: 1<br>Max: 1000000 | Set the polling interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_logging</samp>](## "event_handlers.[].trigger_on_logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poll_interval</samp>](## "event_handlers.[].trigger_on_logging.poll_interval") | Integer |  |  | Min: 1<br>Max: 1000000 | Set the polling interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].trigger_on_logging.regex") | String |  |  |  | Regular expression to use for searching log messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_intf</samp>](## "event_handlers.[].trigger_on_intf") | Dictionary |  |  |  | Trigger condition occurs on specified interface changes.<br>Note: Any one of the `ip`, `ipv6` and `operstatus` key needs to be defined along with the `interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "event_handlers.[].trigger_on_intf.interface") | String | Required |  |  | Interface name.<br>Example - Ethernet4<br>          Loopback4-6<br>          Port-channel4,7 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "event_handlers.[].trigger_on_intf.ip") | Boolean |  |  |  | Action is triggered upon changes to interface IP address assignment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "event_handlers.[].trigger_on_intf.ipv6") | Boolean |  |  |  | Action is triggered upon changes to interface ipv6 address assignment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operstatus</samp>](## "event_handlers.[].trigger_on_intf.operstatus") | Boolean |  |  |  | Action is triggered upon changes to interface operStatus. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_maintenance</samp>](## "event_handlers.[].trigger_on_maintenance") | Dictionary |  |  |  | Settings required for trigger 'on-maintenance'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operation</samp>](## "event_handlers.[].trigger_on_maintenance.operation") | String | Required |  | Valid Values:<br>- <code>enter</code><br>- <code>exit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer</samp>](## "event_handlers.[].trigger_on_maintenance.bgp_peer") | String |  |  |  | Ipv4/Ipv6 address or peer group name.<br>Trigger condition occurs on maintenance operation of specified BGP peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].trigger_on_maintenance.action") | String | Required |  | Valid Values:<br>- <code>after</code><br>- <code>before</code><br>- <code>all</code><br>- <code>begin</code><br>- <code>end</code> | Action for maintenance operation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stage</samp>](## "event_handlers.[].trigger_on_maintenance.stage") | String |  |  | Valid Values:<br>- <code>bgp</code><br>- <code>linkdown</code><br>- <code>mlag</code><br>- <code>ratemon</code> | Action is triggered after/before specified stage. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "event_handlers.[].trigger_on_maintenance.vrf") | String |  |  |  | VRF name. VRF can be defined for "bgp_peer" only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "event_handlers.[].trigger_on_maintenance.interface") | String |  |  |  | Trigger condition occurs on maintenance operation of specified interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "event_handlers.[].trigger_on_maintenance.unit") | String |  |  |  | Name of unit. Trigger condition occurs on maintenance operation of specified unit |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | `False` |  | Set the action to be non-blocking.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") <span style="color:red">removed</span> | String |  |  | Valid Values:<br>- <code>bash</code><br>- <code>increment</code><br>- <code>log</code> | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>event_handlers.actions</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") <span style="color:red">removed</span> | String |  |  |  | Command to execute.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>event_handlers.actions.bash_command</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") <span style="color:red">removed</span> | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>event_handlers.trigger_on_logging.regex</samp> instead.</span> |

=== "YAML"

    ```yaml
    # Gives the ability to monitor and react to Syslog messages.
    # Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
    # customize the system behavior, and implement workarounds to problems discovered in the field.
    event_handlers:

        # Event Handler Name.
      - name: <str; required; unique>

        # Note: `bash_command` and `log` are mutually exclusive. `bash_command` takes precedence over `log`.
        actions:

          # Define BASH command action. Command could be multiline also.
          bash_command: <str>

          # Log a message when the event is triggered.
          log: <bool>

          # Name of device-health metric.
          increment_device_health_metric: <str>

        # Event-handler delay in seconds.
        delay: <int>

        # Configure event trigger condition.
        trigger: <str; "on-boot" | "on-counters" | "on-intf" | "on-logging" | "on-maintenance" | "on-startup-config" | "vm-tracer vm">
        trigger_on_counters:

          # Set the logical expression to evaluate.
          condition: <str>

          # Set the granularity of event counting for a wildcarded condition.
          # Example -
          #   condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )
          #   [* wildcard is used here]
          granularity_per_source: <bool>

          # Set the polling interval in seconds.
          poll_interval: <int; 1-1000000>
        trigger_on_logging:

          # Set the polling interval in seconds.
          poll_interval: <int; 1-1000000>

          # Regular expression to use for searching log messages.
          regex: <str>

        # Trigger condition occurs on specified interface changes.
        # Note: Any one of the `ip`, `ipv6` and `operstatus` key needs to be defined along with the `interface`.
        trigger_on_intf:

          # Interface name.
          # Example - Ethernet4
          #           Loopback4-6
          #           Port-channel4,7
          interface: <str; required>

          # Action is triggered upon changes to interface IP address assignment.
          ip: <bool>

          # Action is triggered upon changes to interface ipv6 address assignment.
          ipv6: <bool>

          # Action is triggered upon changes to interface operStatus.
          operstatus: <bool>

        # Settings required for trigger 'on-maintenance'.
        trigger_on_maintenance:
          operation: <str; "enter" | "exit"; required>

          # Ipv4/Ipv6 address or peer group name.
          # Trigger condition occurs on maintenance operation of specified BGP peer.
          bgp_peer: <str>

          # Action for maintenance operation.
          action: <str; "after" | "before" | "all" | "begin" | "end"; required>

          # Action is triggered after/before specified stage.
          stage: <str; "bgp" | "linkdown" | "mlag" | "ratemon">

          # VRF name. VRF can be defined for "bgp_peer" only.
          vrf: <str>

          # Trigger condition occurs on maintenance operation of specified interface.
          interface: <str>

          # Name of unit. Trigger condition occurs on maintenance operation of specified unit
          unit: <str>

        # Set the action to be non-blocking.
        asynchronous: <bool; default=False>
    ```
