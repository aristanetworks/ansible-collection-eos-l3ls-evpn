# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from collections import ChainMap, defaultdict

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtils

    from .execution import Execution, StructuredConfigExecutor

LOGGER = logging.getLogger(__name__)


class StructuredConfigGenerator:
    """Base class for all structured config generation classes."""

    hostvars: dict | ChainMap
    inputs: EosDesigns
    structured_config: EosCliConfigGen
    custom_structured_configurations: list[EosCliConfigGen]
    shared_utils: SharedUtils
    _cls_method_execution_registry: ClassVar[defaultdict[Execution, list[str]]]

    def __init__(
        self,
        hostvars: dict | ChainMap,
        inputs: EosDesigns,
        structured_config: EosCliConfigGen,
        custom_structured_configurations: list[EosCliConfigGen],
        shared_utils: SharedUtils,
        executor: StructuredConfigExecutor,
    ) -> None:
        """
        Structured Configuration generation class.

        Call the method run() to enerate structured config and in-place update the given structured_config (EosCliConfigGen) instance.

        Args:
            hostvars: Raw input variables - still used to get facts and exposed in some custom templating.
            inputs: EosDesigns instance containing all the inputs.
            structured_config: EosCliConfigGen instance to be updated.
                Can also be inspected to get output of previous generators.
            custom_structured_configurations: List of custom structured configurations.
                The class can either append extra structured configurations or apply them to the given structured_configuration instance.
            shared_utils: SharedUtils instance containing data to be reused between Structured Config generators.
            executor: StructuredConfigExecutor where we should register methods to be executed.
        """
        self.hostvars = hostvars
        self.inputs = inputs
        self.structured_config = structured_config
        self.custom_structured_configurations = custom_structured_configurations
        self.shared_utils = shared_utils

        # Register the methods marked for execution. The marking is done by the RegisterForExecution method decorator.
        executor.register_generator_methods(self, self._cls_method_execution_registry)
