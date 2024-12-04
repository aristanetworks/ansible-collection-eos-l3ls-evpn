#!/usr/bin/env python3
# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._eos_designs.structured_config import STRUCTURED_CONFIG_GENERATORS
from pyavd._eos_designs.structured_config.execution import StructuredConfigExecutor
from pyavd._schema.avdschema import AvdSchema

inputs = EosDesigns()
shared_utils = SharedUtils(hostvars={}, inputs=inputs, templar=None, schema=AvdSchema(schema_id="eos_designs"))

# Created structured config executor without executing the StructuredConfigGenerator subclasses.
structured_config_instance = EosCliConfigGen()
custom_structured_configurations: list[EosCliConfigGen] = []
executor = StructuredConfigExecutor(
    hostvars={},
    inputs=inputs,
    structured_config=structured_config_instance,
    custom_structured_configurations=custom_structured_configurations,
    shared_utils=shared_utils,
    classes=STRUCTURED_CONFIG_GENERATORS,
)
print(executor.graph())
