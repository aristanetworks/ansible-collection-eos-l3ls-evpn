# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.exceptions import CVResourceNotFound
from pyavd._utils import get, get_v2
from pyavd._utils.password_utils.password import simple_7_decrypt

if TYPE_CHECKING:
    from pyavd._cv.api.arista.studio.v1 import InputSchema
    from pyavd._cv.client import CVClient

    from .models import CVDevice, CVPathfinderMetadata, DeployToCvResult

LOGGER = getLogger(__name__)

CV_PATHFINDER_METADATA_STUDIO_ID = "studio-avd-pathfinder-metadata"
CV_PATHFINDER_DEFAULT_STUDIO_INPUTS = {
    "pathfinders": [],
    "pathgroups": [],
    "regions": [],
    "routers": [],
    "vrfs": [],
}


def is_pathfinder_location_supported(studio_schema: InputSchema) -> bool:
    """Detect if pathfinder location is supported by the metadata studio."""
    pathfinder_group_fields = get_v2(studio_schema, "fields.values.pathfinderGroup.group_props.members.values")
    if pathfinder_group_fields is None:
        return False
    attributes = {"pathfinderRegion", "pathfinderAddress", "pathfinderSite"}
    return attributes.issubset(pathfinder_group_fields)


def is_avt_hop_count_supported(studio_schema: InputSchema) -> bool:
    """Detect if AVT hop count is supported by the metadata studio."""
    return bool(get_v2(studio_schema, "fields.values.avtHopCount"))


def is_internet_exit_zscaler_supported(studio_schema: InputSchema) -> bool:
    """Detect if zscaler internet exit is supported by the metadata studio."""
    return bool(get_v2(studio_schema, "fields.values.zscaler"))


def is_applications_supported(studio_schema: InputSchema) -> bool:
    """Detect if applications is supported by the metadata studio."""
    return bool(get_v2(studio_schema, "fields.values.applications"))


def is_zscaler_tunnel_key_encryption_supported(studio_schema: InputSchema) -> bool:
    """Detect if zscaler tunnel key encryption is supported by the metadata studio."""
    return bool(get_v2(studio_schema, "fields.values.zscalerPresharedKeyRef"))


def is_zscaler_tunnel_endpoint_supported(studio_schema: InputSchema) -> bool:
    """Detect if zscaler tunnel endpoint key is supported by the metadata studio."""
    return bool(get_v2(studio_schema, "fields.values.serviceNodeEndpoint"))


async def get_metadata_studio_schema(result: DeployToCvResult, cv_client: CVClient) -> InputSchema | None:
    """
    Download and return the input schema for the cv pathfinder metadata studio.

    Returns None if the metadata studio is not found.
    """
    try:
        studio = await cv_client.get_studio(CV_PATHFINDER_METADATA_STUDIO_ID, result.workspace.id)
    except CVResourceNotFound:
        warning = "deploy_cv_pathfinder_metadata_to_cv: Did not find metadata studio."
        LOGGER.info(warning)
        result.warnings.append(warning)
        return None

    studio_schema: InputSchema = studio.input_schema
    studio_version = get_v2(studio_schema, "fields.values.studioVersion.string_props.default_value")
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Found metadata studio version: %s", studio_version)
    return studio_schema


def update_general_metadata(metadata: dict, studio_inputs: dict, studio_schema: InputSchema) -> list[str]:
    """In-place update general metadata in studio_inputs."""
    warnings = []

    # Temporary fix for default values in metadata studio
    for vrf in get(metadata, "vrfs", default=[]):
        for avt in get(vrf, "avts", default=[]):
            constraints: dict = avt.setdefault("constraints", {})
            constraints.setdefault("latency", 4294967295)
            constraints.setdefault("jitter", 4294967295)
            constraints["lossrate"] = float(constraints.get("lossrate", 99.0))
            if is_avt_hop_count_supported(studio_schema):
                constraints["hopCount"] = constraints.pop("hop_count", "")
            elif constraints.pop("hop_count", ""):
                # hop count is set but not supported by metadata studio.
                warning = "deploy_cv_pathfinder_metadata_to_cv: Ignoring AVT hop-count information since it is not supported by metadata studio."
                LOGGER.info(warning)
                warnings.append(warning)
            if avt_app_profiles := avt.pop("application_profiles", None):
                if is_applications_supported(studio_schema):
                    avt["applicationProfiles"] = avt_app_profiles
                else:
                    # application_profiles are set but not supported by metadata studio.
                    warning = "deploy_cv_pathfinder_metadata_to_cv: Ignoring AVT application-profiles information since it is not supported by metadata studio."
                    LOGGER.info(warning)
                    warnings.append(warning)

    studio_inputs.update(
        {
            "pathgroups": [
                {
                    "carriers": get(pathgroup, "carriers", default=[]),
                    "importedCarriers": get(pathgroup, "imported_carriers", default=[]),
                    "name": get(pathgroup, "name", required=True),
                }
                for pathgroup in get(metadata, "pathgroups", default=[])
            ],
            "regions": get(metadata, "regions", default=[]),
            "vrfs": get(metadata, "vrfs", default=[]),
        },
    )

    if applications := generate_applications_metadata(metadata):
        if not is_applications_supported(studio_schema):
            warning = "deploy_cv_pathfinder_metadata_to_cv: Ignoring application_traffic_recognition information since it is not supported by metadata studio."
            LOGGER.info(warning)
            warnings.append(warning)
        else:
            studio_inputs["applications"] = applications

    return warnings


