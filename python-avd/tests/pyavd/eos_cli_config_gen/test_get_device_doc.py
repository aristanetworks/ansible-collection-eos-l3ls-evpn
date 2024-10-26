# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import get_device_doc, validate_structured_config
from pyavd._utils import get


def test_get_device_doc(hostname: str, all_inputs: dict, device_docs: dict) -> None:
    """Test get_device_config."""
    structured_config: dict = all_inputs[hostname]
    if not get(structured_config, "eos_cli_config_gen_documentation.enable", True):
        return

    # run validation on structured_config to ensure it is covered
    validate_structured_config(structured_config)

    expected_doc: str = device_docs.get(hostname, "")

    device_doc = get_device_doc(structured_config, add_md_toc=True)

    assert isinstance(device_doc, str)
    assert device_doc == expected_doc
