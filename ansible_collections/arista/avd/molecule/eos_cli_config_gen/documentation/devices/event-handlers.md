# event-handlers

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Event Handler](#event-handler)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

## Monitoring

### Event Handler

#### Event Handler Summary

| Handler | Action Type | Action | Trigger |
| ------- | ----------- | ------ | ------- |
| CONFIG_VERSIONING | bash | <code>FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* \| tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* \| tail -n +11 \| xargs -I % rm %; fi</code> | on-startup-config |
| evpn-blacklist-recovery | bash | <code>FastCli -p 15 -c "clear bgp evpn host-flap"</code> | on-logging |
| trigger-on-boot | bash | <code>echo "on-boot"</code> | on-boot |
| trigger-on-maintenance1 | bash | <code>echo "on-maintenance"</code> | on-maintenance |
| trigger-on-maintenance2 | bash | <code>echo "on-maintenance"</code> | on-maintenance |
| trigger-on-maintenance3 | bash | <code>echo "on-maintenance"</code> | on-maintenance |

#### Event Handler Device Configuration

```eos
!
event-handler CONFIG_VERSIONING
   trigger on-startup-config
   action bash FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* | tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* | tail -n +11 | xargs -I % rm %; fi
   delay 0
!
event-handler evpn-blacklist-recovery
   trigger on-logging
      regex EVPN-3-BLACKLISTED_DUPLICATE_MAC
   action bash FastCli -p 15 -c "clear bgp evpn host-flap"
   delay 300
   asynchronous
!
event-handler trigger-on-boot
   trigger on-boot
   action bash echo "on-boot"
!
event-handler trigger-on-maintenance1
   trigger on-maintenance enter interface Management3 after stage linkdown
   action bash echo "on-maintenance"
!
event-handler trigger-on-maintenance2
   trigger on-maintenance enter unit unit1 before stage bgp
   action bash echo "on-maintenance"
!
event-handler trigger-on-maintenance3
   trigger on-maintenance enter bgp 10.0.0.2 vrf vrf1 all
   action bash echo "on-maintenance"
```