def upsert_pathfinder(metadata: dict, device: CVDevice, studio_inputs: dict, studio_schema: InputSchema) -> list[str]:
    """
    In-place insert / update metadata for one pathfinder device in studio_inputs.

    Returns any warnings raised.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: upsert_pathfinder %s", device.hostname)

    warnings = []

    pathfinder_metadata = {
        "inputs": {
            "value": {
                "sslProfileName": metadata.get("ssl_profile", ""),
                "vtepIp": metadata.get("vtep_ip", ""),
                "wanInterfaces": [
                    {
                        "inputs": {
                            "details": {
                                "carrier": interface.get("carrier", ""),
                                "circuitId": interface.get("circuit_id", ""),
                                "pathgroup": interface.get("pathgroup", ""),
                                "publicIp": interface.get("public_ip", ""),
                            },
                        },
                        "tags": {"query": f"interface:{interface.get('name', '')}@{device.serial_number}"},
                    }
                    for interface in metadata.get("interfaces", [])
                ],
            },
        },
        "tags": {"query": f"device:{device.serial_number}"},
    }

    pathfinder_location = {key: metadata.get(key) for key in ("region", "site", "address")}
    if any(pathfinder_location):
        if is_pathfinder_location_supported(studio_schema):
            pathfinder_metadata["inputs"]["value"].update(pathfinder_location)
        else:
            warning = "deploy_cv_pathfinder_metadata_to_cv: Ignoring Pathfinder location information since it is not supported by the metadata studio."
            LOGGER.info(warning)
            warnings.append(warning)

    found_index = None
    for index, router in enumerate(studio_inputs.get("pathfinders", [])):
        if get(router, "tags.query") == f"device:{device.serial_number}":
            found_index = index
            break

    if found_index is None:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: New pathfinder device, adding %s", device.hostname)
        studio_inputs.setdefault("pathfinders", []).append(pathfinder_metadata)
    else:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Existing pathfinder device, updating %s", device.hostname)
        studio_inputs["pathfinders"][found_index] = pathfinder_metadata

    return warnings


def upsert_edge(metadata: dict, device: CVDevice, studio_inputs: dict, studio_schema: InputSchema) -> list[str]:
    """
    In-place insert / update metadata for one edge device in studio_inputs.

    Returns any warnings raised.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: upsert_edge %s", device.hostname)

    warnings = []
    edge_metadata = {
        "inputs": {
            "router": {
                "sslProfileName": metadata.get("ssl_profile", ""),
                "pathfinders": [{"vtepIp": pathfinder["vtep_ip"]} for pathfinder in metadata.get("pathfinders", [])],
                "region": metadata.get("region", ""),
                "role": metadata.get("role", ""),
                "site": metadata.get("site", ""),
                "vtepIp": metadata.get("vtep_ip", ""),
                "wanInterfaces": [
                    {
                        "inputs": {
                            "details": {
                                "carrier": interface.get("carrier", ""),
                                "circuitId": interface.get("circuit_id", ""),
                                "pathgroup": interface.get("pathgroup", ""),
                            },
                        },
                        "tags": {"query": f"interface:{interface.get('name', '')}@{device.serial_number}"},
                    }
                    for interface in metadata.get("interfaces", [])
                ],
                "zone": metadata.get("zone", ""),
            },
        },
        "tags": {"query": f"device:{device.serial_number}"},
    }
    internet_exit_metadata, ie_warnings = generate_internet_exit_metadata(metadata, device, studio_schema)
    warnings.extend(ie_warnings)
    if internet_exit_metadata:
        edge_metadata["inputs"]["router"]["services"] = internet_exit_metadata

    found_index = None
    for index, router in enumerate(studio_inputs.get("routers", [])):
        if get(router, "tags.query") == f"device:{device.serial_number}":
            found_index = index
            break

    if found_index is None:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: New edge/transit device, adding %s", device.hostname)
        studio_inputs.setdefault("routers", []).append(edge_metadata)
    else:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Existing edge/transit device, updating %s", device.hostname)
        studio_inputs["routers"][found_index] = edge_metadata

    return warnings


