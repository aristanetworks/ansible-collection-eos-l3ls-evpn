# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path
from unittest import mock

import pytest
from yaml import safe_dump

from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._schema.avdschema import AvdSchema
from pyavd.api.pool_manager import FILE_HEADER, PoolManager

DUMMYDIR = "mydir"
""" Files will be mocked throughout. This will be the fake directory under which the data folder holding the pool files will be created. """

TESTHOST1 = {"inventory_hostname": "testhost1", "fabric_name": "pool_manager_tests", "type": "l2leaf"}
TESTHOST2 = {"inventory_hostname": "testhost2", "fabric_name": "pool_manager_tests", "type": "l2leaf"}
TESTHOST3 = {"inventory_hostname": "testhost3", "fabric_name": "pool_manager_tests", "type": "l2leaf", "pod_name": "POD1"}
TESTHOST4 = {"inventory_hostname": "testhost4", "fabric_name": "pool_manager_tests", "type": "l2leaf", "pod_name": "POD1", "dc_name": "DC1"}


def get_assignment(hostvars: dict, node_id: int) -> dict:
    return {"key": f"('{hostvars['inventory_hostname']}',)", "value": node_id}


def get_pool(hostvars: dict, assignments: list[dict] | None = None) -> dict:
    return {
        "pool_key": str((hostvars.get("fabric_name"), hostvars.get("dc_name"), hostvars.get("pod_name"), hostvars.get("type"))),
        "assignments": assignments or [],
    }


def get_data(pools: list[dict] | None = None) -> dict:
    return {"node_id_pools": pools or []}


BASIC_DATA = get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1)])])
""" Basic data set. Works for simple scenarios with one host. """


def get_file_content(data: dict) -> str:
    """Computed file content either to be used for mock_file_content or expected file content."""
    return f"{FILE_HEADER}{safe_dump(data)}"


