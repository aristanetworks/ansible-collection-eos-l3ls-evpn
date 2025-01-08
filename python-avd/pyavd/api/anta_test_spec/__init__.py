# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, model_validator

from pyavd._anta.constants import StructuredConfigKey
from pyavd._anta.input_factories._base_classes import AntaTestInputFactory
from pyavd._anta.lib import AntaTest

if TYPE_CHECKING:
    from typing_extensions import Self


class TestSpec(BaseModel):
    """TestSpec model used to define an ANTA test specification in PyAVD.

    Primarily used in the `PYAVD_TEST_INDEX` list to define the ANTA tests to be run
    but can also be provided in the `get_device_anta_catalog` PyAVD function to add custom tests.

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
            msg = f"TestSpec {self.test_class.name} cannot have both `input_factory` and `input_dict`."
            raise ValueError(msg)

        if "Input" in self.test_class.__dict__ and not self.input_factory and not self.input_dict:
            msg = f"TestSpec {self.test_class.name} must have `input_factory or `input_dict`."
            raise ValueError(msg)

        return self
