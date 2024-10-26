# monitor-telemetry-influx

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [InfluxDB Telemetry](#influxdb-telemetry)
  - [InfluxDB Telemetry Summary](#influxdb-telemetry-summary)
  - [InfluxDB Telemetry Device Configuration](#influxdb-telemetry-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

## InfluxDB Telemetry

### InfluxDB Telemetry Summary

Source Group Standard Disabled : True

#### InfluxDB Telemetry Destinations

| Destination | Database | URL | VRF | Username |
| ----------- | -------- | --- | --- | -------- |
| test | test | https://influx_test.localhost | test | test |
| test1 | test1 | https://influx_test1.localhost | test | test1 |

#### InfluxDB Telemetry Sources

| Source Name | URL | Connection Limit |
| ----------- | --- | ---------------- |
| socket1 | unix:///var/run/example2.sock | 100 |
| socket2 | unix:///var/run/example3.sock | 22222 |

#### InfluxDB Telemetry Tags

| Tag | Value |
| --- | ----- |
| tag1 | value1 |
| tag2 | value2 |

### InfluxDB Telemetry Device Configuration

```eos
!
monitor telemetry influx
   destination influxdb test
      url https://influx_test.localhost
      database name test
      retention policy test
      vrf test
      username test password 7 <removed>
   !
   destination influxdb test1
      url https://influx_test1.localhost
      database name test1
      retention policy test1
      vrf test
      username test1 password 7 <removed>
   !
   source socket socket1
      url unix:///var/run/example2.sock
      connection limit 100
   !
   source socket socket2
      url unix:///var/run/example3.sock
      connection limit 22222
   tag global tag1 value1
   tag global tag2 value2
   source group standard disabled
```
