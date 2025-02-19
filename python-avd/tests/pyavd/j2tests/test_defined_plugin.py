# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import warnings
from typing import Any

import pytest
from jinja2.runtime import Undefined

from pyavd.j2tests.defined import defined

VALUE_LIST = ["ab", None, 1, True, {"key": "value"}]
TEST_VALUE_LIST = [None, "ab", True, 1, True]
FAIL_ACTION_LIST = ["warning", "error"]
VAR_NAME_LIST = ["ab", None, 1]
VAR_TYPE_LIST = ["int", "str", "integer", "aaa", None, dict]
INVALID_FAIL_ACTION_LIST = [None, "aaaa"]


class TestDefinedPlugin:
    def defined_function(
        self,
        value: Any,
        test_value: Any = None,
        var_type: str | None = None,
        fail_action: str | None = None,
        var_name: str | None = None,
        err_msg: str | None = None,
        warn_msg: str | None = None,
    ) -> None:
        if str(fail_action).lower() == "warning":
            with warnings.catch_warnings(record=True) as w:
                resp, warning = defined(value, test_value=test_value, var_type=var_type, fail_action=fail_action, var_name=var_name, run_tests=True)
            assert len(w) == 1
            assert isinstance(w[0].message, UserWarning)
            if warn_msg:
                assert warning is not None
                warn = str(next(iter(warning.keys()))).replace("[WARNING]: ", "").strip().replace("\n", " ")
                assert warn == warn_msg
                assert str(w[0].message) == warn_msg
            assert resp is False
        elif str(fail_action).lower() == "error":
            with pytest.raises(ValueError) as e:  # noqa: PT011
                resp, warning = defined(value, test_value=test_value, var_type=var_type, fail_action=fail_action, var_name=var_name, run_tests=True)
            assert str(e.value) == err_msg

    @pytest.mark.parametrize("value", VALUE_LIST)
    @pytest.mark.parametrize("fail_action", FAIL_ACTION_LIST)
    @pytest.mark.parametrize("var_name", VAR_NAME_LIST)
    def test_defined_plugin_value_undefined_or_none(self, value: Any, fail_action: str | None, var_name: str | None) -> None:
        if isinstance(value, Undefined) or value is None:
            if str(fail_action).lower() == "warning":
                if var_name is not None:
                    warn_msg = f"{var_name} was expected but not set. Output may be incorrect or incomplete!"
                else:
                    warn_msg = "A variable was expected but not set. Output may be incorrect or incomplete!"

                self.defined_function(value, fail_action=fail_action, var_name=var_name, warn_msg=warn_msg)
            elif str(fail_action).lower() == "error":
                err_msg = f"{var_name} was expected but not set!" if var_name is not None else "A variable was expected but not set!"

                self.defined_function(value, fail_action=fail_action, var_name=var_name, err_msg=err_msg)

    @pytest.mark.parametrize("value", VALUE_LIST)
    def test_defined_plugin_value_not_none_and_define(self, value: Any) -> None:
        if not isinstance(value, Undefined) and value is not None:
            resp = defined(value)
            assert resp is True

    @pytest.mark.parametrize("value", VALUE_LIST)
    @pytest.mark.parametrize("fail_action", FAIL_ACTION_LIST)
    @pytest.mark.parametrize("var_name", VAR_NAME_LIST)
    @pytest.mark.parametrize("test_value", TEST_VALUE_LIST)
    def test_defined_plugin_test_value_not_none(self, value: Any, fail_action: str | None, var_name: str | None, test_value: Any) -> None:
        if (not isinstance(value, Undefined) and value is not None) and test_value is not None and value != test_value:
            if str(fail_action).lower() == "warning":
                if var_name is not None:
                    warn_msg = f"{var_name} was set to {value} but we expected {test_value}. Output may be incorrect or incomplete!"
                else:
                    warn_msg = f"A variable was set to {value} but we expected {test_value}. Output may be incorrect or incomplete!"
                self.defined_function(value, fail_action=fail_action, var_name=var_name, test_value=test_value, warn_msg=warn_msg)
            elif str(fail_action).lower() == "error":
                if var_name is not None:
                    err_msg = f"{var_name} was set to {value} but we expected {test_value}!"
                else:
                    err_msg = f"A variable was set to {value} but we expected {test_value}!"
                self.defined_function(value, fail_action=fail_action, var_name=var_name, test_value=test_value, err_msg=err_msg)

    @pytest.mark.parametrize("value", VALUE_LIST)
    @pytest.mark.parametrize("fail_action", FAIL_ACTION_LIST)
    @pytest.mark.parametrize("var_name", VAR_NAME_LIST)
    @pytest.mark.parametrize("var_type", VAR_TYPE_LIST)
    def test_defined_plugin_var_type(self, value: Any, fail_action: str | None, var_name: str | None, var_type: Any) -> None:
        type_list = ["float", "int", "str", "list", "dict", "tuple", "bool"]
        if not isinstance(value, Undefined) and value is not None and str(var_type).lower() in type_list and str(var_type).lower() != type(value).__name__:
            if str(fail_action).lower() == "warning":
                if var_name is not None:
                    warn_msg = f"{var_name} was a {type(value).__name__} but we expected a {str(var_type).lower()}. Output may be incorrect or incomplete!"
                else:
                    warn_msg = f"A variable was a {type(value).__name__} but we expected a {str(var_type).lower()}. Output may be incorrect or incomplete!"
                self.defined_function(value, fail_action=fail_action, var_name=var_name, var_type=var_type, warn_msg=warn_msg)
            elif str(fail_action).lower() == "error":
                if var_name is not None:
                    err_msg = f"{var_name} was a {type(value).__name__} but we expected a {str(var_type).lower()}!"
                else:
                    err_msg = f"A variable was a {type(value).__name__} but we expected a {str(var_type).lower()}!"
                self.defined_function(value, fail_action=fail_action, var_name=var_name, var_type=var_type, err_msg=err_msg)

    @pytest.mark.parametrize("value", VALUE_LIST)
    @pytest.mark.parametrize("test_value", TEST_VALUE_LIST)
    @pytest.mark.parametrize("invalid_fail_action", INVALID_FAIL_ACTION_LIST)
    def test_defined_plugin_fail_action_none(self, value: Any, test_value: Any, invalid_fail_action: str | None) -> None:
        resp = defined(value, test_value=test_value, fail_action=invalid_fail_action)
        if not isinstance(value, Undefined) and value is not None:
            if test_value is not None and value != test_value:
                assert resp is False
            else:
                assert resp is True
        else:
            assert resp is False

    @pytest.mark.parametrize("value", VALUE_LIST)
    @pytest.mark.parametrize("var_type", VAR_TYPE_LIST)
    def test_defined_plugin_var_type_fail_action_none(self, value: Any, var_type: str | None) -> None:
        type_list = ["float", "int", "str", "list", "dict", "tuple", "bool"]
        if not isinstance(value, Undefined) and value is not None:
            resp = defined(value, var_type=var_type)
            if str(var_type).lower() in type_list and type(value).__name__ != str(var_type).lower():
                assert resp is False
            else:
                assert resp is True
