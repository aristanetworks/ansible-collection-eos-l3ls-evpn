<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform</samp>](## "platform") | Dictionary |  |  |  | Every key below this point is platform dependent. |
    | [<samp>&nbsp;&nbsp;trident</samp>](## "platform.trident") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_table_partition</samp>](## "platform.trident.forwarding_table_partition") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l3</samp>](## "platform.trident.l3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing_mac_address_per_vlan</samp>](## "platform.trident.l3.routing_mac_address_per_vlan") | Boolean |  |  |  | Enable bridging of packets with destination MAC being a Router MAC in VLANs without routing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mmu</samp>](## "platform.trident.mmu") | Dictionary |  |  |  | Memory Management Unit settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;active_profile</samp>](## "platform.trident.mmu.active_profile") | String |  |  |  | The queue profile to be applied to the platform.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;queue_profiles</samp>](## "platform.trident.mmu.queue_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "platform.trident.mmu.queue_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_queues</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].id") | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the reservation value. If not specified, default is bytes.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reserved</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].reserved") | Integer |  |  |  | Amount of memory that should be reserved for this<br>queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].threshold") | String |  |  |  | Dynamic Shared Memory threshold.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;precedence</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop.precedence") | Integer | Required |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].multicast_queues.[].drop.threshold") | String | Required |  |  | Drop Threshold. This value may also be fractions.<br>Example: 7/8 or 3/4 or 1/2<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unicast_queues</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].id") | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].unit") | String |  |  | Valid Values:<br>- <code>bytes</code><br>- <code>cells</code> | Unit to be used for the reservation value. If not specified, default is bytes.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reserved</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].reserved") | Integer |  |  |  | Amount of memory that should be reserved for this<br>queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].threshold") | String |  |  |  | Dynamic Shared Memory threshold.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;precedence</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop.precedence") | Integer | Required |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "platform.trident.mmu.queue_profiles.[].unicast_queues.[].drop.threshold") | String | Required |  |  | Drop Threshold. This value may also be fractions.<br>Example: 7/8 or 3/4 or 1/2<br> |
    | [<samp>&nbsp;&nbsp;sand</samp>](## "platform.sand") | Dictionary |  |  |  | Most of the platform sand options are hardware dependent and optional. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_maps</samp>](## "platform.sand.qos_maps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;traffic_class</samp>](## "platform.sand.qos_maps.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to_network_qos</samp>](## "platform.sand.qos_maps.[].to_network_qos") | Integer |  |  | Min: 0<br>Max: 63 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lag</samp>](## "platform.sand.lag") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_only</samp>](## "platform.sand.lag.hardware_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "platform.sand.lag.mode") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;forwarding_mode</samp>](## "platform.sand.forwarding_mode") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast_replication</samp>](## "platform.sand.multicast_replication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "platform.sand.multicast_replication.default") | String |  |  | Valid Values:<br>- <code>ingress</code><br>- <code>egress</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mdb_profile</samp>](## "platform.sand.mdb_profile") | String |  |  | Valid Values:<br>- <code>balanced</code><br>- <code>balanced-xl</code><br>- <code>l3</code><br>- <code>l3-xl</code><br>- <code>l3-xxl</code><br>- <code>l3-xxxl</code> | Sand platforms MDB Profile configuration. Note: l3-xxxl does not support MLAG. |
    | [<samp>&nbsp;&nbsp;sfe</samp>](## "platform.sfe") | Dictionary |  |  |  | Sfe (Software Forwarding Engine) settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;data_plane_cpu_allocation_max</samp>](## "platform.sfe.data_plane_cpu_allocation_max") | Integer |  |  | Min: 1<br>Max: 128 | Maximum number of CPUs used for data plane traffic forwarding. |

=== "YAML"

    ```yaml
    # Every key below this point is platform dependent.
    platform:
      trident:
        forwarding_table_partition: <str>
        l3:

          # Enable bridging of packets with destination MAC being a Router MAC in VLANs without routing.
          routing_mac_address_per_vlan: <bool>

        # Memory Management Unit settings.
        mmu:

          # The queue profile to be applied to the platform.
          active_profile: <str>
          queue_profiles:
            - name: <str; required; unique>
              multicast_queues:
                - id: <int; 0-7; required; unique>

                  # Unit to be used for the reservation value. If not specified, default is bytes.
                  unit: <str; "bytes" | "cells">

                  # Amount of memory that should be reserved for this
                  # queue.
                  reserved: <int>

                  # Dynamic Shared Memory threshold.
                  threshold: <str>
                  drop:
                    precedence: <int; 1 | 2; required>

                    # Drop Threshold. This value may also be fractions.
                    # Example: 7/8 or 3/4 or 1/2
                    threshold: <str; required>
              unicast_queues:
                - id: <int; 0-7; required; unique>

                  # Unit to be used for the reservation value. If not specified, default is bytes.
                  unit: <str; "bytes" | "cells">

                  # Amount of memory that should be reserved for this
                  # queue.
                  reserved: <int>

                  # Dynamic Shared Memory threshold.
                  threshold: <str>
                  drop:
                    precedence: <int; 1 | 2; required>

                    # Drop Threshold. This value may also be fractions.
                    # Example: 7/8 or 3/4 or 1/2
                    threshold: <str; required>

      # Most of the platform sand options are hardware dependent and optional.
      sand:
        qos_maps:
          - traffic_class: <int; 0-7>
            to_network_qos: <int; 0-63>
        lag:
          hardware_only: <bool>
          mode: <str>
        forwarding_mode: <str>
        multicast_replication:
          default: <str; "ingress" | "egress">

        # Sand platforms MDB Profile configuration. Note: l3-xxxl does not support MLAG.
        mdb_profile: <str; "balanced" | "balanced-xl" | "l3" | "l3-xl" | "l3-xxl" | "l3-xxxl">

      # Sfe (Software Forwarding Engine) settings.
      sfe:

        # Maximum number of CPUs used for data plane traffic forwarding.
        data_plane_cpu_allocation_max: <int; 1-128>
    ```
