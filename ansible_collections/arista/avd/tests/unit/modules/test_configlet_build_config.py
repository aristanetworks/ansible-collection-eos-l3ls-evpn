# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


import os

import pytest

from ansible_collections.arista.avd.plugins.modules.configlet_build_config import get_configlet

CONFIGLETS_DIR = f"{os.path.dirname(os.path.realpath(__file__))}../../inventory/intended/configs"

CONFIGLETS_DATA = {
    "valid_source": {"src_folder": CONFIGLETS_DIR, "prefix": "AVD"},
    "default_prefix": {"src_folder": CONFIGLETS_DIR},
    "non_default_prefix": {"src_folder": CONFIGLETS_DIR, "prefix": "CFG"},
}


class TestConfigletBuildConfig:
    def verify_configlets(self, src_folder, prefix, extension, output) -> None:
        suffixes = [".cfg"]
        for dirpath, _dirnames, filenames in os.walk(src_folder):
            for filename in filenames:
                filesplit = os.path.splitext(filename)
                key = filesplit[0] if not prefix else prefix + "_" + filesplit[0]
                if filesplit[1] in suffixes:
                    assert key in output

                    # Compare contents of each file
                    with open(os.path.join(dirpath, filename), encoding="utf8") as f:
                        assert f.read() == output[key]

    @pytest.mark.parametrize("DATA", CONFIGLETS_DATA.values(), ids=CONFIGLETS_DATA.keys())
    def test_get_configlet(self, DATA) -> None:
        prefix = DATA.get("prefix", None)
        extension = DATA.get("extension", "cfg")
        src_folder = DATA["src_folder"]

        if prefix:
            output = get_configlet(src_folder=src_folder, prefix=prefix, extension=extension)
        else:
            output = get_configlet(src_folder=src_folder, extension=extension)
            prefix = "AVD"
        assert isinstance(output, dict)
        self.verify_configlets(src_folder, prefix, extension, output)

    def test_get_configlet_invalid_source(self) -> None:
        output = get_configlet()
        assert output == {}

    def test_get_configlet_none_prefix(self) -> None:
        extension = "cfg"
        output = get_configlet(src_folder=CONFIGLETS_DIR, prefix="none")
        assert isinstance(output, dict)
        self.verify_configlets(CONFIGLETS_DIR, "", extension, output)
