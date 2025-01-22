# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


import re
from contextlib import nullcontext as does_not_raise

import pytest
from _pytest.python_api import RaisesContext

from pyavd._cv.client.exceptions import CVDuplicatedDevices
from pyavd._cv.workflows.models import CVDevice
from pyavd._cv.workflows.verify_inputs import verify_device_inputs

ONE_DUPED_SERIAL_ESCAPED_PATTERNS = [
    re.escape(
        "'Duplicated devices found in inventory', "
        "[{'duplicated_serial_number': 'serial1', 'devices_with_duplicated_serial_number': "
        "[CVDevice(hostname='switch1', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f1', _exists_on_cv=None), "
        "CVDevice(hostname='switch2', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f2', _exists_on_cv=None)]}], "
        "[])"
    ),
]

ONE_DUPED_SYS_MAC_ESCAPED_PATTERNS = [
    re.escape(
        "'Duplicated devices found in inventory', "
        "[], "
        "[{'duplicated_system_mac_address': 'aa:bb:cc:dd:ee:f3', 'devices_with_duplicated_system_mac_address': "
        "[CVDevice(hostname='switch3', serial_number='serial3', system_mac_address='aa:bb:cc:dd:ee:f3', _exists_on_cv=None), "
        "CVDevice(hostname='switch4', serial_number='serial4', system_mac_address='aa:bb:cc:dd:ee:f3', _exists_on_cv=None)]}])"
    ),
]

ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_ESCAPED_PATTERNS = [
    re.escape(
        "'Duplicated devices found in inventory', "
        "[{'duplicated_serial_number': 'serial1', 'devices_with_duplicated_serial_number': "
        "[CVDevice(hostname='switch1', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f1', _exists_on_cv=None), "
        "CVDevice(hostname='switch2', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f2', _exists_on_cv=None)]}], "
        "[{'duplicated_system_mac_address': 'aa:bb:cc:dd:ee:f3', 'devices_with_duplicated_system_mac_address': "
        "[CVDevice(hostname='switch3', serial_number='serial3', system_mac_address='aa:bb:cc:dd:ee:f3', _exists_on_cv=None), "
        "CVDevice(hostname='switch4', serial_number='serial4', system_mac_address='aa:bb:cc:dd:ee:f3', _exists_on_cv=None)]}])"
    ),
]

ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_ESCAPED_PATTERNS = [
    re.escape(
        "'Duplicated devices found in inventory', "
        "[{'duplicated_serial_number': 'serial1', 'devices_with_duplicated_serial_number': "
        "[CVDevice(hostname='switch1', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f1', _exists_on_cv=None), "
        "CVDevice(hostname='switch2', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f1', _exists_on_cv=None)]}], "
        "[{'duplicated_system_mac_address': 'aa:bb:cc:dd:ee:f1', 'devices_with_duplicated_system_mac_address': "
        "[CVDevice(hostname='switch1', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f1', _exists_on_cv=None), "
        "CVDevice(hostname='switch2', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f1', _exists_on_cv=None)]}])"
    ),
]

THREE_DUPED_SERIAL_TWO_DUPED_SYS_MAC_ESCAPED_PATTERNS = [
    re.escape(
        "'Duplicated devices found in inventory', "
        "[{'duplicated_serial_number': 'serial1', 'devices_with_duplicated_serial_number': "
        "[CVDevice(hostname='switch1', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f1', _exists_on_cv=None), "
        "CVDevice(hostname='switch2', serial_number='serial1', system_mac_address='aa:bb:cc:dd:ee:f2', _exists_on_cv=None)]}, "
        "{'duplicated_serial_number': 'serial3', 'devices_with_duplicated_serial_number': "
        "[CVDevice(hostname='switch3', serial_number='serial3', system_mac_address='aa:bb:cc:dd:ee:f3', _exists_on_cv=None), "
        "CVDevice(hostname='switch4', serial_number='serial3', system_mac_address='aa:bb:cc:dd:ee:f4', _exists_on_cv=None)]}, "
        "{'duplicated_serial_number': 'serial5', 'devices_with_duplicated_serial_number': "
        "[CVDevice(hostname='switch5', serial_number='serial5', system_mac_address='aa:bb:cc:dd:ee:f5', _exists_on_cv=None), "
        "CVDevice(hostname='switch6', serial_number='serial5', system_mac_address='aa:bb:cc:dd:ee:f6', _exists_on_cv=None)]}], "
        "[{'duplicated_system_mac_address': 'aa:bb:cc:dd:ee:f7', 'devices_with_duplicated_system_mac_address': "
        "[CVDevice(hostname='switch7', serial_number='serial7', system_mac_address='aa:bb:cc:dd:ee:f7', _exists_on_cv=None), "
        "CVDevice(hostname='switch8', serial_number='serial8', system_mac_address='aa:bb:cc:dd:ee:f7', _exists_on_cv=None)]}, "
        "{'duplicated_system_mac_address': 'aa:bb:cc:dd:ee:f9', 'devices_with_duplicated_system_mac_address': "
        "[CVDevice(hostname='switch9', serial_number='serial9', system_mac_address='aa:bb:cc:dd:ee:f9', _exists_on_cv=None), "
        "CVDevice(hostname='switch10', serial_number='serial10', system_mac_address='aa:bb:cc:dd:ee:f9', _exists_on_cv=None)]}]"
    )
]


