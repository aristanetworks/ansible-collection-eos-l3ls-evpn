# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from subprocess import Popen
from typing import TYPE_CHECKING, Any

from setuptools import build_meta as _orig
from yaml import safe_load

if not TYPE_CHECKING:

    def __getattr__(name: str) -> Any:
        """Workaround to avoid 'from setuptools.build_meta import *'."""
        return locals().get(name, getattr(_orig, name))


def _translate_version(version: str, pyavd_prerelease: str) -> str:
    """Translate an Ansible collection version to Python package version."""
    avd_base_version = version.split("-", maxsplit=1)[0]

    if pyavd_prerelease:
        return f"{avd_base_version}{pyavd_prerelease}"

    if "-dev" in version:
        avd_dev_version = version.split("-dev")[1]
        return f"{avd_base_version}.dev{avd_dev_version}"

    if "-rc" in version:
        avd_rc_version = version.split("-rc")[1]
        return f"{avd_base_version}rc{avd_rc_version}"

    return avd_base_version


def _insert_version() -> None:
    with Path(__file__).parents[2].joinpath("ansible_collections/arista/avd/galaxy.yml").open(encoding="UTF-8") as galaxy_file:
        ansible_version = dict(safe_load(galaxy_file)).get("version")

    with Path(__file__).parents[1].joinpath("pyavd/__init__.py").open(encoding="UTF-8") as init_file:
        init_lines = init_file.readlines()

    pyavd_prerelease = ""
    for line in init_lines:
        if "PYAVD_PRERELEASE" in line:
            pyavd_prerelease = line.split("=", maxsplit=1)[1].split("#")[0].replace('"', "").strip()
            break

    version = _translate_version(ansible_version, pyavd_prerelease)

    for index, line in enumerate(init_lines):
        if "__version__" in line:
            init_lines[index] = f'__version__ = "{version}"\n'
            break

    with Path(__file__).parents[1].joinpath("pyavd/__init__.py").open(mode="w", encoding="UTF-8") as init_file:
        init_file.writelines(init_lines)


def get_requires_for_build_wheel(config_settings: dict | None = None) -> list[str]:
    print("Fetch version from ansible.avd ansible collection and insert into __init__.py")
    _insert_version()

    print("Running 'make dep' to generate compiled Jinja2 templates and schemas pickle files.")
    with Popen("make dep", shell=True) as make_process:  # noqa: S602,S607
        if make_process.wait() != 0:
            msg = "Something went wrong during 'make dep'"
            raise RuntimeError(msg)

    return _orig.get_requires_for_build_wheel(config_settings)


def get_requires_for_build_editable(config_settings: dict | None = None) -> list[str]:
    print("Running 'make dep' to generate compiled Jinja2 templates and schemas pickle files.")
    with Popen("make dep", shell=True) as make_process:  # noqa: S602,S607
        if make_process.wait() != 0:
            msg = "Something went wrong during 'make dep'"
            raise RuntimeError(msg)

    return _orig.get_requires_for_build_editable(config_settings)
