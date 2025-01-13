# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import pytest

from pyavd.j2filters import status_render

STATE_STRINGS = [("PASS", "github", ":white_check_mark:"), ("fail", "github", ":x:"), ("FAIL", "test", "FAIL")]


class TestMarkdownRenderingFilter:
    @pytest.mark.parametrize(("state_string", "rendering", "markdown_code"), STATE_STRINGS)
    def test_status_render_valid(self, state_string: str, rendering: str, markdown_code: str) -> None:
        resp = status_render(state_string, rendering)
        assert resp == markdown_code