@pytest.mark.parametrize(
    ("hostvars_list", "expected_ids", "mock_file_data", "expected_data", "requested_ids"),
    [
        pytest.param(
            # File exists but is empty. Request id for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            "",
            BASIC_DATA,
            None,  # requested_ids
            id="empty_file_add_testhost1",
        ),
        pytest.param(
            # File does not exist. Request id for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            None,
            BASIC_DATA,
            None,  # requested_ids
            id="no_file_add_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA. Request id for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            BASIC_DATA,
            BASIC_DATA,
            None,  # requested_ids
            id="keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA. Request ids for testhost1 & 2, get 1 & 2 back.
            # After saving the file contains both IDs since both were active.
            [TESTHOST1, TESTHOST2],
            [1, 2],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="keep_testhost1_add_testhost2",
        ),
        pytest.param(
            # File has BASIC_DATA. Request ids for testhost2 & 1 (reversed order), get 2 & 1 back.
            # After saving the file contains both IDs since both were active.
            [TESTHOST2, TESTHOST1],
            [2, 1],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="add_testhost2_keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA. Request id for testhost2, get 2 back.
            # After saving the file contains only id 2 since id 1 was never requested, so it is deemed stale.
            [TESTHOST2],
            [2],
            BASIC_DATA,
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="add_testhost2_remove_testhost1",
        ),
        pytest.param(
            # File has id2 only. Request id for testhost2 get 2 back.
            # After saving the file contains id 2.
            [TESTHOST2],
            [2],
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="keep_testhost2",
        ),
        pytest.param(
            # File has id2 only. Request id for testhost1 & 2, get 1 & 2 back.
            # After saving the file contains id 1 and 2.
            [TESTHOST1, TESTHOST2],
            [1, 2],
            get_data([get_pool(TESTHOST2, [get_assignment(TESTHOST2, 2)])]),
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            None,  # requested_ids
            id="add_testhost1_remove_testhost2",
        ),
        pytest.param(
            # File has BASIC_DATA. Request id for testhost3 get 1 back.
            # After saving the file contains a new pool with id 1 for testhost3 since id 1 was never requested, so it is deemed stale.
            [TESTHOST3],
            [1],
            BASIC_DATA,
            get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)])]),
            None,  # requested_ids
            id="add_pool_with_testhost2_remove_pool_with_testhost1",
        ),
        pytest.param(
            # File has pool for testhost3 with id 1. Request id for testhost1 & 3, get 1 & 1 back.
            # After saving the file contains two pools with id 1 in each.
            [TESTHOST1, TESTHOST3],
            [1, 1],
            get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)])]),
            get_data([get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)]), get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1)])]),
            None,  # requested_ids
            id="add_pool_with_testhost1_keep_pool_with_testhost3",
        ),
        pytest.param(
            # No file. Request id for testhost4-1 (reversed) and get 1,1,1,2 back.
            # After saving the file contains three pools. First one with 1-2 and 1 in the other two.
            # Notice input is reversed but output is sorted on pool keys (DC1 before None).
            # Also notice testhost2 has id 1 and testhost1 has id 2
            [TESTHOST4, TESTHOST3, TESTHOST2, TESTHOST1],
            [1, 1, 1, 2],
            None,
            get_data(
                [
                    get_pool(TESTHOST4, [get_assignment(TESTHOST4, 1)]),
                    get_pool(TESTHOST3, [get_assignment(TESTHOST3, 1)]),
                    get_pool(TESTHOST1, [get_assignment(TESTHOST2, 1), get_assignment(TESTHOST1, 2)]),
                ]
            ),
            None,  # requested_ids
            id="no_file_add_three_pools_and_four_hosts",
        ),
        pytest.param(
            # File has BASIC_DATA where testhost has id 1. Request the specific id 1 for testhost1, get 1 back.
            # After saving the file contains BASIC_DATA.
            [TESTHOST1],
            [1],
            BASIC_DATA,
            BASIC_DATA,
            [1],  # requested_ids
            id="keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA where testhost has id 1. Request the specific id 66 for testhost1, get 66 back.
            # After saving the file contains testhost1 with id 66.
            [TESTHOST1],
            [66],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 66)])]),
            [66],  # requested_ids
            id="keep_testhost1",
        ),
        pytest.param(
            # File has BASIC_DATA where testhost has id 1. Request the specific id 1 for testhost2, get 2 back.
            # After saving the file contains testhost1 with id 1 and testhost2 with 2.
            [TESTHOST1, TESTHOST2],
            [1, 2],
            BASIC_DATA,
            get_data([get_pool(TESTHOST1, [get_assignment(TESTHOST1, 1), get_assignment(TESTHOST2, 2)])]),
            [None, 1],  # requested_ids
            id="keep_testhost1",
        ),
    ],
)
def test_avdpoolmanager_pool(
    hostvars_list: list[dict], expected_ids: list[int], mock_file_data: str, expected_data: dict, requested_ids: list[int | None] | None
) -> None:
    """
    Test PoolManager.

    Args:
        hostvars_list: Request ID for each host in this list.
        expected_ids: Expected answer on get_id for each host.
        mock_file_data: Initial file data. None for missing file.
        expected_data: File data after saving to file.
        requested_ids: Request this specific ID per host. Index must match hostvars_list.
    """
    file_exists = mock_file_data is not None
    expected_write = mock_file_data != expected_data
    schema = AvdSchema(schema_id="eos_designs")
    with (
        mock.patch.object(Path, "exists", mock.Mock(return_value=file_exists)) as mocked_exists,
        mock.patch.object(Path, "open", mock.mock_open(read_data=get_file_content(mock_file_data))) as mocked_open,
        mock.patch.object(Path, "parent", mock.PropertyMock(mkdir=mock.MagicMock())) as mocked_parent,
        mock.patch.object(Path, "touch", mock.Mock()) as mocked_touch,
    ):
        mocked_open: mock.MagicMock
        mocked_file_write: mock.MagicMock = mocked_open.return_value.write

        # Initialize pool_manager and feed to shared_utils.
        pool_manager = PoolManager(Path(DUMMYDIR))

        for index, hostvars in enumerate(hostvars_list):
            requested_id = requested_ids[index] if requested_ids else None
            shared_utils = SharedUtils(hostvars=hostvars, inputs=EosDesigns._from_dict(hostvars), templar=object(), schema=schema)
            # Get the id of the host from hostvars. If not, a new data set will be created.
            assert pool_manager.get_assignment("node_id_pools", shared_utils, requested_id) == expected_ids[index]

        mocked_exists.assert_called_once()
        if file_exists:
            mocked_open.assert_called_once_with(mode="r", encoding=mock.ANY, errors=None)

        assert pool_manager.save_updated_pools() is expected_write

        if not file_exists:
            # If the mocked file does not exists check that it was created together with the parent dir.
            mocked_mkdir: mock.MagicMock = mocked_parent.return_value.mkdir
            mocked_mkdir.assert_called_once_with(exist_ok=True, mode=509, parents=True)
            mocked_touch.assert_called_once()

        if expected_write:
            mocked_open.assert_called_with(mode="w", encoding=mock.ANY, errors=None, newline=None)
            mocked_file_write.assert_called_once_with(get_file_content(expected_data))
        else:
            mocked_open.assert_called_with(mode="r", encoding=mock.ANY, errors=None)
            mocked_file_write.assert_not_called()
