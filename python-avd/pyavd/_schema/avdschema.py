# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pyavd._errors import AristaAvdError, AvdSchemaError

from .avddataconverter import AvdDataConverter
from .avdvalidator import AvdValidator
from .store import create_store

if TYPE_CHECKING:
    from collections.abc import Generator

DEFAULT_SCHEMA = {
    "type": "dict",
    "allow_other_keys": True,
}


class AvdSchema:
    """
    AvdSchema takes either a schema as dict or the ID of a builtin schema.

    If none of them are set, a default "dummy" schema will be loaded.
    schema -> schema_id -> DEFAULT_SCHEMA.

    Parameters
    ----------
    schema : dict
        AVD Schema as dictionary. Will be validated towards AVD_META_SCHEMA.
    schema_id : str
        ID of AVD Schema. Either 'eos_cli_config_gen' or 'eos_designs'
    load_store_from_yaml : bool
        Force loading the YAML schema files into the store. By default schemas are loaded from pickled files.
    """

    def __init__(self, schema: dict | None = None, schema_id: str | None = None, load_store_from_yaml: bool = False) -> None:
        self.store = create_store(load_from_yaml=load_store_from_yaml)
        self.load_schema(schema, schema_id)

    def load_schema(self, schema: dict | None = None, schema_id: str | None = None) -> None:
        """
        Load schema from dict or the ID of a builtin schema.

        If none of them are set, a default "dummy" schema will be loaded.
        schema -> schema_id -> DEFAULT_SCHEMA.

        Parameters
        ----------
        schema : dict, optional
            AVD Schema as dictionary. Will be validated towards AVD_META_SCHEMA.
        schema_id : str, optional
            ID of AVD Schema. Either 'eos_cli_config_gen' or 'eos_designs'
        """
        if not schema and schema_id:
            if schema_id not in self.store:
                msg = f"Schema id {schema_id} not found in store. Must be one of {self.store.keys()}"
                raise AristaAvdError(msg)

            schema = self.store[schema_id]
        elif not schema:
            schema = DEFAULT_SCHEMA

        self._schema = schema
        try:
            self._validator = AvdValidator(schema)
            self._dataconverter = AvdDataConverter(schema)
        except Exception as e:
            msg = "An error occurred during creation of the validator"
            raise AristaAvdError(msg) from e

    def validate(self, data: Any) -> Generator:
        yield from self._validator.validate(data)

    def convert(self, data: Any) -> Generator:
        yield from self._dataconverter.convert_data(data)

    def subschema(self, datapath: list) -> dict:
        """
        Takes datapath elements as a list and returns the subschema for this datapath.

        Example:
        -------
        Data model:
        a:
          b:
            - c: 1
            - c: 2

        Schema:
        a:
          type: dict
          keys:
            b:
              type: list
              primary_key: c
              items:
                type: dict
                keys:
                  c:
                    type: str

        subschema(['a', 'b'])
        >> {"type": "list", "primary_key": "c", "items": {"type": "dict", "keys": {"c": {"type": "str"}}}}

        subschema(['a', 'b', 'c'])
        >> {"type": "str"}

        subschema(['a', 'b', 'c', 'd'])
        >> raises AvdSchemaError

        subschema([])
        >> self._schema (the loaded schema)

        subschema([], <myschema>)
        >> <myschema>

        subschema(None)
        >> raises AvdSchemaError

        subschema(['a'], <invalid_schema>)
        >> raises AvdSchemaError
        """
        if not isinstance(datapath, list):
            msg = f"The datapath argument must be a list. Got {type(datapath)}"
            raise AvdSchemaError(msg)

        schema = self._schema

        def recursive_function(datapath: list, schema: dict) -> dict:
            """Walk through schema following the datapath."""
            if len(datapath) == 0:
                return schema

            # More items in datapath, so we run recursively with recursive_function
            key = datapath[0]
            if not isinstance(key, str):
                msg = f"All datapath items must be strings. Got {type(key)}"
                raise AvdSchemaError(msg)

            if schema["type"] == "dict":
                if key in schema.get("keys", []):
                    return recursive_function(datapath[1:], schema["keys"][key])
                if key in schema.get("dynamic_keys", []):
                    return recursive_function(datapath[1:], schema["dynamic_keys"][key])

            if schema["type"] == "list" and key in schema.get("items", {}).get("keys", []):
                return recursive_function(datapath[1:], schema["items"]["keys"][key])

            # Falling through here in case the schema is not covering the requested datapath
            msg = f"The datapath '{datapath}' could not be found in the schema"
            raise AvdSchemaError(msg, path=datapath)

        return recursive_function(datapath, schema)

    def get_default_value(self, datapath: list) -> Any:
        """Return the default value of a key given the datapath as a list.

        Raises:
        -------
          AvdSchemaError if no default value is defined.
        """
        if "default" not in (subschema := self.subschema(datapath)):
            msg = f"The datapath '{datapath}' does not have a default value"
            raise AvdSchemaError(msg)
        return subschema["default"]
