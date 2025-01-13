<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>logging</samp>](## "logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;console</samp>](## "logging.console") | String |  |  | Valid Values:<br>- <code>debugging</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>errors</code><br>- <code>critical</code><br>- <code>alerts</code><br>- <code>emergencies</code><br>- <code>disabled</code> | Console logging severity level. |
    | [<samp>&nbsp;&nbsp;monitor</samp>](## "logging.monitor") | String |  |  | Valid Values:<br>- <code>debugging</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>errors</code><br>- <code>critical</code><br>- <code>alerts</code><br>- <code>emergencies</code><br>- <code>disabled</code> | Monitor logging severity level. |
    | [<samp>&nbsp;&nbsp;buffered</samp>](## "logging.buffered") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "logging.buffered.size") | Integer |  |  | Min: 10<br>Max: 2147483647 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging.buffered.level") | String |  |  | Valid Values:<br>- <code>alerts</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>disabled</code> | Buffer logging severity level. |
    | [<samp>&nbsp;&nbsp;repeat_messages</samp>](## "logging.repeat_messages") | Boolean |  |  |  | Summarize concurrent repeat messages. |
    | [<samp>&nbsp;&nbsp;trap</samp>](## "logging.trap") | String |  |  | Valid Values:<br>- <code>alerts</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>system</code><br>- <code>warnings</code><br>- <code>disabled</code> | Trap logging severity level. |
    | [<samp>&nbsp;&nbsp;synchronous</samp>](## "logging.synchronous") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "logging.synchronous.level") | String |  | `critical` | Valid Values:<br>- <code>alerts</code><br>- <code>all</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>disabled</code> | Synchronous logging severity level. |
    | [<samp>&nbsp;&nbsp;format</samp>](## "logging.format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp>](## "logging.format.timestamp") | String |  |  | Valid Values:<br>- <code>high-resolution</code><br>- <code>traditional</code><br>- <code>traditional timezone</code><br>- <code>traditional year</code><br>- <code>traditional timezone year</code><br>- <code>traditional year timezone</code> | Timestamp format. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "logging.format.hostname") | String |  |  | Valid Values:<br>- <code>fqdn</code><br>- <code>ipv4</code> | Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "logging.format.sequence_numbers") | Boolean |  |  |  | Add sequence numbers to log messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rfc5424</samp>](## "logging.format.rfc5424") | Boolean |  |  |  | Forward logs in RFC5424 format. |
    | [<samp>&nbsp;&nbsp;facility</samp>](## "logging.facility") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>cron</code><br>- <code>daemon</code><br>- <code>kern</code><br>- <code>local0</code><br>- <code>local1</code><br>- <code>local2</code><br>- <code>local3</code><br>- <code>local4</code><br>- <code>local5</code><br>- <code>local6</code><br>- <code>local7</code><br>- <code>lpr</code><br>- <code>mail</code><br>- <code>news</code><br>- <code>sys9</code><br>- <code>sys10</code><br>- <code>sys11</code><br>- <code>sys12</code><br>- <code>sys13</code><br>- <code>sys14</code><br>- <code>syslog</code><br>- <code>user</code><br>- <code>uucp</code> |  |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "logging.source_interface") | String |  |  |  | Source Interface Name. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "logging.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "logging.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "logging.vrfs.[].source_interface") | String |  |  |  | Source interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "logging.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "logging.vrfs.[].hosts.[].name") | String | Required, Unique |  |  | Syslog server name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "logging.vrfs.[].hosts.[].protocol") | String |  | `udp` | Valid Values:<br>- <code>tcp</code><br>- <code>udp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "logging.vrfs.[].hosts.[].ports") | List, items: Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;int&gt;</samp>](## "logging.vrfs.[].hosts.[].ports.[]") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policy</samp>](## "logging.policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "logging.policy.match") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_lists</samp>](## "logging.policy.match.match_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "logging.policy.match.match_lists.[].name") | String | Required, Unique |  |  | Match list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "logging.policy.match.match_lists.[].action") | String |  |  | Valid Values:<br>- <code>discard</code> |  |
    | [<samp>&nbsp;&nbsp;event</samp>](## "logging.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;congestion_drops_interval</samp>](## "logging.event.congestion_drops_interval") | Integer |  |  | Min: 1<br>Max: 65535 | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;global_link_status</samp>](## "logging.event.global_link_status") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "logging.event.storm_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;discards</samp>](## "logging.event.storm_control.discards") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;global</samp>](## "logging.event.storm_control.discards.global") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "logging.event.storm_control.discards.interval") | Integer |  |  | Min: 10<br>Max: 65535 | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;level</samp>](## "logging.level") | List, items: Dictionary |  |  |  | Configure logging severity. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;facility</samp>](## "logging.level.[].facility") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</samp>](## "logging.level.[].severity") | String |  |  | Valid Values:<br>- <code>alerts</code><br>- <code>critical</code><br>- <code>debugging</code><br>- <code>emergencies</code><br>- <code>errors</code><br>- <code>informational</code><br>- <code>notifications</code><br>- <code>warnings</code><br>- <code>0</code><br>- <code>1</code><br>- <code>2</code><br>- <code>3</code><br>- <code>4</code><br>- <code>5</code><br>- <code>6</code><br>- <code>7</code> | Severity of facility. Below are the supported severities.<br>emergencies    System is unusable                (severity=0)<br>alerts         Immediate action needed           (severity=1)<br>critical       Critical conditions               (severity=2)<br>errors         Error conditions                  (severity=3)<br>warnings       Warning conditions                (severity=4)<br>notifications  Normal but significant conditions (severity=5)<br>informational  Informational messages            (severity=6)<br>debugging      Debugging messages                (severity=7)<br><0-7>          Severity level value |

=== "YAML"

    ```yaml
    logging:

      # Console logging severity level.
      console: <str; "debugging" | "informational" | "notifications" | "warnings" | "errors" | "critical" | "alerts" | "emergencies" | "disabled">

      # Monitor logging severity level.
      monitor: <str; "debugging" | "informational" | "notifications" | "warnings" | "errors" | "critical" | "alerts" | "emergencies" | "disabled">
      buffered:
        size: <int; 10-2147483647>

        # Buffer logging severity level.
        level: <str; "alerts" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "warnings" | "disabled">

      # Summarize concurrent repeat messages.
      repeat_messages: <bool>

      # Trap logging severity level.
      trap: <str; "alerts" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "system" | "warnings" | "disabled">
      synchronous:

        # Synchronous logging severity level.
        level: <str; "alerts" | "all" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "warnings" | "disabled"; default="critical">
      format:

        # Timestamp format.
        timestamp: <str; "high-resolution" | "traditional" | "traditional timezone" | "traditional year" | "traditional timezone year" | "traditional year timezone">

        # Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour).
        hostname: <str; "fqdn" | "ipv4">

        # Add sequence numbers to log messages.
        sequence_numbers: <bool>

        # Forward logs in RFC5424 format.
        rfc5424: <bool>
      facility: <str; "auth" | "cron" | "daemon" | "kern" | "local0" | "local1" | "local2" | "local3" | "local4" | "local5" | "local6" | "local7" | "lpr" | "mail" | "news" | "sys9" | "sys10" | "sys11" | "sys12" | "sys13" | "sys14" | "syslog" | "user" | "uucp">

      # Source Interface Name.
      source_interface: <str>
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Source interface name.
          source_interface: <str>
          hosts:

              # Syslog server name.
            - name: <str; required; unique>
              protocol: <str; "tcp" | "udp"; default="udp">
              ports:
                - <int>
      policy:
        match:
          match_lists:

              # Match list.
            - name: <str; required; unique>
              action: <str; "discard">
      event:

        # Logging interval in seconds.
        congestion_drops_interval: <int; 1-65535>
        global_link_status: <bool>
        storm_control:
          discards:
            global: <bool>

            # Logging interval in seconds.
            interval: <int; 10-65535>

      # Configure logging severity.
      level:
        - facility: <str; required; unique>

          # Severity of facility. Below are the supported severities.
          # emergencies    System is unusable                (severity=0)
          # alerts         Immediate action needed           (severity=1)
          # critical       Critical conditions               (severity=2)
          # errors         Error conditions                  (severity=3)
          # warnings       Warning conditions                (severity=4)
          # notifications  Normal but significant conditions (severity=5)
          # informational  Informational messages            (severity=6)
          # debugging      Debugging messages                (severity=7)
          # <0-7>          Severity level value
          severity: <str; "alerts" | "critical" | "debugging" | "emergencies" | "errors" | "informational" | "notifications" | "warnings" | "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7">
    ```
