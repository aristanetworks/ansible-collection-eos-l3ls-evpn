# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Self

from pydantic import BaseModel, model_validator

from pyavd._anta.input_factories.protocols import AntaTestInputFactory
from pyavd._anta.lib import AntaTest, AntaTestDefinition
from pyavd._anta.utils import ConfigManager, LogMessage, StructuredConfigKey, TestLoggerAdapter
from pyavd._utils import get


class TestSpec(BaseModel):
    """TestSpec model used to define an ANTA test specification.

    The model attributes are used to create an AntaTestDefinition using the `create_test_definition` method.

    If the ANTA test requires input, either `input_factory` or `input_dict` attributes should be provided, but not both.

    Attributes:
    ----------
    test_class : type[AntaTest]
        The ANTA test class to be used for the test.
    conditional_keys : list[StructuredConfigKey] | None
        Optional structured config keys that are required to run the test.
    input_factory : type[AntaTestInputFactory] | None
        Optional input factory class that generates the `AntaTest.Input` model (inputs) for the test.
    input_dict : dict[str, StructuredConfigKey] | None
        Optional dictionary that maps the input fields to structured config keys.
        The structured config keys values will be extracted to generate the `AntaTest.Input` model (inputs) for the test.
    """

    test_class: type[AntaTest]
    conditional_keys: list[StructuredConfigKey] | None = None
    input_factory: type[AntaTestInputFactory] | None = None
    input_dict: dict[str, StructuredConfigKey] | None = None

    @model_validator(mode="after")
    def check_inputs(self) -> Self:
        """Check that the TestSpec has either an input factory or an input dict if the test requires input. Cannot have both."""
        if self.input_factory and self.input_dict:
            msg = f"TestSpec {self.test_class.name} cannot have both an input factory and an input dict."
            raise ValueError(msg)

        if "Input" in self.test_class.__dict__ and not self.input_factory and not self.input_dict:
            msg = f"TestSpec {self.test_class.name} must have an input factory or an input dict."
            raise ValueError(msg)
        return self

    def create_test_definition(self, manager: ConfigManager, logger: TestLoggerAdapter) -> AntaTestDefinition | None:
        """Create the AntaTestDefinition from this TestSpec instance."""
        # Skip the test if the conditional keys are not present in the structured config
        if self.conditional_keys and not manager.verify_keys(self.conditional_keys):
            keys = StructuredConfigKey.to_string_list(self.conditional_keys)
            logger.info(LogMessage.NO_DATA_MODEL, entity=", ".join(keys))
            return None

        # AntaTestDefinition takes `inputs=None` if the test does not require input
        inputs = None

        # Create the AntaTest.Input instance from the input dict if available
        if self.input_dict:
            rendered_inputs = {}
            for input_field, structured_config_key in self.input_dict.items():
                field_value = get(manager.structured_config, structured_config_key.value)
                if field_value is not None:
                    rendered_inputs[input_field] = field_value
                else:
                    logger.info(LogMessage.NO_DATA_MODEL, entity=structured_config_key.value)
                    return None
            inputs = self.test_class.Input(**rendered_inputs)

        # Create the AntaTest.Input instance from the input factory is available
        elif self.input_factory:
            inputs = self.input_factory.create(self.test_class, manager, logger)
            if inputs is None:
                logger.warning(LogMessage.NO_INPUTS)
                return None

        return AntaTestDefinition(test=self.test_class, inputs=inputs)
