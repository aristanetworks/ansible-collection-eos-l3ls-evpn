# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Literal, Protocol, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.avdfacts import AvdFacts, AvdFactsProtocol

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import TypeVar

    from typing_extensions import Self

    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol

    T_StructuredConfigGeneratorSubclass = TypeVar("T_StructuredConfigGeneratorSubclass", bound="StructuredConfigGeneratorProtocol")


def structured_config_contributor(func: Callable[[T_StructuredConfigGeneratorSubclass], None]) -> Callable[[T_StructuredConfigGeneratorSubclass], None]:
    """Decorator to mark methods that contribute to the structured config."""
    func._is_structured_config_contributor = True
    return func


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


class StructuredConfigGeneratorProtocol(AvdFactsProtocol, Protocol):
    """
    Protocol for the StructuredConfigGenerator base class for structured config generators.

    This differs from AvdFacts by also taking structured_config and custom_structured_configs as argument
    and by the render function which updates the structured_config instead of
    returning a dict.
    """

    structured_config: EosCliConfigGen
    custom_structured_configs: StructCfgs
    _complete_structured_config: EosCliConfigGen
    """
    Temporary store of the complete structured config in case this module is still using the legacy duplication check.

    See render() for details.
    """

    def render(self) -> None:
        """
        In-place update the structured_config by deepmerging the rendered dict over the structured_config object.

        This method is bridging the gap between older classes which returns builtin types on all methods,
        and refactored classes which inplace updates the self.structured_config.
        """
        # This knob makes us keep the legacy behavior of maintaining a single structured config object per module and merging them.
        # Without it set, we will just in-place update the same structured_config, which means any duplication checks will be enforced across all modules.
        # Note that methods that have not been refactored to update structured_config directly will still be merged on top.
        if not self.inputs.avd_eos_designs_enforce_duplication_checks_across_all_models and not getattr(
            self, "ignore_avd_eos_designs_enforce_duplication_checks_across_all_models", False
        ):
            self._complete_structured_config = self.structured_config
            self.structured_config = EosCliConfigGen()

        # In-place update self.structured_config by calling all the refactored methods marked with @structured_config_contributor
        self.render_structured_config()

        # The render method on AvdFacts class will only execute methods with @cached_property not starting with _.
        # These are the legacy methods which will be refactored to use the @structured_config_contributor decorator instead.
        generated_structured_config_as_dict = super().render()
        if generated_structured_config_as_dict:
            generated_structured_config = EosCliConfigGen._from_dict(generated_structured_config_as_dict)
            self.structured_config._deepmerge(generated_structured_config, list_merge="append_unique")

        # If we run with the legacy behavior we now have to restore the original structured config and merge in the things we generated here.
        if not self.inputs.avd_eos_designs_enforce_duplication_checks_across_all_models and not getattr(
            self, "ignore_avd_eos_designs_enforce_duplication_checks_across_all_models", False
        ):
            module_structured_config = self.structured_config
            self.structured_config = self._complete_structured_config
            self.structured_config._deepmerge(module_structured_config, list_merge="append_unique")

    def render_structured_config(self) -> None:
        """
        Execute all class methods marked with @structured_config_contributor decorator.

        Each method will in-place update self.structured_config.
        """
        for method in self.structured_config_methods():
            method(self)

    @classmethod
    def structured_config_methods(cls) -> list[Callable[[Self], None]]:
        """Return the list of methods decorated with 'structured_config_contributor'."""
        return [method for key in cls._keys() if getattr(method := getattr(cls, key), "_is_structured_config_contributor", False)]


class StructuredConfigGenerator(AvdFacts, StructuredConfigGeneratorProtocol):
    """
    Base class for structured config generators.

    This differs from AvdFacts by also taking structured_config and custom_structured_configs as argument
    and by the render function which updates the structured_config instead of
    returning a dict.
    """

    def __init__(
        self, hostvars: dict, inputs: EosDesigns, shared_utils: SharedUtilsProtocol, structured_config: EosCliConfigGen, custom_structured_configs: StructCfgs
    ) -> None:
        self.structured_config = structured_config
        self.custom_structured_configs = custom_structured_configs
        super().__init__(hostvars=hostvars, inputs=inputs, shared_utils=shared_utils)
