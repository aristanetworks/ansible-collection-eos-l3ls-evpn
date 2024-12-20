# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections import ChainMap


def get_device_structured_config(hostname: str, inputs: dict, avd_facts: dict) -> dict:
    """
    Build and return the AVD structured configuration for one device.

    Args:
        hostname: Hostname of device.
        inputs: Dictionary with inputs for "eos_designs".
            Variables should be converted and validated according to AVD `eos_designs` schema first using `pyavd.validate_inputs`.
        avd_facts: Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.

    Returns:
        Device Structured Configuration as a dictionary
    """
    # pylint: disable=import-outside-toplevel
    from ._eos_designs.structured_config import get_structured_config
    from ._errors import AristaAvdError
    from .avd_schema_tools import AvdSchemaTools
    from .constants import EOS_DESIGNS_SCHEMA_ID

    # pylint: enable=import-outside-toplevel
    #
    # Set 'inventory_hostname' on the input hostvars, to keep compatibility with Ansible focused code.
    # Also map in avd_facts without touching the hostvars
    mapped_hostvars = ChainMap(
        {
            "inventory_hostname": hostname,
            "switch": avd_facts["avd_switch_facts"][hostname]["switch"],
        },
        avd_facts,
        inputs,
    )

    input_schema_tools = AvdSchemaTools(schema_id=EOS_DESIGNS_SCHEMA_ID)
    result = {}

    # We do not validate input variables in this stage (done in "validate_inputs")
    structured_config = get_structured_config(
        vars=mapped_hostvars,
        input_schema_tools=input_schema_tools,
        result=result,
        templar=None,
        validate=False,
    )
    if result.get("failed"):
        msg = f"{[str(error) for error in result['errors']]}"
        raise AristaAvdError(msg)

    return structured_config
