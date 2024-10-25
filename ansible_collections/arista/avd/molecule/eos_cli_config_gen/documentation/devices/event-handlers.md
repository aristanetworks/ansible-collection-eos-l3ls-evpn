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

## Monitoring

### Event Handler

#### Event Handler Summary

| Handler | Actions | Trigger | Trigger Config |
| ------- | ------- | ------- | -------------- |
| CONFIG_VERSIONING | bash <code>FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* \| tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* \| tail -n +11 \| xargs -I % rm %; fi</code> | on-startup-config | - |
| trigger-on-boot | bash <code>if [ 15 -gt 10 ]\nthen\n  echo "a is greater than 10"\nfi</code><br>increment device health metric Metric1 | on-boot | - |
| trigger-on-counters | log | on-counters | poll interval 10<br>condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )<br>granularity per-source |
| trigger-on-counters2 | - | on-counters | condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )<br>granularity per-source |
| trigger-on-counters3 | - | on-counters | - |
| trigger-on-intf | - | on-intf | trigger on-intf Ethernet4 operstatus ip ip6 |
| trigger-on-intf2 | - | on-intf | - |
| trigger-on-logging | increment device health metric Metric2 | on-logging | poll interval 10<br>regex ab* |
| trigger-on-logging2 | - | on-logging | regex ab* |
| trigger-on-logging3 | - | on-logging | - |
| trigger-on-maintenance1 | - | on-maintenance | trigger on-maintenance enter interface Management3 after stage linkdown |
| trigger-on-maintenance2 | bash <code>echo "on-maintenance"</code> | on-maintenance | trigger on-maintenance exit unit unit1 before stage bgp |
| trigger-on-maintenance3 | bash <code>echo "on-maintenance"</code> | on-maintenance | trigger on-maintenance enter bgp 10.0.0.2 vrf vrf1 all |
| trigger-on-maintenance4 | - | on-maintenance | - |
| trigger-on-maintenance5 | - | on-maintenance | - |
| trigger-vm-tracer | bash <code>echo "vm-tracer vm"</code> | vm-tracer vm | - |

#### Event Handler Device Configuration

```eos
!
event-handler CONFIG_VERSIONING
   trigger on-startup-config
   action bash FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* | tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* | tail -n +11 | xargs -I % rm %; fi
   delay 0
!
event-handler trigger-on-boot
   trigger on-boot
   action bash
      if [ 15 -gt 10 ]
      then
        echo "a is greater than 10"
      fi
      EOF
   action increment device-health metric Metric1
!
event-handler trigger-on-counters
   action log
   trigger on-counters
      poll interval 10
      condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )
      granularity per-source
!
event-handler trigger-on-counters2
   trigger on-counters
      condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )
      granularity per-source
!
event-handler trigger-on-counters3
   trigger on-counters
!
event-handler trigger-on-intf
   trigger on-intf Ethernet4 operstatus ip ip6
!
event-handler trigger-on-intf2
!
event-handler trigger-on-logging
   action increment device-health metric Metric2
   trigger on-logging
      poll interval 10
      regex ab*
!
event-handler trigger-on-logging2
   trigger on-logging
      regex ab*
!
event-handler trigger-on-logging3
   trigger on-logging
!
event-handler trigger-on-maintenance1
   trigger on-maintenance enter interface Management3 after stage linkdown
!
event-handler trigger-on-maintenance2
   trigger on-maintenance exit unit unit1 before stage bgp
   action bash echo "on-maintenance"
!
event-handler trigger-on-maintenance3
   trigger on-maintenance enter bgp 10.0.0.2 vrf vrf1 all
   action bash echo "on-maintenance"
!
event-handler trigger-on-maintenance4
!
event-handler trigger-on-maintenance5
!
event-handler trigger-vm-tracer
   trigger vm-tracer vm
   action bash echo "vm-tracer vm"
```
