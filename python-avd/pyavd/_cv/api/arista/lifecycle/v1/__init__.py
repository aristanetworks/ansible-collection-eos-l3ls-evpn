# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: arista/lifecycle.v1/lifecycle.proto, arista/lifecycle.v1/services.gen.proto
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
class DeviceLifecycleSummaryKey(aristaproto.Message):
    """
    DeviceLifecycleSummaryKey is the key type for
     DeviceLifecycleSummary model
    """

    device_id: Optional[str] = aristaproto.message_field(
        1, wraps=aristaproto.TYPE_STRING
    )
    """device_id is the device ID"""


@dataclass(eq=False, repr=False)
class SoftwareEol(aristaproto.Message):
    """SoftwareEOL represents a software end of life"""

    version: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """version of a SoftwareEOL"""

    end_of_support: datetime = aristaproto.message_field(2)
    """end_of_support of a SoftwareEOL"""


@dataclass(eq=False, repr=False)
class DateAndModels(aristaproto.Message):
    """
    DateAndModels has an "end of" date along with
     the models that has this exact "end of" date
    """

    date: datetime = aristaproto.message_field(1)
    """end of" date"""

    models: "___fmp__.MapStringInt32" = aristaproto.message_field(2)
    """
    models with this exact "end of" date
     mapped to its count
    """


@dataclass(eq=False, repr=False)
class HardwareLifecycleSummary(aristaproto.Message):
    """HardwareLifecycleSummary represents a hardware lifecycle summary"""

    end_of_life: "DateAndModels" = aristaproto.message_field(1)
    """end_of_life of a HardwareLifecycleSummary"""

    end_of_sale: "DateAndModels" = aristaproto.message_field(2)
    """end_of_sale of a HardwareLifecycleSummary"""

    end_of_tac_support: "DateAndModels" = aristaproto.message_field(3)
    """end_of_tac_support of a HardwareLifecycleSummary"""

    end_of_hardware_rma_requests: "DateAndModels" = aristaproto.message_field(4)
    """end_of_hardware_rma_requests of a HardwareLifecycleSummary"""


@dataclass(eq=False, repr=False)
class DeviceLifecycleSummary(aristaproto.Message):
    """
    DeviceLifecycleSummary is the state model that represents
     the lifecycle summary of a device
    """

    key: "DeviceLifecycleSummaryKey" = aristaproto.message_field(1)
    """
    DeviceLifecycleSummaryKey is the key of
     DeviceLifecycleSummary
    """

    software_eol: "SoftwareEol" = aristaproto.message_field(2)
    """
    software_eol is the software end of life of
     a device
    """

    hardware_lifecycle_summary: "HardwareLifecycleSummary" = aristaproto.message_field(
        3
    )
    """
    hardware_lifecycle_summary is the hardware lifecycle summary
     of a device
    """


@dataclass(eq=False, repr=False)
class MetaResponse(aristaproto.Message):
    time: datetime = aristaproto.message_field(1)
    """
    Time holds the timestamp of the last item included in the metadata calculation.
    """

    type: "__subscriptions__.Operation" = aristaproto.enum_field(2)
    """
    Operation indicates how the value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """

    count: Optional[int] = aristaproto.message_field(3, wraps=aristaproto.TYPE_UINT32)
    """
    Count is the number of items present under the conditions of the request.
    """


@dataclass(eq=False, repr=False)
class DeviceLifecycleSummaryRequest(aristaproto.Message):
    key: "DeviceLifecycleSummaryKey" = aristaproto.message_field(1)
    """
    Key uniquely identifies a DeviceLifecycleSummary instance to retrieve.
     This value must be populated.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the time for which you are interested in the data.
     If no time is given, the server will use the time at which it makes the request.
    """


@dataclass(eq=False, repr=False)
class DeviceLifecycleSummaryResponse(aristaproto.Message):
    value: "DeviceLifecycleSummary" = aristaproto.message_field(1)
    """
    Value is the value requested.
     This structure will be fully-populated as it exists in the datastore. If
     optional fields were not given at creation, these fields will be empty or
     set to default values.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time carries the (UTC) timestamp of the last-modification of the
     DeviceLifecycleSummary instance in this response.
    """


