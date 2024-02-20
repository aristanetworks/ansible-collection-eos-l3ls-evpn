# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.filter.status_render import FilterModule

STATE_STRINGS = ["PASS", "FAIL"]
RENDERING_VALID = "github"
RENDERING_INVALID = "test"

GH_CODE = {}
# Github MD code for Emoji checked box
GH_CODE["PASS"] = ":white_check_mark:"
# GH MD code for Emoji Fail
GH_CODE["FAIL"] = ":x:"

f = FilterModule()


class TestMarkdownRenderingFilter:
    @pytest.mark.parametrize("STATE_STRING", STATE_STRINGS)
    def test_status_render_valid(self, STATE_STRING):
        resp = f.status_render(STATE_STRING, RENDERING_VALID)
        assert resp == GH_CODE[STATE_STRING]

    @pytest.mark.parametrize("STATE_STRING", STATE_STRINGS)
    def test_status_render_invalid(self, STATE_STRING):
        resp = f.status_render(STATE_STRING, RENDERING_INVALID)
        assert resp == STATE_STRING

    def test_markdown_rendering_filter(self):
        resp = f.filters()
        assert isinstance(resp, dict)
        assert "status_render" in resp.keys()
