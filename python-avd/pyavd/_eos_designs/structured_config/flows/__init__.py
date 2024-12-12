# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from itertools import chain

from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import strip_null_from_data
from pyavd.j2filters import natural_sort


class AvdStructuredConfigFlows(StructuredConfigGenerator):
    """
    Structured config for sflow and flow_tracker.

    This class must be rendered after all other eos_designs modules since it relies on
    detecting sflow from the interface structured config generated by the other modules.

    The only exception is of course custom_structured_configuration which always comes last.
    """

    @cached_property
    def sflow(self) -> dict | None:
        """
        Structured config for sFlow.

        Only configure if any interface is enabled for sFlow.

        Covers:
        - sflow_settings
        - source-interfaces based on source_interfaces.sflow
        """
        if not self._enable_sflow:
            return None

        if not (destinations := self.inputs.sflow_settings.destinations):
            msg = "`sflow_settings.destinations` is required to configure `sflow`."
            raise AristaAvdInvalidInputsError(msg)

        sflow_settings_vrfs = self.inputs.sflow_settings.vrfs

        # At this point we have at least one interface with sFlow enabled
        # and at least one destination.
        sflow = {"run": True, "sample": self.inputs.sflow_settings.sample.rate}

        # Using a temporary dict for VRFs
        sflow_vrfs = {}

        for destination in natural_sort(destinations, "destination"):
            destination: EosDesigns.SflowSettings.DestinationsItem
            vrf = destination.vrf
            if vrf is None:
                vrf = self.shared_utils.default_mgmt_protocol_vrf
                source_interface = self.shared_utils.default_mgmt_protocol_interface

            elif vrf == "use_mgmt_interface_vrf":
                if (self.shared_utils.node_config.mgmt_ip is None) and (self.shared_utils.node_config.ipv6_mgmt_ip is None):
                    msg = "Unable to configure sFlow source-interface with 'use_mgmt_interface_vrf' since 'mgmt_ip' or 'ipv6_mgmt_ip' are not set."
                    raise AristaAvdInvalidInputsError(msg)

                vrf = self.inputs.mgmt_interface_vrf
                if vrf in sflow_settings_vrfs and sflow_settings_vrfs[vrf].source_interface:
                    source_interface = sflow_settings_vrfs[vrf].source_interface
                else:
                    source_interface = self.shared_utils.mgmt_interface

            elif vrf == "use_inband_mgmt_vrf":
                # Check for missing interface
                if self.shared_utils.inband_mgmt_interface is None:
                    msg = "Unable to configure sFlow source-interface with 'use_inband_mgmt_vrf' since 'inband_mgmt_interface' is not set."
                    raise AristaAvdInvalidInputsError(msg)

                # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
                vrf = self.shared_utils.inband_mgmt_vrf or "default"
                if vrf in sflow_settings_vrfs and sflow_settings_vrfs[vrf].source_interface:
                    source_interface = sflow_settings_vrfs[vrf].source_interface
                else:
                    source_interface = self.shared_utils.inband_mgmt_interface

            # Default is none, meaning we will not configure a source interface for this VRF.
            elif vrf in sflow_settings_vrfs and sflow_settings_vrfs[vrf].source_interface:
                source_interface = sflow_settings_vrfs[vrf].source_interface
            else:
                source_interface = None

            if vrf in [None, "default"]:
                # Add destination without VRF field
                sflow.setdefault("destinations", []).append(
                    {
                        "destination": destination.destination,
                        "port": destination.port,
                    },
                )
                sflow["source_interface"] = source_interface

            else:
                # Add destination with VRF field.
                sflow_vrfs.setdefault(vrf, {}).setdefault("destinations", []).append(
                    {
                        "destination": destination.destination,
                        "port": destination.port,
                    },
                )
                sflow_vrfs[vrf]["source_interface"] = source_interface

        # convert sflow_vrfs dict into list and insert into sflow
        if sflow_vrfs:
            sflow["vrfs"] = [{"name": vrf_name, **vrf} for vrf_name, vrf in sflow_vrfs.items()]

        return strip_null_from_data(sflow)

    @cached_property
    def _enable_sflow(self) -> bool:
        """
        Enable sFlow if any interface is enabled for sFlow.

        This relies on sFlow being rendered after all other eos_designs modules (except structured config).
        """
        return any(interface.sflow.enable for interface in chain(self.structured_config.ethernet_interfaces, self.structured_config.port_channel_interfaces))

    def resolve_flow_tracker_by_type(self, tracker_settings: EosDesigns.FlowTrackingSettings.TrackersItem) -> dict:
        tracker = {
            "name": tracker_settings.name,
            "record_export": tracker_settings.record_export._as_dict(),
            "exporters": tracker_settings.exporters._as_list(),
        }
        if self.shared_utils.flow_tracking_type == "sampled":
            if (table_size := tracker_settings.sampled.table_size) is not None:
                tracker["table_size"] = table_size
            if (mpls := tracker_settings.sampled.record_export.mpls) is not None:
                tracker["record_export"]["mpls"] = mpls

        return tracker

    @cached_property
    def flow_tracking(self) -> dict | None:
        """Return structured config for flow_tracking."""
        configured_trackers = self._get_enabled_flow_trackers()
        if not configured_trackers:
            return None

        flow_tracking = {}

        tracker_type = self.shared_utils.flow_tracking_type
        global_settings = self.inputs.flow_tracking_settings.hardware if tracker_type == "hardware" else self.inputs.flow_tracking_settings.sampled
        flow_tracking[tracker_type] = global_settings._as_dict()
        if tracker_type == "sampled":
            # asdict does not contain default values so we need to insert the default sample.
            # TODO: consider if asdict should include defaults.
            flow_tracking[tracker_type]["sample"] = global_settings.sample

        filtered_trackers = []
        for tracker_name in natural_sort(configured_trackers):
            """
            We allow overriding the default flow tracker name, so if user has configured a tracker
            with the default tracker name, then we just use that, if not, we create a default config
            """
            default_tracker = next(iter(EosDesigns.FlowTrackingSettings().trackers))
            if tracker_name not in self.inputs.flow_tracking_settings.trackers:
                if tracker_name == default_tracker.name:
                    tracker = default_tracker
                else:
                    msg = f"{tracker_name} is being used for one of the interfaces, but is not configured in flow_tracking_settings"
                    raise AristaAvdInvalidInputsError(msg)
            else:
                tracker = self.inputs.flow_tracking_settings.trackers[tracker_name]

            filtered_trackers.append(self.resolve_flow_tracker_by_type(tracker))

        flow_tracking[tracker_type]["trackers"] = filtered_trackers
        flow_tracking[tracker_type]["shutdown"] = False

        return flow_tracking

    def _get_enabled_flow_trackers(self) -> set:
        """
        Enable flow-tracking if any interface is enabled for flow-tracking.

        This relies on flow-tracking being rendered after all other eos_designs modules (except structured config).
        """
        all_interfaces = chain(
            self.structured_config.ethernet_interfaces, self.structured_config.port_channel_interfaces, self.structured_config.dps_interfaces
        )
        if self.shared_utils.flow_tracking_type == "hardware":
            return {interface.flow_tracker.hardware for interface in all_interfaces if interface.flow_tracker.hardware}

        return {interface.flow_tracker.sampled for interface in all_interfaces if interface.flow_tracker.sampled}