async def deploy_cv_pathfinder_metadata_to_cv(cv_pathfinder_metadata: list[CVPathfinderMetadata], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy given CV Pathfinder metadata.

    The given metadata is parsed and updated onto the existing metadata studio inputs.

    TODO: Remove stale metadata - not sure how to deduct this.

    Example of metadata for an edge (below metadata.cv_pathfinder in structured config):
    ```yaml
    ---
    pathfinders:
      - public_ip: 10.2.3.4
    region: EMEA
    role: "transit region"
    site: Paris
    ssl_profile: VERYSAFE
    vtep_ip: 10.10.10.10
    interfaces:
      - name: Ethernet1
        carrier: BT
        circuit_id: ABC123
        pathgroup: INET
    zone: EU
    ```

    Example of metadata for a pathfinder (below metadata.cv_pathfinder in structured config):
    ```yaml
    ---
    role: pathfinder
    ssl_profile: VERYSAFE
    vtep_ip: 10.0.1.1
    interfaces:
      - carrier: BT
        circuit_id: XYZ987
        name: Ethernet2
        pathgroup: INET
        public_ip: 10.2.3.4
    pathgroups:
      - carriers:
          - name: BT
        imported_carriers:
          - name: 5GLTE
        name: INET
    regions:
      - id: 1
        name: EMEA
        zones:
          - id: 1
            name: DefaultZone
            sites:
              - id: 1
                name: Paris
                location: 99, rue de Rivoli, 75001 Paris
    vrfs:
      - avts:
          - constraints:
              jitter: 50
              latency: 200
              lossrate: 0.1
            description: Voice AVT
            id: 1
            name: Voice
            pathgroups:
              - name: INET
                preference: preferred
              - name: BACKUP
                preference: alternate
        name: HR
        vni: 100
    ```
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Got cv_pathfinder_metadata for %s devices", len(cv_pathfinder_metadata))

    if not cv_pathfinder_metadata:
        return

    if (studio_schema := await get_metadata_studio_schema(result, cv_client)) is None:
        return

    # Get existing studio inputs
    existing_studio_inputs = await cv_client.get_studio_inputs(
        studio_id=CV_PATHFINDER_METADATA_STUDIO_ID,
        workspace_id=result.workspace.id,
        default_value=CV_PATHFINDER_DEFAULT_STUDIO_INPUTS,
    )
    studio_inputs = deepcopy(existing_studio_inputs)

    # Walk through given metadata, skip missing devices or invalid roles.
    # Sort between edges (including transit) and pathfinders
    edges: list[CVPathfinderMetadata] = []
    pathfinders: list[CVPathfinderMetadata] = []
    for device_metadata in cv_pathfinder_metadata:
        if not device_metadata.device._exists_on_cv:
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Skipping metadata for device '%s' since the device is not found on CV.",
                device_metadata.device.serial_number,
            )
            result.skipped_cv_pathfinder_metadata.append(device_metadata)
            continue

        device_role = get(device_metadata.metadata, "role")

        if device_role in ["edge", "transit region"]:
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Adding metadata for device '%s' as role '%s'.",
                device_metadata.device.serial_number,
                device_role,
            )
            edges.append(device_metadata)
        elif device_role == "pathfinder":
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Adding metadata for device '%s' as role '%s'.",
                device_metadata.device.serial_number,
                device_role,
            )
            pathfinders.append(device_metadata)
        else:
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Skipping metadata for device '%s' since role '%s' is not supported.",
                device_metadata.device.serial_number,
                device_role,
            )
            result.skipped_cv_pathfinder_metadata.append(device_metadata)
            continue

    if pathfinders:
        # All pathfinders must have the same be general metadata, so we just set it in the studio based on the first one.
        result.warnings.extend(update_general_metadata(metadata=pathfinders[0].metadata, studio_inputs=studio_inputs, studio_schema=studio_schema))

    for pathfinder in pathfinders:
        result.warnings.extend(
            upsert_pathfinder(metadata=pathfinder.metadata, device=pathfinder.device, studio_inputs=studio_inputs, studio_schema=studio_schema),
        )

    for edge in edges:
        result.warnings.extend(upsert_edge(metadata=edge.metadata, device=edge.device, studio_inputs=studio_inputs, studio_schema=studio_schema))

    if studio_inputs != existing_studio_inputs:
        await cv_client.set_studio_inputs(studio_id=CV_PATHFINDER_METADATA_STUDIO_ID, workspace_id=result.workspace.id, inputs=studio_inputs)

    result.deployed_cv_pathfinder_metadata.extend(pathfinders + edges)


