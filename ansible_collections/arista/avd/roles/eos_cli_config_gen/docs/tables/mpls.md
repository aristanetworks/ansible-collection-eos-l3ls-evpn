<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mpls</samp>](## "mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ip</samp>](## "mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ldp</samp>](## "mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_disabled_default</samp>](## "mpls.ldp.interface_disabled_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "mpls.ldp.router_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mpls.ldp.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transport_address_interface</samp>](## "mpls.ldp.transport_address_interface") | String |  |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;icmp</samp>](## "mpls.icmp") | Dictionary |  |  |  | Enables the LSRs to generate ICMP reply messages and deliver them to the originating host. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fragmentation_needed_tunneling</samp>](## "mpls.icmp.fragmentation_needed_tunneling") | Boolean |  |  |  | Enables the MPLS tunneling of MTU exceeded ICMP replies (fragmentation needed, packet too big). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ttl_exceeded_tunneling</samp>](## "mpls.icmp.ttl_exceeded_tunneling") | Boolean |  |  |  | Enables the MPLS tunneling of TTL exceeded ICMP replies. |
    | [<samp>&nbsp;&nbsp;rsvp</samp>](## "mpls.rsvp") | Dictionary |  |  |  | RSVP configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "mpls.rsvp.authentication") | Dictionary |  |  |  | Configure cryptographic authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_indexes</samp>](## "mpls.rsvp.authentication.password_indexes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;index</samp>](## "mpls.rsvp.authentication.password_indexes.[].index") | Integer | Required, Unique |  | Min: 1<br>Max: 4294967295 | Password index. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "mpls.rsvp.authentication.password_indexes.[].password_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication password type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "mpls.rsvp.authentication.password_indexes.[].password") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;active_index</samp>](## "mpls.rsvp.authentication.active_index") | Integer |  |  |  | Use index as active password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_number_window</samp>](## "mpls.rsvp.authentication.sequence_number_window") | Integer |  |  | Min: 1<br>Max: 255 | Index in the sequence.<br>Size of reorder window. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "mpls.rsvp.authentication.type") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>none</code> | Authentication mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group</samp>](## "mpls.rsvp.ip_access_group") | String |  |  |  | IP config commands.<br>Access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group</samp>](## "mpls.rsvp.ipv6_access_group") | String |  |  |  | IPv6 config commands.<br>Access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute</samp>](## "mpls.rsvp.fast_reroute") | Dictionary |  |  |  | Configure fast reroute. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mpls.rsvp.fast_reroute.mode") | String |  |  | Valid Values:<br>- <code>link-protection</code><br>- <code>node-protection</code><br>- <code>none</code> | Fast reroute mode.<br>Protect against failure of the next link.<br>Protect against failure of the next node.<br>Disable fast reroute. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reversion</samp>](## "mpls.rsvp.fast_reroute.reversion") | String |  |  | Valid Values:<br>- <code>global</code><br>- <code>local</code> | Select reversion behavior.<br>Global revertive repair.<br>Local revertive repair. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bypass_tunnel_optimization_interval</samp>](## "mpls.rsvp.fast_reroute.bypass_tunnel_optimization_interval") | Integer |  |  | Min: 1<br>Max: 65535 | Fast-reroute bypass configuration.<br>Interval between each re-optimization attempt. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;label_local_termination</samp>](## "mpls.rsvp.label_local_termination") | String |  |  | Valid Values:<br>- <code>implicit-null</code><br>- <code>explicit-null</code> | Local termination label to be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;preemption_method</samp>](## "mpls.rsvp.preemption_method") | Dictionary |  |  |  | Configure preemption. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preemption</samp>](## "mpls.rsvp.preemption_method.preemption") | String | Required |  | Valid Values:<br>- <code>hard</code><br>- <code>soft</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer</samp>](## "mpls.rsvp.preemption_method.timer") | Integer |  |  | Min: 1<br>Max: 65535 | Timer value in units of seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu_signaling</samp>](## "mpls.rsvp.mtu_signaling") | Boolean |  |  |  | Enable MTU signaling. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart</samp>](## "mpls.rsvp.graceful_restart") | Dictionary |  |  |  | RSVP graceful restart. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role_helper</samp>](## "mpls.rsvp.graceful_restart.role_helper") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.graceful_restart.role_helper.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grace_period_recovery</samp>](## "mpls.rsvp.graceful_restart.role_helper.grace_period_recovery") | Integer |  |  | Min: 1<br>Max: 320 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grace_period_restart</samp>](## "mpls.rsvp.graceful_restart.role_helper.grace_period_restart") | Integer |  |  | Min: 1<br>Max: 320 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role_speaker</samp>](## "mpls.rsvp.graceful_restart.role_speaker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.graceful_restart.role_speaker.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grace_period_recovery</samp>](## "mpls.rsvp.graceful_restart.role_speaker.grace_period_recovery") | Integer |  |  | Min: 1<br>Max: 320 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grace_period_restart</samp>](## "mpls.rsvp.graceful_restart.role_speaker.grace_period_restart") | Integer |  |  | Min: 1<br>Max: 320 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hello</samp>](## "mpls.rsvp.hello") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "mpls.rsvp.hello.interval") | Integer |  |  | Min: 1<br>Max: 60 | Time between hello messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "mpls.rsvp.hello.multiplier") | Integer |  |  | Min: 1<br>Max: 255 | Number of missed hellos after which the neighbor is expired. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hitless_restart</samp>](## "mpls.rsvp.hitless_restart") | Dictionary |  |  |  | RSVP hitless restart. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "mpls.rsvp.hitless_restart.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer_recovery</samp>](## "mpls.rsvp.hitless_restart.timer_recovery") | Integer |  |  | Min: 1<br>Max: 320 | Time stale states will be preserved after restart. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;p2mp_enabled</samp>](## "mpls.rsvp.p2mp_enabled") | Boolean |  |  |  | P2MP configuration.<br>To disable P2MP make `p2mp_enabled` false. |

=== "YAML"

    ```yaml
    mpls:
      ip: <bool>
      ldp:
        interface_disabled_default: <bool>
        router_id: <str>
        shutdown: <bool>

        # Interface Name.
        transport_address_interface: <str>

      # Enables the LSRs to generate ICMP reply messages and deliver them to the originating host.
      icmp:

        # Enables the MPLS tunneling of MTU exceeded ICMP replies (fragmentation needed, packet too big).
        fragmentation_needed_tunneling: <bool>

        # Enables the MPLS tunneling of TTL exceeded ICMP replies.
        ttl_exceeded_tunneling: <bool>

      # RSVP configuration.
      rsvp:

        # Configure cryptographic authentication.
        authentication:
          password_indexes:

              # Password index.
            - index: <int; 1-4294967295; required; unique>

              # Configure authentication password type.
              password_type: <str; "0" | "7" | "8a"; required>

              # Password string.
              password: <str; required>

          # Use index as active password.
          active_index: <int>

          # Index in the sequence.
          # Size of reorder window.
          sequence_number_window: <int; 1-255>

          # Authentication mechanism.
          type: <str; "md5" | "none">

        # IP config commands.
        # Access list name.
        ip_access_group: <str>

        # IPv6 config commands.
        # Access list name.
        ipv6_access_group: <str>

        # Configure fast reroute.
        fast_reroute:

          # Fast reroute mode.
          # Protect against failure of the next link.
          # Protect against failure of the next node.
          # Disable fast reroute.
          mode: <str; "link-protection" | "node-protection" | "none">

          # Select reversion behavior.
          # Global revertive repair.
          # Local revertive repair.
          reversion: <str; "global" | "local">

          # Fast-reroute bypass configuration.
          # Interval between each re-optimization attempt.
          bypass_tunnel_optimization_interval: <int; 1-65535>

        # Local termination label to be advertised.
        label_local_termination: <str; "implicit-null" | "explicit-null">

        # Configure preemption.
        preemption_method:
          preemption: <str; "hard" | "soft"; required>

          # Timer value in units of seconds.
          timer: <int; 1-65535>

        # Enable MTU signaling.
        mtu_signaling: <bool>

        # RSVP graceful restart.
        graceful_restart:
          role_helper:
            enabled: <bool; required>
            grace_period_recovery: <int; 1-320>
            grace_period_restart: <int; 1-320>
          role_speaker:
            enabled: <bool; required>
            grace_period_recovery: <int; 1-320>
            grace_period_restart: <int; 1-320>
        hello:

          # Time between hello messages.
          interval: <int; 1-60>

          # Number of missed hellos after which the neighbor is expired.
          multiplier: <int; 1-255>

        # RSVP hitless restart.
        hitless_restart:
          enabled: <bool>

          # Time stale states will be preserved after restart.
          timer_recovery: <int; 1-320>

        # P2MP configuration.
        # To disable P2MP make `p2mp_enabled` false.
        p2mp_enabled: <bool>
    ```