@pytest.mark.parametrize(
    ("devices", "tolerate_duplicated_devices", "expected_patterns", "expected_exception"),
    [
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial2", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            True,
            [],
            does_not_raise(),
            id="NO_DUPS_TOLER_TRUE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial2", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            False,
            [],
            does_not_raise(),
            id="NO_DUPS_TOLER_FALSE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            True,
            ONE_DUPED_SERIAL_ESCAPED_PATTERNS,
            does_not_raise(),
            id="ONE_DUPED_SERIAL_TOLER_TRUE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            False,
            ONE_DUPED_SERIAL_ESCAPED_PATTERNS,
            pytest.raises(CVDuplicatedDevices),
            id="ONE_DUPED_SERIAL_TOLER_FALSE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            True,
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_ESCAPED_PATTERNS,
            does_not_raise(),
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_TOLER_TRUE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            False,
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_ESCAPED_PATTERNS,
            pytest.raises(CVDuplicatedDevices),
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_TOLER_FALSE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            True,
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_ESCAPED_PATTERNS,
            does_not_raise(),
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_TOLER_TRUE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
            ],
            False,
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_ESCAPED_PATTERNS,
            pytest.raises(CVDuplicatedDevices),
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_TOLER_FALSE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
                CVDevice(hostname="switch6", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f6"),
                CVDevice(hostname="switch7", serial_number="serial7", system_mac_address="aa:bb:cc:dd:ee:f7"),
                CVDevice(hostname="switch8", serial_number="serial8", system_mac_address="aa:bb:cc:dd:ee:f7"),
                CVDevice(hostname="switch9", serial_number="serial9", system_mac_address="aa:bb:cc:dd:ee:f9"),
                CVDevice(hostname="switch10", serial_number="serial10", system_mac_address="aa:bb:cc:dd:ee:f9"),
            ],
            True,
            THREE_DUPED_SERIAL_TWO_DUPED_SYS_MAC_ESCAPED_PATTERNS,
            does_not_raise(),
            id="THREE_DUPED_SERIAL_TWO_DUPED_SYS_MAC_TOLER_TRUE",
        ),
        pytest.param(
            [
                CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
                CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
                CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
                CVDevice(hostname="switch4", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f4"),
                CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
                CVDevice(hostname="switch6", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f6"),
                CVDevice(hostname="switch7", serial_number="serial7", system_mac_address="aa:bb:cc:dd:ee:f7"),
                CVDevice(hostname="switch8", serial_number="serial8", system_mac_address="aa:bb:cc:dd:ee:f7"),
                CVDevice(hostname="switch9", serial_number="serial9", system_mac_address="aa:bb:cc:dd:ee:f9"),
                CVDevice(hostname="switch10", serial_number="serial10", system_mac_address="aa:bb:cc:dd:ee:f9"),
            ],
            False,
            THREE_DUPED_SERIAL_TWO_DUPED_SYS_MAC_ESCAPED_PATTERNS,
            pytest.raises(CVDuplicatedDevices),
            id="THREE_DUPED_SERIAL_TWO_DUPED_SYS_MAC_TOLER_FALSE",
        ),
    ],
)
def test_verify_device_inputs(
    *,
    devices: list[CVDevice],
    tolerate_duplicated_devices: bool,
    warnings: list[Exception] | None = None,
    expected_patterns: list[str],
    expected_exception: RaisesContext | does_not_raise,
) -> None:
    # Create an empty list for warnings
    warnings = []
    with expected_exception as exc_info:
        # Engage FUT
        verify_device_inputs(devices=devices, tolerate_duplicated_devices=tolerate_duplicated_devices, warnings=warnings)
    # Assert that updated warnings contain patterns of all expected exceptions
    if warnings:
        for expected_pattern in expected_patterns:
            assert any(re.search(re.compile(expected_pattern), str(warning_item.args)) for warning_item in warnings)
    # If exception is raised, assert that exception value conytains all expected exception patterns
    if exc_info and (exception_string := str(exc_info.value)):
        for expected_pattern in expected_patterns:
            assert re.search(re.compile(expected_pattern), exception_string)
