# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Iterable
from string import Formatter


class AvdStringFormatter(Formatter):
    """
    Custom string formatter class to provide extra protection from malicious format strings and support for prefixes and suffixes per field.

    The regular Python syntax is "{" [field_name] ["!" conversion] [":" format_spec] "}"
    This class supports "{" [field_name] ["?"] ["<" prefix] [">" suffix] ["!" conversion] [":" format_spec] "}"

    where
        ? ::= The literal ? signals that the field is optional and will not be printed if the value is missing or None.
        prefix ::= string including spaces which will be inserted before the field value.
                   Most useful in combination with ?. Prefix should not contain "<", ">", "!" or ":".
        suffix ::= string including spaces which will be inserted after the field value.
                   Most useful in combination with ?. Suffix should not contain "<", ">", "!" or ":".
        conversion ::= "!u" for "upper()" (The regular Python conversions "!r", "!s", "!a" have been removed).

    Note the order of syntax field matters!
    """

    def _vformat(self, format_string: str, args: list, kwargs: dict, used_args: set, recursion_depth: int, auto_arg_index: int = 0) -> tuple[str, int]:
        """
        Perform the actual formatting.

        Mostly a copy from the base class, but adding support for using "optional", "prefix" and "suffix" from the .parse() method.

        This should not be called directly. Instead call AvdStringFormatter().format(format_string, /, *args, **kwargs)
        """
        if recursion_depth < 0:
            msg = "Max string recursion exceeded"
            raise ValueError(msg)
        result = []
        for literal_text, org_field_name, org_format_spec, conversion, optional, prefix, suffix in self.parse(format_string):
            # Make ruff happy.
            field_name = org_field_name
            format_spec = org_format_spec

            # output the literal text
            if literal_text:
                result.append(literal_text)

            # if there's a field, output it
            if field_name is not None:
                # this is some markup, find the object and do the formatting

                # handle arg indexing when empty field_names are given.
                if field_name == "":
                    if auto_arg_index is False:
                        msg = "cannot switch from manual field specification to automatic field numbering"
                        raise ValueError(msg)
                    field_name = str(auto_arg_index)
                    auto_arg_index += 1
                elif field_name.isdigit():
                    if auto_arg_index:
                        msg = "cannot switch from manual field specification to automatic field numbering"
                        raise ValueError(msg)
                    # disable auto arg incrementing, if it gets
                    # used later on, then an exception will be raised
                    auto_arg_index = False

                # given the field_name, find the object it references
                #  and the argument it came from
                if optional:
                    try:
                        obj, arg_used = self.get_field(field_name, args, kwargs)
                    except (IndexError, KeyError):
                        # Skip this field if it is optional and not existing.
                        continue
                    if obj is None:
                        # Skip this field if it is optional and None.
                        continue
                else:
                    obj, arg_used = self.get_field(field_name, args, kwargs)

                used_args.add(arg_used)

                # do any conversion on the resulting object
                obj = self.convert_field(obj, conversion)

                # expand the format spec, if needed
                format_spec, auto_arg_index = self._vformat(format_spec, args, kwargs, used_args, recursion_depth - 1, auto_arg_index=auto_arg_index)

                # Append prefix if set
                if prefix:
                    result.append(prefix)

                # format the object and append to the result
                result.append(self.format_field(obj, format_spec))

                # Append suffix if set
                if suffix:
                    result.append(suffix)

        return "".join(result), auto_arg_index

    def parse(self, format_string: str) -> Iterable[tuple[str, str | None, str | None, str | None, bool | None, str | None, str | None]]:
        """
        Parse the format_string and yield elements back.

        Mostly a copy from the base class, but also returning "optional", "prefix" and "suffix" for every field.
        """
        for literal_text, field_name, format_spec, conversion in super().parse(format_string):
            if not field_name or not ("?" in field_name or ">" in field_name or "<" in field_name):
                yield (literal_text, field_name, format_spec, conversion, None, None, None)
                continue

            tmp_field_name = field_name
            # Doing suffix first so the split will keep a potential prefix in the tmp_field_name
            if ">" in tmp_field_name:
                tmp_field_name, suffix = tmp_field_name.split(">", maxsplit=1)
            else:
                suffix = None

            if "<" in tmp_field_name:
                tmp_field_name, prefix = tmp_field_name.split("<", maxsplit=1)
            else:
                prefix = None

            optional = tmp_field_name.endswith("?")
            tmp_field_name = tmp_field_name.removesuffix("?")

            yield (literal_text, tmp_field_name, format_spec, conversion, optional, prefix, suffix)

    def convert_field(self, value: object, conversion: str | None) -> object:
        """
        Convert the value according to the given conversion instruction.

        Mostly a copy from the base class, but only supporting !u for upper().
        """
        # TODO: !l for lowercase, !t for TitleCase and shorten interface names i.e Ethernet -> Et
        # do any conversion on the resulting object
        if conversion is None:
            return value
        if conversion == "u":
            return str(value).upper()
        msg = f"Unknown conversion specifier {conversion!s}"
        raise ValueError(msg)

    def get_field(self, field_name: str, args: list, kwargs: dict) -> tuple[object, str]:
        """
        Get field value including parsing attributes/keys.

        Reusing base class after guarding against accessing attributes leading with underscore.
        This protects against access to dunders etc.
        """
        if not field_name or "_" not in field_name:
            return super().get_field(field_name, args, kwargs)

        if any(attr.startswith("_") for attr in field_name.split(".")):
            msg = f"Unsupported field name '{field_name}'. Avoid attributes starting with underscore."
            raise ValueError(msg)
        if any(key_and_more.startswith("_") for key_and_more in field_name.split("[")):
            msg = f"Unsupported field name '{field_name}'. Avoid keys starting with underscore."
            raise ValueError(msg)

        return super().get_field(field_name, args, kwargs)
