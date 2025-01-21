<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_api_gnmi</samp>](## "management_api_gnmi") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;provider</samp>](## "management_api_gnmi.provider") | String |  | `eos-native` |  |  |
    | [<samp>&nbsp;&nbsp;transport</samp>](## "management_api_gnmi.transport") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;grpc</samp>](## "management_api_gnmi.transport.grpc") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_api_gnmi.transport.grpc.[].name") | String | Required, Unique |  |  | Transport name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "management_api_gnmi.transport.grpc.[].ssl_profile") | String |  |  |  | SSL profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_api_gnmi.transport.grpc.[].vrf") | String |  |  |  | VRF name is optional. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notification_timestamp</samp>](## "management_api_gnmi.transport.grpc.[].notification_timestamp") | String |  |  | Valid Values:<br>- <code>send-time</code><br>- <code>last-change-time</code> | Per the gNMI specification, the default timestamp field of a notification message is set to be<br>the time at which the value of the underlying data source changes or when the reported event takes place.<br>In order to facilitate integration in legacy environments oriented around polling style operations,<br>an option to support overriding the timestamp field to the send-time is available from EOS 4.27.0F.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_access_group</samp>](## "management_api_gnmi.transport.grpc.[].ip_access_group") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "management_api_gnmi.transport.grpc.[].port") | Integer |  |  |  | GNMI port.<br>Make sure to update the control-plane ACL accordingly in order for the service to be reachable by external applications.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;grpc_tunnels</samp>](## "management_api_gnmi.transport.grpc_tunnels") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].name") | String | Required, Unique |  |  | Transport name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].shutdown") | Boolean |  |  |  | Operational status of the gRPC tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_ssl_profile</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].tunnel_ssl_profile") | String |  |  |  | Tunnel SSL profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gnmi_ssl_profile</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].gnmi_ssl_profile") | String |  |  |  | gNMI SSL profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].destination.address") | String | Required |  |  | IP address or hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].destination.port") | Integer | Required |  | Min: 1<br>Max: 65535 | TCP Port. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].local_interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].local_interface.name") | String | Required |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].local_interface.port") | Integer | Required |  | Min: 1<br>Max: 65535 | TCP Port. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;target</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_serial_number</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target.use_serial_number") | Boolean |  |  |  | Use serial number as the Target ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;target_ids</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target.target_ids") | List, items: String |  |  |  | Target IDs as a list.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_api_gnmi.transport.grpc_tunnels.[].target.target_ids.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_vrfs</samp>](## "management_api_gnmi.enable_vrfs") <span style="color:red">removed</span> | List |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>transport.grpc</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;octa</samp>](## "management_api_gnmi.octa") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>provider</samp> instead.</span> |

=== "YAML"

    ```yaml
    management_api_gnmi:
      provider: <str; default="eos-native">
      transport:
        grpc:

            # Transport name.
          - name: <str; required; unique>

            # SSL profile name.
            ssl_profile: <str>

            # VRF name is optional.
            vrf: <str>

            # Per the gNMI specification, the default timestamp field of a notification message is set to be
            # the time at which the value of the underlying data source changes or when the reported event takes place.
            # In order to facilitate integration in legacy environments oriented around polling style operations,
            # an option to support overriding the timestamp field to the send-time is available from EOS 4.27.0F.
            notification_timestamp: <str; "send-time" | "last-change-time">

            # ACL name.
            ip_access_group: <str>

            # GNMI port.
            # Make sure to update the control-plane ACL accordingly in order for the service to be reachable by external applications.
            port: <int>
        grpc_tunnels:

            # Transport name.
          - name: <str; required; unique>

            # Operational status of the gRPC tunnel.
            shutdown: <bool>

            # Tunnel SSL profile name.
            tunnel_ssl_profile: <str>

            # gNMI SSL profile name.
            gnmi_ssl_profile: <str>

            # VRF name.
            vrf: <str>
            destination:

              # IP address or hostname.
              address: <str; required>

              # TCP Port.
              port: <int; 1-65535; required>
            local_interface:

              # Interface name.
              name: <str; required>

              # TCP Port.
              port: <int; 1-65535; required>
            target:

              # Use serial number as the Target ID.
              use_serial_number: <bool>

              # Target IDs as a list.
              target_ids:
                - <str>
    ```
