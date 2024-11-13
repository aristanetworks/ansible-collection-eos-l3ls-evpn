# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import json
import sys
from importlib.metadata import Distribution, PackageNotFoundError, version
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Any

import yaml
from ansible import constants as C  # noqa: N812
from ansible.errors import AnsibleActionFail
from ansible.module_utils.compat.importlib import import_module
from ansible.plugins.action import ActionBase, display
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata

from ansible_collections.arista.avd.plugins import PYTHON_AVD_PATH, RUNNING_FROM_SOURCE

try:
    # Relying on packaging installed by ansible
    from packaging.requirements import InvalidRequirement, Requirement
    from packaging.specifiers import SpecifierSet

    HAS_PACKAGING = True
except ImportError:
    HAS_PACKAGING = False

try:
    from ansible_collections.arista.avd.plugins.plugin_utils.utils.init_logging import init_pyavd_logging

    HAS_INIT_PYAVD_LOGGING = True
except ImportError:
    HAS_INIT_PYAVD_LOGGING = False

if HAS_INIT_PYAVD_LOGGING:
    init_pyavd_logging()

MIN_PYTHON_SUPPORTED_VERSION = (3, 10)
DEPRECATE_MIN_PYTHON_SUPPORTED_VERSION = False


def _validate_python_version(info: dict, result: dict) -> bool:
    """
    TODO: - avoid hardcoding the min supported version.

    Args:
      info (dict): Dictionary to store information to present in ansible logs
      result (dict): Module result dictionary to store deprecation warnings

    return False if the python version is not valid
    """
    info["python_version_info"] = {
        "major": sys.version_info.major,
        "minor": sys.version_info.minor,
        "micro": sys.version_info.micro,
        "releaselevel": sys.version_info.releaselevel,
        "serial": sys.version_info.serial,
    }
    info["python_path"] = sys.path

    running_version = ".".join(str(v) for v in sys.version_info[:3])
    min_version = ".".join(str(v) for v in MIN_PYTHON_SUPPORTED_VERSION)
    if sys.version_info < MIN_PYTHON_SUPPORTED_VERSION:
        display.error(f"Python Version running {running_version} - Minimum Version required is {min_version}", wrap_text=False)
        return False
    # Keeping this for next deprecation adjust the message as required
    if DEPRECATE_MIN_PYTHON_SUPPORTED_VERSION and sys.version_info[:2] == MIN_PYTHON_SUPPORTED_VERSION:
        result.setdefault("deprecations", []).append(
            {
                "msg": (
                    f"You are currently running Python version {running_version}. "
                    f"AVD version 5.0.0 will drop support for Python version {min_version}. "
                    "The decision has been taken to remove Python version 3.9 support in AVD "
                    "collection to anticipate its removal in `ansible-core`. `ansible-core` "
                    "version 2.15 End-Of-Life is scheduled for November 2024 and it will be the "
                    "last `ansible-core` version supporting Python version 3.9 as documented here: "
                    "https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix."
                ),
            },
        )

    return True


