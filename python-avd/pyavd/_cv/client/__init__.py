# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl
from typing import TYPE_CHECKING

from grpclib.client import Channel
from requests import JSONDecodeError, get, post

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .exceptions import CVClientException
from .inventory import InventoryMixin
from .studio import StudioMixin
from .swg import SwgMixin
from .tag import TagMixin
from .utils import UtilsMixin
from .versioning import CvVersion
from .workspace import WorkspaceMixin

if TYPE_CHECKING:
    from types import TracebackType
    from typing import Self


class CVClient(
    ChangeControlMixin,
    ConfigletMixin,
    InventoryMixin,
    StudioMixin,
    SwgMixin,
    TagMixin,
    UtilsMixin,
    WorkspaceMixin,
):
    _channel: Channel | None = None
    _metadata: dict
    _servers: list[str]
    _port: int
    _verify_certs: bool
    _token: str | None
    _username: str | None
    _password: str | None
    _cv_version: CvVersion | None = None

    def __init__(
        self,
        servers: str | list[str],
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        port: int = 443,
        verify_certs: bool = True,
    ) -> None:
        """
        CVClient is a high-level API library for using CloudVision Resource APIs.

        Use CVClient as an async context manager like:
            `async with CVClient(servers="myserver", token="mytoken") as cv_client:`

        Parameters:
            servers: A single FQDN for CVaaS or a list of FQDNs for one CVP cluster.
            token: Token defined in CloudVision under service-accounts.
            username: Username to use for authentication if token is not set.
            password: Password to use for authentication if token is not set.
            port: TCP port to use for the connection.
            verify_certs: Disables SSL certificate verification if set to False. Not recommended for production.
        """
        if isinstance(servers, list):
            self._servers = servers
        else:
            self._servers = [servers]

        self._port = port
        self._token = token
        self._username = username
        self._password = password
        self._verify_certs = verify_certs

    async def __aenter__(self) -> Self:
        """Using asynchronous context manager since grpclib must be initialized inside an asyncio loop."""
        self._connect()
        return self

    async def __aexit__(self, _exc_type: type[BaseException] | None, _exc_val: BaseException | None, _exc_tb: TracebackType | None) -> None:
        self._channel.close()
        self._channel = None

    def _connect(self) -> None:
        # TODO: Verify connection
        # TODO: Handle multinode clusters

        # Ensure that the default ssl context is initialized before doing any requests.
        ssl_context = self._ssl_context()

        if not self._token:
            self._set_token()

        self._set_version()

        if self._channel is None:
            self._channel = Channel(host=self._servers[0], port=self._port, ssl=ssl_context)

        self._metadata = {"authorization": "Bearer " + self._token}

    def _ssl_context(self) -> ssl.SSLContext | bool:
        """
        Initialize the default SSL context with relaxed verification if needed.

        Otherwise we just return True.
        The return value (The default ssl context or True) will be passed to grpclib.
        Requests will pick it up from ssl lib itself.
        """
        if not self._verify_certs:
            # Accepting SonarLint issue: We are purposely implementing no verification of certs.
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  # NOSONAR
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # NOSONAR
            context.set_alpn_protocols(["h2"])
        else:
            context = True
        return context

    def _set_token(self) -> None:
        """
        Uses username/password for authenticating via REST.

        Sets the session token into self._token to be used for gRPC channel.

        TODO: Handle multinode clusters
        """
        if self._token:
            return

        if not self._username or not self._password:
            msg = "Unable to authenticate. Missing token or username/password."
            raise CVClientException(msg)

        try:
            response = post(  # noqa: S113 TODO: Add configurable timeout
                "https://" + self._servers[0] + "/cvpservice/login/authenticate.do",
                auth=(self._username, self._password),
                verify=self._verify_certs,
                json={},
            )

            self._token = response.json()["sessionId"]
        except (KeyError, JSONDecodeError) as e:
            msg = "Unable to get token from CloudVision server. Please supply service account token instead of username/password."
            raise CVClientException(msg) from e

    def _set_version(self) -> None:
        """
        Fetch the CloudVision version via REST and set self._cv_version.

        This version is used to decide which APIs to use later.

        TODO: Handle multinode clusters
        """
        if not self._token:
            msg = "Unable to get version from CloudVision server. Missing token."
            raise CVClientException(msg)

        try:
            response = get(  # noqa: S113 TODO: Add configurable timeout
                "https://" + self._servers[0] + "/cvpservice/cvpInfo/getCvpInfo.do",
                headers={"Authorization": f"Bearer {self._token}"},
                verify=self._verify_certs,
                json={},
            )

            self._cv_version = CvVersion(response.json()["version"])
        except (KeyError, JSONDecodeError) as e:
            msg = f"Unable to get version from CloudVision server. Got {response.text}"
            raise CVClientException(msg) from e
