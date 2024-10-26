# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import validate_structured_config
from pyavd._errors import AvdValidationError
from pyavd.avd_schema_tools import AvdSchemaTools

SCHEMA = AvdSchemaTools(schema_id="eos_cli_config_gen").avdschema._schema


def test_validate_structured_config_with_valid_data(hostname: str, structured_configs: dict) -> None:
    """Test validate_structured_config."""
    structured_config = structured_configs[hostname]
    validation_result = validate_structured_config(structured_config)
    assert hostname
    assert validation_result.validation_errors == []
    assert hostname
    assert validation_result.failed is False


def test_validate_structured_config_with_invalid_data(hostname: str, structured_configs: dict) -> None:
    """Test validate_structured_config."""
    structured_config = structured_configs[hostname]

    updated = False
    # Insert a bad key in a random dict (making sure the dict is covered by the schema)
    for key, value in structured_config.items():
        if not isinstance(value, dict) or "structured_config" in key or key not in SCHEMA["keys"]:
            continue
        value.update({"invalid_key": "some_value"})
        updated = True
        break

    # No dict found, so we insert our own instead
    if not updated:
        structured_config.update({"router_bgp": {"invalid_key": "some_value"}})

    validation_result = validate_structured_config(structured_config)
    assert validation_result.failed is True
    assert len(validation_result.validation_errors) >= 1
    assert isinstance(validation_result.validation_errors[0], AvdValidationError)
    assert "invalid_key" in str(validation_result.validation_errors[0])
