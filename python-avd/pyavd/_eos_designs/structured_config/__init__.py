# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils

from .base import AvdStructuredConfigBase
from .connected_endpoints import AvdStructuredConfigConnectedEndpoints
from .core_interfaces_and_l3_edge import AvdStructuredConfigCoreInterfacesAndL3Edge
from .custom_structured_configuration import AvdStructuredConfigCustomStructuredConfiguration
from .flows import AvdStructuredConfigFlows
from .inband_management import AvdStructuredConfigInbandManagement
from .metadata import AvdStructuredConfigMetadata
from .mlag import AvdStructuredConfigMlag
from .network_services import AvdStructuredConfigNetworkServices
from .overlay import AvdStructuredConfigOverlay
from .structured_config_generator import StructCfgs
from .underlay import AvdStructuredConfigUnderlay

if TYPE_CHECKING:
    from pyavd.avd_schema_tools import AvdSchemaTools

    from .structured_config_generator import StructuredConfigGenerator

AVD_STRUCTURED_CONFIG_CLASSES: list[type[StructuredConfigGenerator]] = [
    AvdStructuredConfigBase,
    AvdStructuredConfigMlag,
    AvdStructuredConfigUnderlay,
    AvdStructuredConfigOverlay,
    AvdStructuredConfigCoreInterfacesAndL3Edge,
    AvdStructuredConfigNetworkServices,
    AvdStructuredConfigConnectedEndpoints,
    AvdStructuredConfigInbandManagement,
    # The Flows module must be rendered after others contributing interfaces,
    # since it parses those interfaces for sFlow or flow tracking (ipfix) config.
    AvdStructuredConfigFlows,
    # Metadata must be after anything else that can generate structured config, since CV tags can consume from structured config.
    AvdStructuredConfigMetadata,
    # The Custom Structured Configuration module must be rendered last,
    # since it strips empties from all previously generated structured config and then
    # applies the custom structured config snips gathered by the other generators.
    AvdStructuredConfigCustomStructuredConfiguration,
]
"""
AVD_STRUCTURED_CONFIG contains a list of AvdStructuredConfig classes which generate the complete structured config.
The order is important, since later modules can overwrite or read config created by earlier ones.
"""


def get_structured_config(
    vars: dict,  # noqa: A002
    input_schema_tools: AvdSchemaTools,
    result: dict,
    templar: object | None = None,
    *,
    validate: bool = True,
) -> dict:
    """
    Generate structured_config for a device.

    Args:
        vars:
            The variable for the device
        input_schema_tools:
            An AvdSchemaTools object used to validate the input variables if enabled.
        result:
            Dictionary to store results.
        templar:
            The templar to use for rendering templates.
        validate:
            Optional flag to disable validation for the input schema.

    Returns:
        The structured_config as a dict
    """
    # Validate input data
    if validate:
        result.update(input_schema_tools.convert_and_validate_data(vars))
        if result.get("failed"):
            # Input data validation failed so return empty dict. Calling function should check result.get("failed").
            return {}

    # Load input vars into the EosDesigns data class.
    inputs = EosDesigns._from_dict(vars)

    # Initialize SharedUtils class to be passed to each python_module below.
    shared_utils = SharedUtils(hostvars=vars, inputs=inputs, templar=templar, schema=input_schema_tools.avdschema)

    # Single structured config instance which will be in-place updated by each structured config generator.
    structured_config = EosCliConfigGen()

    # Placeholder for custom structured configs added by the structured config generators.
    # Will be applied last by AvdStructuredConfigCustomStructuredConfiguration.
    # "root" holds full device structured configs given under node-config or under VRFs. They will be applied at the root level of the final structured config.
    # "nested" is one instance of structured config merged onto during parsing of various models supporting a "structured_config" option.
    # We need these variants because the order of application is important (root first, then nested).
    #
    custom_structured_configs = StructCfgs.new_from_ansible_list_merge_strategy(inputs.custom_structured_configuration_list_merge)

    for cls in AVD_STRUCTURED_CONFIG_CLASSES:
        eos_designs_module = cls(
            hostvars=vars, inputs=inputs, shared_utils=shared_utils, structured_config=structured_config, custom_structured_configs=custom_structured_configs
        )
        eos_designs_module.render()

    return structured_config._as_dict()