def _validate_python_requirements(requirements: list, info: dict) -> bool:
    """
    Validate python lib versions.

    Args:
      requirements (list): List of requirements for pythom modules
      info (dict): Dictionary to store information to present in ansible logs

    return False if any python requirement is not valid
    """
    valid = True

    requirements_dict: dict[str, Any] = {
        "not_found": {},
        "valid": {},
        "mismatched": {},
        "parsing_failed": [],
    }

    # Remove the comments including inline comments
    requirements = [req.split(" #", maxsplit=1)[0] for req in requirements if req[0] != "#"]
    for raw_req in requirements:
        try:
            req = Requirement(raw_req)
        except InvalidRequirement as exc:
            msg = f"Wrong format for requirement {raw_req}"
            raise AnsibleActionFail(msg) from exc

        if RUNNING_FROM_SOURCE and req.name == "pyavd":
            display.vvv("AVD is running from source, *not* checking pyavd version.", "Verify Requirements")
            requirements_dict["valid"][req.name] = {
                "installed": "running from source",
                "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            continue

        try:
            installed_version = version(req.name)
            display.vvv(f"Found {req.name} {installed_version} installed!", "Verify Requirements")

            # If some old dist-info files are leftover in Python site-packages, it is possible
            # to find multiple Distributions for the installed version
            potential_dists = Distribution.discover(name=req.name)
            detected_versions = [dist.version for dist in potential_dists]
            valid_versions = [version for version in detected_versions if req.specifier.contains(version)]
            if len(detected_versions) > 1:
                display.v(f"Found {req.name} {detected_versions} metadata - this could mean legacy dist-info files are present in your site-packages folder.")
        except PackageNotFoundError:
            requirements_dict["not_found"][req.name] = {
                "installed": None,
                "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            display.error(f"Python library '{req.name}' required but not found - requirement is {req!s}", wrap_text=False)
            valid = False
            continue

        if req.specifier.contains(installed_version):
            requirements_dict["valid"][req.name] = {
                "installed": installed_version,
                "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
            }
        elif len(valid_versions) > 0:
            # More than one dist found and at least one was matching - output a warning
            requirements_dict["valid"][req.name] = {
                "installed": installed_version,
                "detected_versions": detected_versions,
                "valid_versions": valid_versions,
                "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            display.warning(
                f"Found {req.name} valid versions {valid_versions} among {detected_versions} from metadata - assuming a valid version is running - more"
                " information available with -v",
            )
            display.v(
                "The Arista AVD collection relies on Python built-in library `importlib.metadata` to detect running versions. In some cases where legacy"
                " dist-info folders are leftovers in the site-packages folder, there can be misdetection of the version. This module assumes that if any"
                " version matches the required one, then the requirement is met. This could led to false positive results. Please make sure to clean the"
                " leftovers dist-info folders.",
            )
        elif len(detected_versions) > 1:
            # More than one dist found and none matching the requirements
            display.error(
                f"Python library '{req.name}' detected versions {detected_versions} - requirement is {req!s} - more information available with -v",
                wrap_text=False,
            )
            requirements_dict["mismatched"][req.name] = {
                "installed": installed_version,
                "detected_versions": detected_versions,
                "valid_versions": None,
                "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            display.error(f"Python library '{req.name}' version running {installed_version} - requirement is {req!s}", wrap_text=False)
        else:
            display.error(f"Python library '{req.name}' version running {installed_version} - requirement is {req!s}", wrap_text=False)
            requirements_dict["mismatched"][req.name] = {
                "installed": installed_version,
                "required_version": str(req.specifier) if len(req.specifier) > 0 else None,
            }
            valid = False

    info["python_requirements"] = requirements_dict
    return valid


def _validate_ansible_version(collection_name: str, running_version: str, info: dict, result: dict) -> bool:
    """
    Validate ansible version in use, running_version, based on the collection requirements.

    Args:
      collection_name (str): The collection name
      running_version (str): A string representing the current Ansible version being run
      info (dict): Dictionary to store information to present in ansible logs
      result (dict): Module result dictionary to store deprecation warnings

    Return False if Ansible version is not valid
    """
    collection_meta = _get_collection_metadata(collection_name)
    specifiers_set = SpecifierSet(collection_meta.get("requires_ansible", ""))
    deprecation_specifiers_set = SpecifierSet()
    info["ansible_version"] = running_version

    if len(specifiers_set) > 0:
        info["requires_ansible"] = str(specifiers_set)
    if not specifiers_set.contains(running_version):
        display.error(
            f"Ansible Version running {running_version} - Requirement is {specifiers_set!s}",
            wrap_text=False,
        )
        return False
    # Keeping this for next deprecation - set the value of deprecation_specifiers_set when needed and adjust message
    if not deprecation_specifiers_set.contains(running_version):
        result.setdefault("deprecations", []).append(
            {
                "msg": (
                    f"You are currently running ansible-core {running_version}. The next minor release of AVD after November 6th 2023 will drop support for"
                    " ansible-core<2.14. Python 3.8 support will be dropped at the same time as ansible-core>=2.14 does not support it. See the following link"
                    " for more details: https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix"
                ),
            },
        )

    return True


def _validate_ansible_collections(running_collection_name: str, info: dict) -> bool:
    """
    Verify the version of required ansible collections running based on the collection requirements.

    Args:
      running_collection_name (str): The collection name
      info (dict): Dictionary to store information to present in ansible logs

    Return True if all collection requirements are valid, False otherwise
    """
    valid = True

    collection_path = _get_collection_path(running_collection_name)
    with Path(collection_path, "collections.yml").open("rb") as fd:
        metadata = yaml.safe_load(fd)
    if "collections" not in metadata:
        # no requirements
        return True

    requirements_dict: dict[str, Any] = {
        "not_found": {},
        "valid": {},
        "mismatched": {},
        "parsing_failed": [],
    }

    for collection_dict in metadata["collections"]:
        if "name" not in collection_dict:
            display.error("key `name` required but not found in collections requirement - please raise an issue on Github", wrap_text=False)
            continue

        collection_name = collection_dict["name"]
        # Check if there is a version requirement
        specifiers_set = SpecifierSet(collection_dict.get("version", ""))

        try:
            collection_path = _get_collection_path(collection_name)
        except ModuleNotFoundError:
            requirements_dict["not_found"][collection_name] = {
                "installed": None,
                "required_version": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
            if specifiers_set:
                display.error(f"{collection_name} required but not found - required version is {specifiers_set!s}", wrap_text=False)
            else:
                display.error(f"{collection_name} required but not found", wrap_text=False)
            valid = False
            continue

        installed_version = _get_collection_version(collection_path)

        if specifiers_set.contains(installed_version):
            requirements_dict["valid"][collection_name] = {
                "installed": installed_version,
                "required_version": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
        else:
            display.error(f"{collection_name} version running {installed_version} - required version is {specifiers_set!s}", wrap_text=False)
            requirements_dict["mismatched"][collection_name] = {
                "installed": installed_version,
                "required_version": str(specifiers_set) if len(specifiers_set) > 0 else None,
            }
            valid = False

    info["collection_requirements"] = requirements_dict
    return valid


def _get_collection_path(collection_name: str) -> str:
    """Retrieve the collection path based on the collection_name."""
    collection = import_module(f"ansible_collections.{collection_name}")
    return str(Path(collection.__file__).parent)


def _get_collection_version(collection_path: str) -> str:
    """Returns the collection version based on the collection path."""
    # Trying to find the version based on either galaxy.yml or MANIFEST.json
    try:
        galaxy_file = Path(collection_path, "galaxy.yml")
        with galaxy_file.open("rb") as fd:
            metadata = yaml.safe_load(fd)
    except FileNotFoundError:
        manifest_file = Path(collection_path, "MANIFEST.json")
        with manifest_file.open("rb") as fd:
            metadata = json.load(fd)["collection_info"]

    return metadata["version"]


def _get_running_collection_version(running_collection_name: str, result: dict) -> None:
    """Stores the version collection in result."""
    collection_path = _get_collection_path(running_collection_name)
    version = _get_collection_version(collection_path)

    try:
        # Try to detect a git tag
        # Using subprocess for now
        with Popen(["git", "describe", "--tags"], stdout=PIPE, stderr=PIPE, cwd=collection_path) as process:  # noqa: S603, S607
            output, err = process.communicate()
            if err:
                # Not that when molecule runs, it runs in a copy of the directory that is not a git repo
                # so only the latest tag is being returned
                display.vvv("Not a git repository")
            else:
                display.vvv("This is a git repository, overwriting version with 'git describe --tags output'")
                version = output.decode("UTF-8").strip()
    except FileNotFoundError:
        # Handle the case where `git` is not installed or not in the PATH
        display.vvv("Could not find 'git' executable, returning collection version")

    result["collection"] = {
        "name": running_collection_name,
        "path": str(Path(collection_path).parents[1]),
        "version": version,
    }


def check_running_from_source() -> bool:
    """
    Check if running from sources, if so recompile schemas and templates as needed.

    Returns:
    --------
    bool:
        True if schemas or templates were recompiled, False otherwise.
    """
    if not RUNNING_FROM_SOURCE:
        return False

    # if running from source, path to pyavd and schema_tools has already been prepended to Python Path
    from schema_tools.check_schemas import check_schemas, rebuild_schemas
    from schema_tools.compile_templates import check_templates, recompile_templates

    if schemas_recompiled := check_schemas():
        display.display("Schemas have changed, rebuilding...", color=C.COLOR_CHANGED)
        rebuild_schemas()
        display.display("Done.", color=C.COLOR_CHANGED)

    if templates_recompiled := check_templates():
        display.display("Templates have changed, recompiling...", color=C.COLOR_CHANGED)
        recompile_templates()
        display.display("Done.", color=C.COLOR_CHANGED)

    return schemas_recompiled or templates_recompiled


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PACKAGING:
            msg = "packaging is required to run this plugin"
            raise AnsibleActionFail(msg)

        if not (self._task.args and "requirements" in self._task.args):
            msg = "The argument 'requirements' must be set"
            raise AnsibleActionFail(msg)

        py_requirements = self._task.args.get("requirements")
        avd_ignore_requirements = self._task.args.get("avd_ignore_requirements", False)
        if avd_ignore_requirements in ["true", "True"]:
            avd_ignore_requirements = True

        if not isinstance(py_requirements, list):
            msg = "The argument 'requirements' is not a list"
            raise AnsibleActionFail(msg)

        running_ansible_version = task_vars["ansible_version"]["string"]
        running_collection_name = task_vars["ansible_collection_name"]

        result["failed"] = False

        error_message = "Set 'avd_ignore_requirements=True' to ignore validation error(s)."
        info: dict[str, Any] = {
            "ansible": {},
            "python": {},
        }

        _get_running_collection_version(running_collection_name, info["ansible"])

        if check_running_from_source():
            result["changed"] = True

        display.display(f"AVD version {info['ansible']['collection']['version']}", color=C.COLOR_OK)
        if RUNNING_FROM_SOURCE:
            display.display(f"AVD is running from source using PyAVD at '{PYTHON_AVD_PATH}'", color=C.COLOR_OK)
        if display.verbosity < 1:
            display.display("Use -v for details.")

        if not _validate_python_version(info["python"], result):
            result["failed"] = True
        if not _validate_python_requirements(py_requirements, info["python"]):
            result["failed"] = True
        if not _validate_ansible_version(running_collection_name, running_ansible_version, info["ansible"], result):
            result["failed"] = True
        if not _validate_ansible_collections(running_collection_name, info["ansible"]):
            result["failed"] = True

        display.v(json.dumps(info, indent=4))

        if avd_ignore_requirements is True:
            result["failed"] = False
        elif result["failed"] is True:
            result["msg"] = error_message

        return result
