# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import get_event_loop
from functools import partial
from json import JSONDecodeError, loads
from logging import getLogger
from typing import TYPE_CHECKING
from urllib.error import HTTPError

from ansible.errors import AnsibleActionFail, AnsibleConnectionFailure
from ansible.module_utils.connection import ConnectionError as AnsibleConnectionError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse

PLUGIN_NAME = "arista.avd.eos_validate_state"

try:
    from pyavd._errors import AristaAvdError
except ImportError as e:
    AristaAvdError = RaiseOnUse(
        AnsibleActionFail(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

logger = getLogger(__name__)

try:
    from anta import __DEBUG__
    from anta.device import AntaDevice
    from anta.logger import anta_log_exception, exc_to_str

    HAS_ANTA = True
except ImportError:
    HAS_ANTA = False
    # Next line to make ansible-test sanity happy
    AntaDevice = object

if TYPE_CHECKING:
    from collections.abc import Generator

    from ansible.plugins.connection import ConnectionBase
    from anta.models import AntaCommand

ANSIBLE_EOS_PLUGIN_NAME = "ansible_collections.arista.eos.plugins.httpapi.eos"


class AnsibleEOSDevice(AntaDevice):
    """Implementation of an AntaDevice using Ansible HttpApi plugin for EOS."""

    def __init__(self, name: str, connection: ConnectionBase, tags: list | None = None, *, check_mode: bool = False) -> None:
        """Initialize an instance of the AnsibleEOSDevice class.

        Args:
        ----
            name (str): Name of the AnsibleEOSDevice instance.
            connection (ConnectionBase): An instance of Ansible ConnectionBase. It must utilize the EOS HttpApi plugin to manage the device's connection.
            tags (list, optional): A list of tags associated with the device. Defaults to None.
            check_mode (bool, optional): If True, initializes the class in check mode. Defaults to False.

        Attributes:
        ----------
            check_mode (bool): Flag indicating if the class is operating in check mode.
            _connection (ConnectionBase): An instance of ConnectionBase using the EOS HttpApi plugin for device connection management.

        Raises:
        ------
            AristaAvdError: Raised if ANTA is not imported or if the provided Ansible connection does not use the EOS HttpApi plugin.
        """
        if not HAS_ANTA:
            raise AristaAvdError(message="AVD could not import the required 'anta' Python library")

        super().__init__(name, tags, disable_cache=False)
        self.check_mode = check_mode

        # Check the ansible connection is defined
        if not self.check_mode and not hasattr(connection, "_sub_plugin"):
            raise AristaAvdError(
                message="AVD could not determine the Ansible connection plugin used. "
                "Please ensure that the 'ansible_network_os' and 'ansible_connection' variables are set to 'eos' and 'httpapi' respectively for this host.",
            )
        # In check_mode we don't care that we cannot connect to the device
        if self.check_mode or (plugin_name := connection._sub_plugin.get("name")) == ANSIBLE_EOS_PLUGIN_NAME:
            self._connection = connection
        else:
            raise AristaAvdError(
                message=f"The provided Ansible connection does not use EOS HttpApi plugin: {plugin_name}. "
                "Please ensure that the 'ansible_network_os' and 'ansible_connection' variables are set to 'eos' and 'httpapi' respectively for this host.",
            )

    @property
    def _keys(self) -> tuple:
        """Keys used to implement hashing and equality for an AntaDevice instance."""
        return (self._connection._options.get("host"), self._connection._options.get("use_ssl"), self._connection._options.get("network_os"))

    def __rich_repr__(self) -> Generator:
        """Implement Rich Repr Protocol."""
        connection_vars = vars(self._connection)
        if "_defs" in connection_vars:
            del connection_vars["_defs"]
        yield from super().__rich_repr__()
        if __DEBUG__:
            yield "_connection", connection_vars

    async def _collect(self, command: AntaCommand, *, collection_id: str | None = None) -> None:  # noqa: ARG002
        """Collect device command result using Ansible HttpApi connection plugin.

        Supports outformat 'json' and 'text' as output structure.

        Args:
        ----
            command (AntaCommand): The command to collect.

        Keyword Args:
        -------------
            collection_id (str, optional): This parameter is not used in this implementation. Defaults to None.
        """
        if self.check_mode:
            logger.info("_collect was called in check_mode, doing nothing")
            return
        commands = []

        if command.revision:
            commands.append({"cmd": command.command, "revision": command.revision})
        else:
            commands.append({"cmd": command.command})

        # Run the synchronous function send_request() in a separate thread to not block the asyncio event loop
        send_request = partial(self._connection.send_request, commands, version=command.version, output=command.ofmt)
        loop = get_event_loop()
        try:
            response = await loop.run_in_executor(None, send_request)

            # Save the command result
            command.output = loads(response) if command.ofmt == "json" else response
        except JSONDecodeError:
            # Even if the outformat is 'json' send_request() sometimes returns a non-valid JSON depending on the output content
            # https://github.com/ansible-collections/arista.eos/blob/main/plugins/httpapi/eos.py#L194
            command.output = {"messages": [response]}
        except Exception as e:
            command.errors = [exc_to_str(e)]
            logger.warning("Command '%s' failed: %s", command.command, exc_to_str(e))
        logger.debug("%s: %s", self.name, command)

    async def refresh(self) -> None:
        """Update attributes of an AnsibleEOSDevice instance.

        This coroutine must update the following attributes of AnsibleEOSDevice:
        - is_online: When a device IP is reachable and a port can be open
        - established: When a command execution succeeded
        - hw_model: The hardware model of the device

        On `get_device_info()` failure:
        - The exception is caught and logged locally
        - The exception won't be propagated to ANTA
        - The task will fail per the logger handler and the play for the device will stop
        """
        logger.debug("Refreshing device %s", self.name)
        if self.check_mode:
            logger.info("Refresh was called in check_mode, doing nothing")
            return

        try:
            device_info = self._connection.get_device_info()
        except (AnsibleConnectionFailure, HTTPError) as e:
            message = "Failed to connect to device"
            anta_log_exception(e, message, logger)
        except AnsibleConnectionError as e:
            message = "Error while getting the device information"
            anta_log_exception(e, message, logger)
        else:
            self.is_online = self._connection.connected
            self.hw_model = device_info["network_os_model"]

        self.established = bool(self.is_online and self.hw_model)
