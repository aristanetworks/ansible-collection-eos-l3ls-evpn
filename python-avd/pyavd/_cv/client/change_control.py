# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.changecontrol.v1 import (
    ApproveConfig,
    ApproveConfigServiceStub,
    ApproveConfigSetRequest,
    ChangeConfig,
    ChangeControl,
    ChangeControlConfig,
    ChangeControlConfigServiceStub,
    ChangeControlConfigSetRequest,
    ChangeControlConfigSetResponse,
    ChangeControlKey,
    ChangeControlRequest,
    ChangeControlServiceStub,
    ChangeControlStatus,
    ChangeControlStreamRequest,
    FlagConfig,
)

from .constants import DEFAULT_API_TIMEOUT
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from datetime import datetime

    from aristaproto import _DateTime

    from . import CVClientProtocol


LOGGER = getLogger(__name__)

CHANGE_CONTROL_STATUS_MAP = {
    "completed": ChangeControlStatus.COMPLETED,
    "unspecified": ChangeControlStatus.UNSPECIFIED,
    "running": ChangeControlStatus.RUNNING,
    "scheduled": ChangeControlStatus.SCHEDULED,
}


class ChangeControlMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    workspace_api_version: Literal["v1"] = "v1"

    async def get_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ChangeControl:
        """
        Get Change Control using arista.changecontrol.v1.ChangeControlService.GetOne API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            ChangeControl object matching the change_control_id
        """
        request = ChangeControlRequest(
            key=ChangeControlKey(id=change_control_id),
            time=time,
        )
        client = ChangeControlServiceStub(self._channel)

        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Change Control ID '{change_control_id}'") or e

        return response.value

    async def set_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        name: str | None = None,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ChangeControlConfigSetResponse:
        """
        Set Change Control details using arista.changecontrol.v1.ChangeControlConfigService.Set API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            name: Change Control Name.
            description: Change Control description.
            TODO: Add CC template
            timeout: Timeout in seconds.

        Returns:
            ChangeControlConfig object after being set including any server-generated values.
        """
        request = ChangeControlConfigSetRequest(
            value=ChangeControlConfig(
                key=ChangeControlKey(id=change_control_id),
                change=ChangeConfig(name=name, notes=description),
            ),
        )
        client = ChangeControlConfigServiceStub(self._channel)

        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Change Control ID '{change_control_id}'") or e

        return response.value

    async def approve_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        timestamp: _DateTime,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ApproveConfig:
        """
        Get Change Control using arista.changecontrol.v1.ChangeControlService.GetOne API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            timestamp: Timestamp for the change control information to be approved. \
                This must be using the aristaproto._DateTime subclass which contains nanosecond information.
            description: Description to set on the approval.
            timeout: Timeout in seconds.

        Returns:
            ApproveConfig object carrying all the values given in the ApproveConfigSetRequest as well
            as any server-generated values.
        """
        request = ApproveConfigSetRequest(
            value=ApproveConfig(
                key=ChangeControlKey(id=change_control_id),
                approve=FlagConfig(value=True, notes=description),
                version=timestamp,
            ),
        )
        client = ApproveConfigServiceStub(self._channel)

        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Approving Change Control ID '{change_control_id}' for timestamp '{timestamp}'") or e

        return response.value

    async def start_change_control(
        self: CVClientProtocol,
        change_control_id: str,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ChangeControlConfig:
        """
        Set Change Control details using arista.changecontrol.v1.ChangeControlConfigService.Set API.

        Parameters:
            change_control_id: Unique identifier of the Change Control.
            description: Description to add for the start request.
            timeout: Timeout in seconds.

        Returns:
            ChangeControlConfig object including any server-generated values.
        """
        request = ChangeControlConfigSetRequest(
            value=ChangeControlConfig(
                key=ChangeControlKey(id=change_control_id),
                start=FlagConfig(value=True, notes=description),
            ),
        )
        client = ChangeControlConfigServiceStub(self._channel)

        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Change Control ID '{change_control_id}'") or e

        return response.value

    async def wait_for_change_control_state(
        self: CVClientProtocol,
        cc_id: str,
        state: Literal["completed", "unspecified", "running", "scheduled"],
        timeout: float = 3600.0,
    ) -> ChangeControl:
        """
        Monitor a Change control using arista.changecontrol.v1.ChangeControlService.Subscribe API for a response to the given cc_id.

        Blocks until a response is returned or timed out.

        Parameters:
            cc_id: Unique identifier of the change control.
            state: Change Control state to wait for.
            timeout: Timeout in seconds for the Change Control to reach the expected state.

        Returns:
            Full change control object
        """
        request = ChangeControlStreamRequest(
            partial_eq_filter=[
                ChangeControl(
                    key=ChangeControlKey(id=cc_id),
                ),
            ],
        )
        client = ChangeControlServiceStub(self._channel)
        try:
            responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                LOGGER.debug("wait_for_change_control_complete: Response is '%s.'", response)
                if hasattr(response, "value") and response.value.status == CHANGE_CONTROL_STATUS_MAP[state]:
                    LOGGER.info("wait_for_change_control_complete: Got response for request '%s': %s", cc_id, response.value.status)
                    return response.value
                LOGGER.debug("wait_for_change_control_complete: Status of change control is '%s.'", response)

        except Exception as e:
            raise get_cv_client_exception(e, f"CC ID '{cc_id}')") or e
