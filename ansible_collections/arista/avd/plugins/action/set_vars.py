# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:  # noqa: ARG002
        if task_vars is None:
            task_vars = {}

        result = {}
        result["ansible_facts"] = self._task.args
        return result
