# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Literal, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.avdfacts import AvdFacts

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtils


@dataclass
class StructCfgs:
    """
    Snips of structured config gathered during structured config generation.

    The snips comes from the `structured_config` input fields in various data models.
    """

    root: list[EosCliConfigGen] = field(default_factory=list)
    nested: EosCliConfigGen = field(default_factory=EosCliConfigGen)
    list_merge_strategy: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique"

    @classmethod
    def new_from_ansible_list_merge_strategy(cls, ansible_strategy: Literal["replace", "append", "keep", "prepend", "append_rp", "prepend_rp"]) -> StructCfgs:
        merge_strategy_map = {
            "append_rp": "append_unique",
            "prepend_rp": "prepend_unique",
        }
        list_merge_strategy = merge_strategy_map.get(ansible_strategy, ansible_strategy)
        if list_merge_strategy not in ["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"]:
            msg = f"Unsupported list merge strategy: {ansible_strategy}"
            raise ValueError(msg)

        list_merge_strategy = cast(Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"], list_merge_strategy)
        return cls(list_merge_strategy=list_merge_strategy)


class StructuredConfigGenerator(AvdFacts):
    """
    Base class for structured config generators.

    This differs from AvdFacts by also taking structured_config and custom_structured_configs as argument
    and by the render function which updates the structured_config instead of
    returning a dict.
    """

    structured_config: EosCliConfigGen
    custom_structured_configs: StructCfgs

    def __init__(
        self, hostvars: dict, inputs: EosDesigns, shared_utils: SharedUtils, structured_config: EosCliConfigGen, custom_structured_configs: StructCfgs
    ) -> None:
        self.structured_config = structured_config
        self.custom_structured_configs = custom_structured_configs
        super().__init__(hostvars=hostvars, inputs=inputs, shared_utils=shared_utils)

    def render(self) -> None:
        """
        In-place update the structured_config by deepmerging the rendered dict over the structured_config object.

        This method is bridging the gap between older classes which returns builtin types on all methods,
        and refactored classes which returns AVD schema class instances. The _from_dict will automatically convert as needed.
        """
        generated_structured_config_as_dict = super().render()
        generated_structured_config = EosCliConfigGen._from_dict(generated_structured_config_as_dict)
        self.structured_config._deepmerge(generated_structured_config, list_merge="append_unique")
