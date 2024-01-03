# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: arista/redirector.v1/redirector.proto, arista/redirector.v1/services.gen.proto
# plugin: python-aristaproto
# This file has been @generated

from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Dict,
    List,
    Optional,
)

import aristaproto
import grpclib
from aristaproto.grpc.grpclib_server import ServiceBase

from .... import fmp as ___fmp__
from ... import (
    subscriptions as __subscriptions__,
    time as __time__,
)


if TYPE_CHECKING:
    import grpclib.server
    from aristaproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class AssignmentKey(aristaproto.Message):
    """AssignmentKey allows to uniquely identify an assignment."""

    system_id: Optional[str] = aristaproto.message_field(
        1, wraps=aristaproto.TYPE_STRING
    )
    """system_id is the unique identifier of a device."""


@dataclass(eq=False, repr=False)
class Assignment(aristaproto.Message):
    """
    Assignment returns the information about the regional clusters that the
     system is assigned to. Each cluster consists of a series of hosts, each of
     which the client can use to connect.
    """

    key: "AssignmentKey" = aristaproto.message_field(1)
    """key uniquely identifies the assignment of system_id to the cluster."""

    clusters: "Clusters" = aristaproto.message_field(2)
    """clusters that the system is assigned to."""


@dataclass(eq=False, repr=False)
class Clusters(aristaproto.Message):
    """
    Clusters wraps a cluster list which contain the information about the hosts.
    """

    values: List["Cluster"] = aristaproto.message_field(2)
    """values contains the list of clusters associated with the region"""


@dataclass(eq=False, repr=False)
class Cluster(aristaproto.Message):
    name: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """
    name of the cluster. The name can change over time as new clusters
     are added or removed.
    """

    hosts: "___fmp__.RepeatedString" = aristaproto.message_field(2)
    """hosts in the cluster that the devices can connect to."""


@dataclass(eq=False, repr=False)
class AssignmentRequest(aristaproto.Message):
    key: "AssignmentKey" = aristaproto.message_field(1)
    """
    Key uniquely identifies a Assignment instance to retrieve.
     This value must be populated.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the time for which you are interested in the data.
     If no time is given, the server will use the time at which it makes the request.
    """


@dataclass(eq=False, repr=False)
class AssignmentResponse(aristaproto.Message):
    value: "Assignment" = aristaproto.message_field(1)
    """
    Value is the value requested.
     This structure will be fully-populated as it exists in the datastore. If
     optional fields were not given at creation, these fields will be empty or
     set to default values.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time carries the (UTC) timestamp of the last-modification of the
     Assignment instance in this response.
    """


@dataclass(eq=False, repr=False)
class AssignmentStreamRequest(aristaproto.Message):
    partial_eq_filter: List["Assignment"] = aristaproto.message_field(1)
    """
    PartialEqFilter provides a way to server-side filter a GetAll/Subscribe.
     This requires all provided fields to be equal to the response.

     While transparent to users, this field also allows services to optimize internal
     subscriptions if filter(s) are sufficiently specific.
    """

    time: "__time__.TimeBounds" = aristaproto.message_field(3)
    """
    TimeRange allows limiting response data to within a specified time window.
     If this field is populated, at least one of the two time fields are required.

     This field is not allowed in the Subscribe RPC.
    """


@dataclass(eq=False, repr=False)
class AssignmentStreamResponse(aristaproto.Message):
    value: "Assignment" = aristaproto.message_field(1)
    """
    Value is a value deemed relevant to the initiating request.
     This structure will always have its key-field populated. Which other fields are
     populated, and why, depends on the value of Operation and what triggered this notification.
    """

    time: datetime = aristaproto.message_field(2)
    """Time holds the timestamp of this Assignment's last modification."""

    type: "__subscriptions__.Operation" = aristaproto.enum_field(3)
    """
    Operation indicates how the Assignment value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """


class AssignmentServiceStub(aristaproto.ServiceStub):
    async def get_one(
        self,
        assignment_request: "AssignmentRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "AssignmentResponse":
        return await self._unary_unary(
            "/arista.redirector.v1.AssignmentService/GetOne",
            assignment_request,
            AssignmentResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_all(
        self,
        assignment_stream_request: "AssignmentStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["AssignmentStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.redirector.v1.AssignmentService/GetAll",
            assignment_stream_request,
            AssignmentStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def subscribe(
        self,
        assignment_stream_request: "AssignmentStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["AssignmentStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.redirector.v1.AssignmentService/Subscribe",
            assignment_stream_request,
            AssignmentStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class AssignmentServiceBase(ServiceBase):
    async def get_one(
        self, assignment_request: "AssignmentRequest"
    ) -> "AssignmentResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_all(
        self, assignment_stream_request: "AssignmentStreamRequest"
    ) -> AsyncIterator["AssignmentStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe(
        self, assignment_stream_request: "AssignmentStreamRequest"
    ) -> AsyncIterator["AssignmentStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_one(
        self, stream: "grpclib.server.Stream[AssignmentRequest, AssignmentResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_one(request)
        await stream.send_message(response)

    async def __rpc_get_all(
        self,
        stream: "grpclib.server.Stream[AssignmentStreamRequest, AssignmentStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_all,
            stream,
            request,
        )

    async def __rpc_subscribe(
        self,
        stream: "grpclib.server.Stream[AssignmentStreamRequest, AssignmentStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/arista.redirector.v1.AssignmentService/GetOne": grpclib.const.Handler(
                self.__rpc_get_one,
                grpclib.const.Cardinality.UNARY_UNARY,
                AssignmentRequest,
                AssignmentResponse,
            ),
            "/arista.redirector.v1.AssignmentService/GetAll": grpclib.const.Handler(
                self.__rpc_get_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                AssignmentStreamRequest,
                AssignmentStreamResponse,
            ),
            "/arista.redirector.v1.AssignmentService/Subscribe": grpclib.const.Handler(
                self.__rpc_subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                AssignmentStreamRequest,
                AssignmentStreamResponse,
            ),
        }
