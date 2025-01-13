# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import os
from collections import namedtuple
from importlib.metadata import PackageNotFoundError
from pathlib import Path
from unittest.mock import patch

import pytest

from ansible_collections.arista.avd.plugins.action.verify_requirements import (
    MIN_PYTHON_SUPPORTED_VERSION,
    _get_running_collection_version,
    _validate_ansible_collections,
    _validate_ansible_version,
    _validate_python_requirements,
    _validate_python_version,
)


@pytest.mark.parametrize(
    ("mocked_version", "expected_return"),
    [
        ((2, 2, 2, "final", 0), False),
        ((MIN_PYTHON_SUPPORTED_VERSION[0], MIN_PYTHON_SUPPORTED_VERSION[1], 42, "final", 0), True),
        ((MIN_PYTHON_SUPPORTED_VERSION[0], MIN_PYTHON_SUPPORTED_VERSION[1] + 1, 42, "final", 0), True),
    ],
)
def test__validate_python_version(mocked_version, expected_return) -> None:
    """TODO: - could add the expected stderr."""
    info = {}
    result = {}  # As in ansible module result
    version_info = namedtuple("version_info", "major minor micro releaselevel serial")
    with patch("ansible_collections.arista.avd.plugins.action.verify_requirements.sys") as mocked_sys:
        mocked_sys.version_info = version_info(*mocked_version)
        ret = _validate_python_version(info, result)
    assert ret == expected_return
    assert info["python_version_info"] == {
        "major": mocked_version[0],
        "minor": mocked_version[1],
        "micro": mocked_version[2],
        "releaselevel": mocked_version[3],
        "serial": mocked_version[4],
    }
    assert bool(info["python_path"])
    # if mocked_version[:2] == MIN_PYTHON_SUPPORTED_VERSION:
    #     # Check for depreecation of PYTHON 3.8
    #     assert len(result["deprecations"]) == 1


@pytest.mark.parametrize(
    ("n_reqs", "mocked_version", "requirement_version", "expected_return"),
    [
        pytest.param(
            1,
            "4.3",
            "4.2",
            True,
            id="valid version",
        ),
        pytest.param(
            1,
            "4.3",
            "4.2 # inline comment",
            True,
            id="requirement with inline comment",
        ),
        pytest.param(
            2,
            "4.0",
            "4.2",
            False,
            id="invalid version",
        ),
        pytest.param(
            1,
            None,
            "4.2",
            False,
            id="missing requirement",
        ),
        pytest.param(
            0,
            None,
            None,
            True,
            id="no requirement",
        ),
    ],
)
def test__validate_python_requirements(n_reqs, mocked_version, requirement_version, expected_return) -> None:
    """
    Running with n_reqs requirements.

    TODO: - check the results
         - not testing for wrongly formatted requirements
    """
    result = {}
    requirements = [f"test-dep>={requirement_version}" for _ in range(n_reqs)]  # pylint: disable=disallowed-name
    with patch("ansible_collections.arista.avd.plugins.action.verify_requirements.version") as patched_version:
        patched_version.return_value = mocked_version
        if mocked_version is None:
            patched_version.side_effect = PackageNotFoundError()
        ret = _validate_python_requirements(requirements, result)
        assert ret == expected_return


@pytest.mark.parametrize(
    ("mocked_running_version", "deprecated_version", "expected_return"),
    [
        pytest.param(
            "2.16",
            False,
            True,
            id="valid ansible version",
        ),
        pytest.param(
            "2.14.0",
            True,
            False,
            id="invalid ansible version",
        ),
        # pytest.param(
        #     "2.12.6",
        #     True,
        #     True,
        #     id="deprecated ansible version",
        # ),
    ],
)
def test__validate_ansible_version(mocked_running_version, deprecated_version, expected_return) -> None:
    """TODO: - check that the requires_ansible is picked up from the correct place."""
    info = {}
    result = {}  # As in ansible module result
    ret = _validate_ansible_version("arista.avd", mocked_running_version, info, result)
    assert ret == expected_return
    if expected_return is True and deprecated_version is True:
        # Check for depreecation of old Ansible versions (Not used right now)
        assert len(result["deprecations"]) == 1


@pytest.mark.parametrize(
    ("n_reqs", "mocked_version", "requirement_version", "expected_return"),
    [
        pytest.param(1, "4.3", ">=4.2", True, id="valid version"),
        pytest.param(1, "4.3", None, True, id="no required version"),
        pytest.param(2, "4.0", ">=4.2", False, id="invalid version"),
        pytest.param(1, None, ">=4.2", False, id="missing requirement"),
        pytest.param(0, None, None, True, id="no requirement"),
    ],
)
def test__validate_ansible_collections(n_reqs, mocked_version, requirement_version, expected_return) -> None:
    """
    Running with n_reqs requirements in the collection file.

    TODO: - check the results
         - not testing for wrongly formatted collection.yml file
    """
    result = {}

    # Create the metadata based on test input data
    metadata = {}
    if n_reqs > 0:
        metadata["collections"] = [{"name": "test-collection"} for _ in range(n_reqs)]  # pylint: disable=disallowed-name
        if requirement_version is not None:
            for collection in metadata["collections"]:
                collection["version"] = requirement_version

    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.Path.open"),
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.yaml.safe_load") as patched_safe_load,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_path",
        ) as patched__get_collection_path,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_version",
        ) as patched__get_collection_version,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements.open",
        ),
    ):
        patched_safe_load.return_value = metadata
        patched__get_collection_path.return_value = "/collections/foo/bar"
        if mocked_version is None and n_reqs > 0:
            # First call is for arista.avd
            patched__get_collection_path.side_effect = ["/collections/foo/bar", ModuleNotFoundError()]
        patched__get_collection_version.return_value = mocked_version

        ret = _validate_ansible_collections("arista.avd", result)
        assert ret == expected_return


def test__get_running_collection_version_git_not_installed() -> None:
    """Verify that when git is not found in PATH the function returns properly."""
    # setting PATH to empty string to make sure git is not present
    os.environ["PATH"] = ""
    # setting ANSIBLE_VERBOSITY to trigger the log message when raising the exception
    os.environ["ANSIBLE_VERBOSITY"] = "3"
    result = {}
    with (
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.Path") as patched_Path,
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_path") as patched__get_collection_path,
        patch(
            "ansible_collections.arista.avd.plugins.action.verify_requirements._get_collection_version",
        ) as patched__get_collection_version,
        patch("ansible_collections.arista.avd.plugins.action.verify_requirements.display") as patched_display,
    ):
        patched__get_collection_path.return_value = "."
        patched__get_collection_version.return_value = "42.0.0"
        # TODO: Path is less kind than os.path was
        patched_Path.return_value = Path("/collections/foo/bar/__synthetic__/blah")

        _get_running_collection_version("dummy", result)
        patched_display.vvv.assert_called_once_with("Could not find 'git' executable, returning collection version")
    assert result == {"collection": {"name": "dummy", "path": "/collections/foo/bar", "version": "42.0.0"}}
