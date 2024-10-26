# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import get_device_config, validate_structured_config
from pyavd._utils import get


def test_get_device_config(hostname: str, all_inputs: dict, configs: dict) -> None:
    """Test get_device_config."""
    structured_config: dict = all_inputs[hostname]
    if not get(structured_config, "eos_cli_config_gen_configuration.enable", True):
        return

    expected_config: str = configs[hostname]

    # run validation on structured_config to ensure it is converted
    validate_structured_config(structured_config)

    device_config = get_device_config(structured_config)

    assert isinstance(device_config, str)

    assert device_config == expected_config