@dataclass(eq=False, repr=False)
class DeviceLifecycleSummaryStreamRequest(aristaproto.Message):
    partial_eq_filter: List["DeviceLifecycleSummary"] = aristaproto.message_field(1)
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

     For GetAll, the fields start and end can be used as follows:

       * end: Returns the state of each DeviceLifecycleSummary at end.
         * Each DeviceLifecycleSummary response is fully-specified (all fields set).
       * start: Returns the state of each DeviceLifecycleSummary at start, followed by updates until now.
         * Each DeviceLifecycleSummary response at start is fully-specified, but updates may be partial.
       * start and end: Returns the state of each DeviceLifecycleSummary at start, followed by updates
         until end.
         * Each DeviceLifecycleSummary response at start is fully-specified, but updates until end may
           be partial.

     This field is not allowed in the Subscribe RPC.
    """


@dataclass(eq=False, repr=False)
class DeviceLifecycleSummaryStreamResponse(aristaproto.Message):
    value: "DeviceLifecycleSummary" = aristaproto.message_field(1)
    """
    Value is a value deemed relevant to the initiating request.
     This structure will always have its key-field populated. Which other fields are
     populated, and why, depends on the value of Operation and what triggered this notification.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time holds the timestamp of this DeviceLifecycleSummary's last modification.
    """

    type: "__subscriptions__.Operation" = aristaproto.enum_field(3)
    """
    Operation indicates how the DeviceLifecycleSummary value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """


class DeviceLifecycleSummaryServiceStub(aristaproto.ServiceStub):
    async def get_one(
        self,
        device_lifecycle_summary_request: "DeviceLifecycleSummaryRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "DeviceLifecycleSummaryResponse":
        return await self._unary_unary(
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/GetOne",
            device_lifecycle_summary_request,
            DeviceLifecycleSummaryResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_all(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["DeviceLifecycleSummaryStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/GetAll",
            device_lifecycle_summary_stream_request,
            DeviceLifecycleSummaryStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def subscribe(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["DeviceLifecycleSummaryStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/Subscribe",
            device_lifecycle_summary_stream_request,
            DeviceLifecycleSummaryStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def get_meta(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MetaResponse":
        return await self._unary_unary(
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/GetMeta",
            device_lifecycle_summary_stream_request,
            MetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def subscribe_meta(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["MetaResponse"]:
        async for response in self._unary_stream(
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/SubscribeMeta",
            device_lifecycle_summary_stream_request,
            MetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class DeviceLifecycleSummaryServiceBase(ServiceBase):

    async def get_one(
        self, device_lifecycle_summary_request: "DeviceLifecycleSummaryRequest"
    ) -> "DeviceLifecycleSummaryResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_all(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
    ) -> AsyncIterator["DeviceLifecycleSummaryStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
    ) -> AsyncIterator["DeviceLifecycleSummaryStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_meta(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
    ) -> "MetaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe_meta(
        self,
        device_lifecycle_summary_stream_request: "DeviceLifecycleSummaryStreamRequest",
    ) -> AsyncIterator["MetaResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_one(
        self,
        stream: "grpclib.server.Stream[DeviceLifecycleSummaryRequest, DeviceLifecycleSummaryResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_one(request)
        await stream.send_message(response)

    async def __rpc_get_all(
        self,
        stream: "grpclib.server.Stream[DeviceLifecycleSummaryStreamRequest, DeviceLifecycleSummaryStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_all,
            stream,
            request,
        )

    async def __rpc_subscribe(
        self,
        stream: "grpclib.server.Stream[DeviceLifecycleSummaryStreamRequest, DeviceLifecycleSummaryStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe,
            stream,
            request,
        )

    async def __rpc_get_meta(
        self,
        stream: "grpclib.server.Stream[DeviceLifecycleSummaryStreamRequest, MetaResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_meta(request)
        await stream.send_message(response)

    async def __rpc_subscribe_meta(
        self,
        stream: "grpclib.server.Stream[DeviceLifecycleSummaryStreamRequest, MetaResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe_meta,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/GetOne": grpclib.const.Handler(
                self.__rpc_get_one,
                grpclib.const.Cardinality.UNARY_UNARY,
                DeviceLifecycleSummaryRequest,
                DeviceLifecycleSummaryResponse,
            ),
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/GetAll": grpclib.const.Handler(
                self.__rpc_get_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                DeviceLifecycleSummaryStreamRequest,
                DeviceLifecycleSummaryStreamResponse,
            ),
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/Subscribe": grpclib.const.Handler(
                self.__rpc_subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                DeviceLifecycleSummaryStreamRequest,
                DeviceLifecycleSummaryStreamResponse,
            ),
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/GetMeta": grpclib.const.Handler(
                self.__rpc_get_meta,
                grpclib.const.Cardinality.UNARY_UNARY,
                DeviceLifecycleSummaryStreamRequest,
                MetaResponse,
            ),
            "/arista.lifecycle.v1.DeviceLifecycleSummaryService/SubscribeMeta": grpclib.const.Handler(
                self.__rpc_subscribe_meta,
                grpclib.const.Cardinality.UNARY_STREAM,
                DeviceLifecycleSummaryStreamRequest,
                MetaResponse,
            ),
        }
