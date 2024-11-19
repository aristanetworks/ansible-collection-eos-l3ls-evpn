# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from os import environ
from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest
import pytest_asyncio

from tests.pyavd.cv.mockery import MockedServiceStub, RecordingServiceStub, mocked_cv_client_aenter

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    # Avoid importing this outside the mock.
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


@pytest_asyncio.fixture
async def cv_client() -> AsyncGenerator[CVClient, None]:
    """
    Instance of CVClient.

    If CVAAS_AAWG_CI environment variable is set, but RECORDING environment variable is not set,
    this will return a proper instance of CVClient connected to cv-staging with the token.

    If CVAAS_AAWG_CI environment variable is set, but RECORDING environment variable is set,
    this will return an instance of CVClient connected to cv-staging with the token where all API calls will be recorded.

    Otherwise this will return an instance of CVClient where API calls are mocked using previously recorded API messages.
    """
    if token := environ.get("CVAAS_AAWG_CI"):
        LOGGER.info("Running in online mode connecting to cv-staging.")
        if environ.get("RECORDING"):
            LOGGER.info("Mocking ServiceStub to RecordingServiceStub")
            with patch("aristaproto.ServiceStub", new=RecordingServiceStub):
                from pyavd._cv.client import CVClient

                async with CVClient("www.cv-staging.corp.arista.io", token=token) as cv_client:
                    yield cv_client

        else:
            from pyavd._cv.client import CVClient

            async with CVClient("www.cv-staging.corp.arista.io", token=token) as cv_client:
                yield cv_client

    else:
        with patch("aristaproto.ServiceStub", new=MockedServiceStub):  # noqa: SIM117, We do not want to combine since the second mock will mess up imports.
            with patch("pyavd._cv.client.CVClient.__aenter__", new=mocked_cv_client_aenter):
                from pyavd._cv.client import CVClient

                async with CVClient("www.cv-staging.corp.arista.io", token=token) as cv_client:
                    yield cv_client

        return


@pytest.mark.asyncio
async def test_get_inventory_devices(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices()
    assert len(result) > 0


@pytest.mark.asyncio
async def test_get_inventory_devices_with_filter(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices([(None, None, "avd-ci-spine1")])
    assert len(result) == 1
    assert hasattr(result[0], "hostname")
    assert result[0].hostname == "avd-ci-spine1"
