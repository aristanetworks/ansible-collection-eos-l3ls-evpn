# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.configlet.v1 import (
    Configlet,
    ConfigletAssignment,
    ConfigletAssignmentConfig,
    ConfigletAssignmentConfigServiceStub,
    ConfigletAssignmentConfigSetRequest,
    ConfigletAssignmentConfigSetSomeRequest,
    ConfigletAssignmentKey,
    ConfigletAssignmentServiceStub,
    ConfigletAssignmentStreamRequest,
    ConfigletConfig,
    ConfigletConfigServiceStub,
    ConfigletConfigSetRequest,
    ConfigletConfigSetSomeRequest,
    ConfigletKey,
    ConfigletServiceStub,
    ConfigletStreamRequest,
    MatchPolicy,
)
from pyavd._cv.api.arista.time import TimeBounds
from pyavd._cv.api.fmp import RepeatedString
from pyavd._utils import batch

from .async_decorators import LimitCvVersion, grpc_msg_size_handler
from .constants import DEFAULT_API_TIMEOUT
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol


ASSIGNMENT_MATCH_POLICY_MAP = {
    "match_first": MatchPolicy.MATCH_FIRST,
    "match_all": MatchPolicy.MATCH_ALL,
    None: MatchPolicy.UNSPECIFIED,
}
PARALLEL_COROUTINES = 20

LOGGER = getLogger(__name__)


class ConfigletMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    configlet_api_version: Literal["v1"] = "v1"

    async def get_configlet_containers(
        self: CVClientProtocol,
        workspace_id: str,
        container_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletAssignment]:
        """
        Get Configlet Containers (a.k.a. Assignments) using arista.configlet.v1.ConfigletAssignmentServiceStub.GetAll API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            container_ids: Unique identifiers for Containers/Assignments.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignment objects.
        """
        request = ConfigletAssignmentStreamRequest(partial_eq_filter=[], time=TimeBounds(start=None, end=time))
        if container_ids:
            for container_id in container_ids:
                request.partial_eq_filter.append(
                    ConfigletAssignment(key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=container_id)),
                )
        else:
            request.partial_eq_filter.append(ConfigletAssignment(key=ConfigletAssignmentKey(workspace_id=workspace_id)))

        client = ConfigletAssignmentServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            configlet_assignments = [response.value async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', ConfigletAssignment ID '{container_ids}'") or e

        return configlet_assignments

    async def set_configlet_container(
        self: CVClientProtocol,
        workspace_id: str,
        container_id: str,
        display_name: str | None = None,
        description: str | None = None,
        configlet_ids: list[str] | None = None,
        query: str | None = None,
        child_assignment_ids: list[str] | None = None,
        match_policy: Literal["match_first", "match_all"] = "match_all",
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletAssignmentConfig:
        """
        Create/update a Configlet Container (a.k.a. Assignment) using arista.configlet.v1.ConfigletAssignmentServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            container_id: Unique identifier for Container/Assignment.
            display_name: Container/Assignment Name.
            description: Container/Assignment description.
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignmentConfig object after being set including any server-generated values.
        """
        request = ConfigletAssignmentConfigSetRequest(
            value=ConfigletAssignmentConfig(
                key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=container_id),
                display_name=display_name,
                description=description,
                configlet_ids=RepeatedString(values=configlet_ids),
                query=query,
                child_assignment_ids=RepeatedString(values=child_assignment_ids),
                match_policy=ASSIGNMENT_MATCH_POLICY_MAP.get(match_policy or "match_all"),
            ),
        )
        client = ConfigletAssignmentConfigServiceStub(self._channel)
        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', ConfigletAssignment ID '{container_id}'") or e

        return response.value

    @LimitCvVersion(min_ver="2024.2.0")
    @grpc_msg_size_handler("containers")
    async def set_configlet_containers(
        self: CVClientProtocol,
        workspace_id: str,
        containers: list[tuple[str, str | None, str | None, list[str] | None, str | None, list[str] | None, str | None]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletAssignmentKey]:
        """
        Create/update a Configlet Container (a.k.a. Assignment) using arista.configlet.v1.ConfigletAssignmentServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            containers: List of Tuples with the format\
                (container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy).
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignmentKey objects after being set including any server-generated values.
        """
        request = ConfigletAssignmentConfigSetSomeRequest(
            values=[
                ConfigletAssignmentConfig(
                    key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=container_id),
                    display_name=display_name,
                    description=description,
                    configlet_ids=RepeatedString(values=configlet_ids),
                    query=query,
                    child_assignment_ids=RepeatedString(values=child_assignment_ids),
                    match_policy=ASSIGNMENT_MATCH_POLICY_MAP.get(match_policy or "match_all"),
                )
                for container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy in containers
            ],
        )
        client = ConfigletAssignmentConfigServiceStub(self._channel)
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
            assignment_keys = [response.key async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Containers '{containers}'") or e

        return assignment_keys

    # Use this variant for versions below 2024.2.0 (still respecting overall min version)
    @LimitCvVersion(max_ver="2024.1.99")
    async def set_configlet_containers(  # noqa: F811 - Redefining with decorator.
        self: CVClientProtocol,
        workspace_id: str,
        containers: list[tuple[str, str | None, str | None, list[str] | None, str | None, list[str] | None, str | None]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletAssignmentKey]:
        """
        Create batches of containers and do parallel calls to set_configlet_container for each batch.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            containers: List of Tuples with the format\
                (container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy).
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignmentKey objects after being set including any server-generated values.
        """
        coroutines = [
            self.set_configlet_container(
                workspace_id=workspace_id,
                container_id=container_id,
                display_name=display_name,
                description=description,
                configlet_ids=configlet_ids,
                query=query,
                child_assignment_ids=child_assignment_ids,
                match_policy=match_policy,
                timeout=timeout,
            )
            for container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy in containers
        ]

        configlet_configs = []

        LOGGER.info("set_configlet_containers: Deploying %s configlet assignments / containers in batches of %s.", len(coroutines), PARALLEL_COROUTINES)
        for index, batch_coroutines in enumerate(batch(coroutines, PARALLEL_COROUTINES), start=1):
            LOGGER.info("set_configlet_containers: Batch %s", index)
            configlet_configs.extend(await gather(*batch_coroutines))

        return [
            await self.set_configlet_container(
                workspace_id, container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy, timeout
            )
            for container_id, display_name, description, configlet_ids, query, child_assignment_ids, match_policy in containers
        ]

    async def delete_configlet_container(
        self: CVClientProtocol,
        workspace_id: str,
        assignment_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletAssignmentConfig:
        """
        Delete a Configlet Container (a.k.a. Assignment) using arista.configlet.v1.ConfigletAssignmentServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            assignment_id: Unique identifier for Container/Assignment.

        Returns:
            ConfigletAssignmentConfig object after being set including any server-generated values.
        """
        request = ConfigletAssignmentConfigSetRequest(
            value=ConfigletAssignmentConfig(
                key=ConfigletAssignmentKey(workspace_id=workspace_id, configlet_assignment_id=assignment_id),
                remove=True,
            ),
        )
        client = ConfigletAssignmentConfigServiceStub(self._channel)
        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', ConfigletAssignment ID '{assignment_id}'") or e

        return response.value

    @grpc_msg_size_handler("configlet_ids")
    async def get_configlets(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_ids: list[str] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[Configlet]:
        """
        Get Configlets using arista.configlet.v1.ConfigletServiceStub.GetAll API.

        Missing objects will not produce an error.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            configlet_ids: Unique identifiers for Configlets. If not set the function will return all configlets.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            List of matching Configlet objects.
        """
        request = ConfigletStreamRequest(partial_eq_filter=[], time=TimeBounds(start=None, end=time))
        if configlet_ids:
            for configlet_id in configlet_ids:
                request.partial_eq_filter.append(Configlet(key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id)))
        else:
            request.partial_eq_filter.append(Configlet(key=ConfigletKey(workspace_id=workspace_id)))

        client = ConfigletServiceStub(self._channel)

        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            configlets = [response.value async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Configlet IDs '{configlet_ids}'") or e

        return configlets

    async def set_configlet(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_id: str,
        display_name: str | None = None,
        description: str | None = None,
        body: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletConfig:
        """
        Create/update a Configlet using arista.configlet.v1.ConfigletServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlet_id: Unique identifier for Configlet.
            display_name: Configlet Name.
            description: Configlet description.
            body: EOS Configuration.
            timeout: Timeout in seconds.

        Returns:
            ConfigletAssignment object after being set including any server-generated values.
        """
        request = ConfigletConfigSetRequest(
            value=ConfigletConfig(
                key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                display_name=display_name,
                description=description,
                body=body,
            ),
        )
        client = ConfigletConfigServiceStub(self._channel)
        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Configlet ID '{configlet_id}'") or e

        return response.value

    async def set_configlet_from_file(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_id: str,
        file: str,
        display_name: str | None = None,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> ConfigletConfig:
        """
        Create/update a Configlet using arista.configlet.v1.ConfigletServiceStub.Set API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlet_id: Unique identifier for Configlet.
            file: Path to file containing EOS Configuration.
            display_name: Configlet Name.
            description: Configlet description.
            timeout: Timeout in seconds.

        Returns:
            ConfigletConfig object after being set including any server-generated values.
        """
        request = ConfigletConfigSetRequest(
            value=ConfigletConfig(
                key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                display_name=display_name,
                description=description,
                body=Path(file).read_text(encoding="UTF-8"),
            ),
        )
        client = ConfigletConfigServiceStub(self._channel)
        try:
            response = await client.set(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Configlet ID '{configlet_id}', File '{file}'") or e

        return response.value

    @LimitCvVersion(min_ver="2024.2.0")
    @grpc_msg_size_handler("configlets")
    async def set_configlets_from_files(
        self: CVClientProtocol,
        workspace_id: str,
        configlets: list[tuple[str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletKey]:
        """
        Create/update multiple Configlets using arista.configlet.v1.ConfigletServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlets: List of Tuples with the format `(configlet_id, display_name, description, path_to_config_file)`.
            timeout: Timeout in seconds.

        Returns:
            List of ConfigletConfig objects after being set including any server-generated values.
        """
        request = ConfigletConfigSetSomeRequest(values=[])
        for configlet in configlets:
            configlet_id, display_name, description, file = configlet
            request.values.append(
                ConfigletConfig(
                    key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                    display_name=display_name,
                    description=description,
                    body=Path(file).read_text(encoding="UTF-8"),
                )
            )
        client = ConfigletConfigServiceStub(self._channel)

        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
            configlet_configs = [response.key async for response in responses]

        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Configlets '{configlets}'") or e

        return configlet_configs

    # Use this variant for versions below 2024.2.0 (still respecting overall min version)
    @LimitCvVersion(max_ver="2024.1.99")
    async def set_configlets_from_files(  # noqa: F811 - Redefining with decorator.
        self: CVClientProtocol,
        workspace_id: str,
        configlets: list[tuple[str, str]],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletKey]:
        """
        Create batches of configlets and do parallel calls to set_configlet_from_file for each batch.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlets: List of Tuples with the format `(configlet_id, display_name, description, path_to_config_file)`.
            timeout: Timeout in seconds.

        Returns:
            List of ConfigletConfig objects after being set including any server-generated values.
        """
        coroutines = [
            self.set_configlet_from_file(
                workspace_id=workspace_id,
                configlet_id=configlet_id,
                file=file,
                display_name=display_name,
                description=description,
                timeout=timeout,
            )
            for configlet_id, display_name, description, file in configlets
        ]

        configlet_configs = []

        LOGGER.info("set_configlets_from_files: Deploying %s configlets in batches of %s.", len(coroutines), PARALLEL_COROUTINES)
        for index, batch_coroutines in enumerate(batch(coroutines, PARALLEL_COROUTINES), start=1):
            LOGGER.info("set_configlets_from_files: Batch %s", index)
            configlet_configs.extend(await gather(*batch_coroutines))

    @grpc_msg_size_handler("configlet_ids")
    async def delete_configlets(
        self: CVClientProtocol,
        workspace_id: str,
        configlet_ids: list[str],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[ConfigletKey]:
        """
        Delete a Configlet using arista.configlet.v1.ConfigletServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            configlet_ids: List of unique identifiers for Configlets to delete.
            timeout: Timeout in seconds.

        Returns:
            List of ConfigletKey objects after being deleted including any server-generated values.
        """
        request = ConfigletConfigSetSomeRequest(values=[])
        for configlet_id in configlet_ids:
            request.values.append(
                ConfigletConfig(
                    key=ConfigletKey(workspace_id=workspace_id, configlet_id=configlet_id),
                    remove=True,
                ),
            )
        client = ConfigletConfigServiceStub(self._channel)

        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout)
            configlet_configs = [response.key async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Configlet IDs '{configlet_ids}'") or e

        return configlet_configs
