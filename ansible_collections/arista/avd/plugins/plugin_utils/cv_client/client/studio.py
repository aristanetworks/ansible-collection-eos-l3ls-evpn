# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Literal

from ..api.arista.studio.v1 import (
    DeviceInfo,
    Inputs,
    InputsConfig,
    InputsConfigServiceStub,
    InputsConfigSetRequest,
    InputsConfigStreamRequest,
    InputsKey,
    InputsRequest,
    InputsServiceStub,
    TopologyInput,
    TopologyInputConfig,
    TopologyInputConfigServiceStub,
    TopologyInputConfigSetSomeRequest,
    TopologyInputKey,
    TopologyInputServiceStub,
    TopologyInputStreamRequest,
)
from ..api.fmp import RepeatedString
from .exceptions import CVResourceNotFound, get_cv_client_exception

if TYPE_CHECKING:
    from .cv_client import CVClient

TOPOLOGY_STUDIO_ID = "TOPOLOGY"


class StudioMixin:
    """
    Only to be used as mixin on CVClient class.
    """

    studio_api_version: Literal["v1"] = "v1"

    async def get_studio_inputs(
        self: CVClient,
        studio_id: str,
        workspace_id: str,
        input_path: list[str] | None = None,
        time: datetime = None,
        timeout: float = 10.0,
    ) -> Inputs:
        """
        Get Studio Inputs using arista.studio.v1.InputsService.GetOne and arista.studio.v1.InputsConfigServer.GetAll APIs.

        The Studio Inputs GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the Workspace Studio Inputs we need to fetch from the workspace, and if we find nothing, we need to check if inputs
        got deleted in the workspace by retrieving config. Finally we can fetch from mainline.

        Parameters:
            studio_id: Unique identifier for the studio.
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            input_path: Data elements leading to specific inputs. Returning all inputs if not given.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        TODO: Refactor to fetch inputs with GetAll so we can stream larger input sets. Issue is to reassemble all this data.

        Returns:
            Inputs object.
        """
        request = InputsRequest(
            # First attempt to fetch inputs from workspace.
            key=InputsKey(
                studio_id=studio_id,
                workspace_id=workspace_id,
                path=RepeatedString(values=input_path),
            ),
            time=time,
        )
        client = InputsServiceStub(self._channel)
        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
            # We only get a response if the inputs are set/changed in the workspace.
            return response.value
        except Exception as e:
            e = get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e
            if isinstance(e, CVResourceNotFound) and workspace_id != "":
                # Ignore this error, since it simply means we have to check if inputs got deleted in this workspace or fetch from mainline as last resort.
                # Saving the error for raising in case the inputs was deleted.
                not_found_error = e
                pass
            else:
                raise e

        # Next up fetch the inputs config from the workspace to see if the inputs was deleted in this workspace.
        request = InputsConfigStreamRequest(
            partial_eq_filter=InputsConfig(key=InputsKey(studio_id=studio_id, workspace_id=workspace_id, path=input_path), remove=True),
            time=time,
        )
        client = InputsConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                # If we get here it means we got an entry with "removed: True" so no need to look further.
                # So we will raise since we have no inputs for the studio. Reusing the error with correct grpc error context.
                raise not_found_error

        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e

        # If we get here, it means there are no inputs in the workspace and they are not deleted, so we can fetch from mainline.
        request = InputsRequest(
            # Notice using workspace="" for mainline.
            key=InputsKey(
                studio_id=studio_id,
                workspace_id="",
                path=RepeatedString(values=input_path),
            ),
            time=time,
        )
        client = InputsServiceStub(self._channel)
        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
            # We only get a response if the inputs are set in mainline.
            return response.value
        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e

    async def set_studio_inputs(
        self: CVClient,
        studio_id: str,
        workspace_id: str,
        inputs: str | None = None,
        input_path: list[str] | None = None,
        timeout: float = 10.0,
    ) -> InputsConfig:
        """
        Set Studio Inputs using arista.studio.v1.InputsConfigService.Set API.

        Parameters:
            studio_id: Unique identifier for the studio.
            workspace_id: Unique identifier of the Workspace for which the information is set.
            inputs: JSON encoded string with data to set at the given path.
            input_path: Data path elements for setting specific inputs. Set at the root, replacing all inputs if not given.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        TODO: Refactor to fetch inputs with GetAll so we can stream larger input sets. Issue is to reassemble all this data.

        Returns:
            InputsConfig object after being set including any server-generated values.
        """
        request = InputsConfigSetRequest(
            InputsConfig(
                key=InputsKey(
                    studio_id=studio_id,
                    workspace_id=workspace_id,
                    path=RepeatedString(values=input_path),
                ),
                inputs=inputs,
            )
        )
        client = InputsConfigServiceStub(self._channel)
        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
            return response.value

        except Exception as e:
            raise get_cv_client_exception(e, f"Studio ID '{studio_id}, Workspace ID '{workspace_id}', Path '{input_path}'") or e

    async def get_topology_studio_inputs(
        self: CVClient,
        workspace_id: str,
        device_ids: list[str] | None = None,
        time: datetime = None,
        timeout: float = 10.0,
    ) -> list[TopologyInput]:
        """
        Get Topology Studio Inputs using arista.studio.v1.TopologyInputsService.GetAll and arista.studio.v1.TopologyInputsConfigService.GetAll APIs.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            device_ids: List of Device IDs / Serial numbers to get inputs for.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Inputs object.
        """
        request = TopologyInputStreamRequest(partial_eq_filter=[], time=time)
        if device_ids:
            for device_id in device_ids:
                request.partial_eq_filter.append(
                    TopologyInput(
                        key=TopologyInputKey(workspace_id=workspace_id, device_id=device_id),
                    )
                )
        else:
            request.partial_eq_filter.append(
                TopologyInput(
                    key=TopologyInputKey(workspace_id=workspace_id),
                )
            )
        client = TopologyInputServiceStub(self._channel)
        topology_inputs = []
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                topology_inputs.append(response.value)
            return topology_inputs
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Device IDs '{device_ids}'") or e

    async def set_topology_studio_inputs(
        self: CVClient,
        workspace_id: str,
        device_inputs: list[tuple[str, str]],
        timeout: float = 10.0,
    ) -> list[TopologyInputKey]:
        """
        Set Topology Studio Inputs using arista.studio.v1.TopologyInputsConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            device_inputs: List of Tuples with the format (<device_id>, <hostname>).
            timeout: Timeout in seconds.

        Returns:
            TopologyInputKey objects after being set including any server-generated values.
        """
        request = TopologyInputConfigSetSomeRequest(
            values=[
                TopologyInputConfig(
                    key=TopologyInputKey(workspace_id=workspace_id, device_id=device_id),
                    device_info=DeviceInfo(device_id=device_id, hostname=hostname),
                )
                for device_id, hostname in device_inputs
            ]
        )

        client = TopologyInputConfigServiceStub(self._channel)
        topology_input_keys = []
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                topology_input_keys.append(response.key)
            return topology_input_keys

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Device IDs '{device_inputs}'") or e