def generate_internet_exit_metadata(metadata: dict, device: CVDevice, studio_schema: InputSchema) -> tuple[dict, list[str]]:
    """
    Generate internet-exit related metadata for one device.

    To be inserted into edge router metadata under "services".

    Returns metadata dict and list of any warnings raised.
    """
    if (internet_exit_policies := get(metadata, "internet_exit_policies")) is None:
        LOGGER.debug("deploy_cv_pathfinder_metadata_to_cv: Did not find 'internet_exit_policies' for device: %s", device.hostname)
        return {}, []

    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Found %s 'internet_exit_policies' for device: %s", len(internet_exit_policies), device.hostname)

    services_dict = {}
    warnings = []

    for internet_exit_policy in internet_exit_policies:
        # We currently only support "zscaler" and ignore "direct".
        if internet_exit_policy.get("type") not in ["zscaler", "direct"]:
            warning = (
                f"deploy_cv_pathfinder_metadata_to_cv: Ignoring unsupported internet exit policy '{internet_exit_policies.get('name')}' "
                f"with type '{internet_exit_policy.get('type')}' for device: {device.hostname}."
            )
            LOGGER.info(warning)
            warnings.append(warning)
            continue

        if internet_exit_policy["type"] == "direct":
            # No metadata needed for direct internet-exit.
            continue

        if not is_internet_exit_zscaler_supported(studio_schema):
            warning = "deploy_cv_pathfinder_metadata_to_cv: Ignoring Zscaler internet-exit information since it is not supported by metadata studio."
            LOGGER.info(warning)
            warnings.append(warning)
            continue

        policy_name = internet_exit_policy["name"]
        services_dict.setdefault("zscaler", {"locations": [], "tunnels": []})

        zscaler_location = {
            "name": f"{device.hostname}_{policy_name}",
            "description": f"Location corresponding to {device.hostname} for internet-exit policy {policy_name}.",
            "city": internet_exit_policy["city"],
            "country": internet_exit_policy["country"],
            "uploadBandwidth": internet_exit_policy.get("upload_bandwidth"),
            "downloadBandwidth": internet_exit_policy.get("download_bandwidth"),
            "firewallEnabled": internet_exit_policy["firewall"],
            "ipsControl": internet_exit_policy["ips_control"],
            "aupEnabled": internet_exit_policy["acceptable_use_policy"],
            "vpnCredentials": [],
        }

        for vpn_credential in internet_exit_policy["vpn_credentials"]:
            zscaler_vpn_credential = {
                "fqdn": vpn_credential["fqdn"],
                "comments": f"Credential for {device.hostname} internet-exit policy {policy_name}",
                "vpnType": vpn_credential["vpn_type"],
            }
            if is_zscaler_tunnel_key_encryption_supported(studio_schema):
                zscaler_vpn_credential.update({"presharedKey": vpn_credential["pre_shared_key"], "secretServiceRef": "encrypted"})
            else:
                zscaler_vpn_credential["presharedKey"] = simple_7_decrypt(vpn_credential["pre_shared_key"])

            zscaler_location["vpnCredentials"].append(zscaler_vpn_credential)

        services_dict["zscaler"]["locations"].append(zscaler_location)

        for tunnel in internet_exit_policy["tunnels"]:
            zscaler_tunnel = {"name": tunnel["name"], "preference": tunnel["preference"]}
            if is_zscaler_tunnel_endpoint_supported(studio_schema):
                zscaler_tunnel["endpoint"] = {
                    "ipAddress": tunnel["endpoint"]["ip_address"],
                    "dcName": tunnel["endpoint"]["datacenter"],
                    "city": tunnel["endpoint"]["city"],
                    "country": tunnel["endpoint"]["country"],
                    "region": tunnel["endpoint"]["region"],
                    "latitude": float(tunnel["endpoint"]["latitude"]),
                    "longitude": float(tunnel["endpoint"]["longitude"]),
                }
            services_dict["zscaler"]["tunnels"].append(zscaler_tunnel)

    return services_dict, warnings


def generate_applications_metadata(metadata: dict) -> dict:
    """
    Generate application traffic recognition related metadata for one patfinder.

    To be inserted into the common metadata under "applications".
    """
    if (applications := get(metadata, "applications")) is None:
        return {}

    return {
        "appProfiles": [
            {
                "name": profile["name"],
                "builtinApps": get(profile, "builtin_applications"),
                "userDefinedApps": get(profile, "user_defined_applications"),
                "categories": get(profile, "categories"),
                "transportProtocols": get(profile, "transport_protocols"),
            }
            for profile in get(applications, "profiles", default=[])
        ],
        "appCategories": {
            "builtinApps": [
                {
                    "appName": application["name"],
                    "category": application["category"],
                    "service": get(application, "service"),
                }
                for application in get(applications, "builtin_applications", default=[])
            ],
            "userDefinedApps": [
                {
                    "appName": application["name"],
                    "category": application["category"],
                }
                for application in get(applications, "user_defined_applications", default=[])
            ],
        },
    }
