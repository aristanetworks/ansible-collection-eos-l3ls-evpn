# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: arista/event.v1/event.proto, arista/event.v1/services.gen.proto
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

try:
    import aristaproto
    import grpclib
    from aristaproto.grpc.grpclib_server import ServiceBase
except ImportError:
    HAS_ARISTAPROTO = False
    from .....mocked_classes import mocked_aristaproto as aristaproto
    from .....mocked_classes import mocked_grpclib as grpclib
    ServiceBase = object
else:
    HAS_ARISTAPROTO = True

from .... import fmp as ___fmp__
from ... import (
    subscriptions as __subscriptions__,
    time as __time__,
)


if TYPE_CHECKING:
    import grpclib.server
    from aristaproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class EventSeverity(aristaproto.Enum):
    """EventSeverity is the severity level of the event"""

    UNSPECIFIED = 0
    """
    EVENT_SEVERITY_UNSPECIFIED is the default value, if the severity is not specified.
    """

    INFO = 1
    """EVENT_SEVERITY_INFO is used for generally useful information."""

    WARNING = 2
    """EVENT_SEVERITY_WARNING is used for potentially harmful conditions."""

    ERROR = 3
    """
    EVENT_SEVERITY_ERROR is used for errors events that may allow for continued functioning.
    """

    CRITICAL = 4
    """
    EVENT_SEVERITY_CRITICAL is used to designate severe errors that impede functioning.
    """


class ComponentType(aristaproto.Enum):
    """
    ComponentType describes the type of entity on which the event occured
    """

    UNSPECIFIED = 0
    """
    COMPONENT_TYPE_UNSPECIFIED is the default value, if the type is not specified.
    """

    DEVICE = 1
    """COMPONENT_TYPE_DEVICE is used for device events."""

    INTERFACE = 2
    """COMPONENT_TYPE_INTERFACE is used for device interface events."""

    TURBINE = 3
    """
    COMPONENT_TYPE_TURBINE is used for events on the internal CVP turbine
     components. A turbine is an internal CV streaming analytics backend process.
    """

    DVS = 4
    """
    COMPONENT_TYPE_DVS is used for DVS events.
     A vSphere Distributed Switch provides centralized management and
     monitoring of the networking configuration of all workload servers that are
     associated with the switch.
    """

    DVS_INTERFACE = 5
    """COMPONENT_TYPE_DVS_INTERFACE is used for DVS interface events."""

    VM = 6
    """
    COMPONENT_TYPE_VM is used for VM events.
     A VM is a software computer that, like a physical computer, runs an
     operating system and applications.
    """

    VM_INTERFACE = 7
    """COMPONENT_TYPE_VM_INTERFACE is used for VM interface events."""

    WORKLOAD_SERVER = 8
    """
    COMPONENT_TYPE_WORKLOAD_SERVER is used for workload server events.
     A workload server is a server/data storage device on which the hypervisor is installed.
    """

    WORKLOAD_SERVER_INTERFACE = 9
    """
    COMPONENT_TYPE_WORKLOAD_SERVER_INTERFACE is used for workload server interface events.
    """

    APPLICATION = 10
    """COMPONENT_TYPE_APPLICATION is used for application-service events."""

    CVP_NODE = 11
    """COMPONENT_TYPE_CVP_NODE is used for CVP node events."""


@dataclass(eq=False, repr=False)
class EventComponent(aristaproto.Message):
    """EventComponent describes an entity on which the event occured"""

    type: "ComponentType" = aristaproto.enum_field(1)
    """type is the type of component"""

    components: Dict[str, str] = aristaproto.map_field(
        2, aristaproto.TYPE_STRING, aristaproto.TYPE_STRING
    )
    """components identifies the entity on which the event occured"""


@dataclass(eq=False, repr=False)
class EventComponents(aristaproto.Message):
    """EventComponents contains entities on which an event occured"""

    components: List["EventComponent"] = aristaproto.message_field(1)
    """components describes the components on which an event occured"""


@dataclass(eq=False, repr=False)
class EventAck(aristaproto.Message):
    """EventAck contains acknowledgement information of an event"""

    ack: Optional[bool] = aristaproto.message_field(1, wraps=aristaproto.TYPE_BOOL)
    """ack is the acknowledgement state of an event"""

    acker: Optional[str] = aristaproto.message_field(2, wraps=aristaproto.TYPE_STRING)
    """acker is the user that acknowledged the event"""

    ack_time: datetime = aristaproto.message_field(3)
    """ack_time is the time of acknowledgement"""


@dataclass(eq=False, repr=False)
class EventRead(aristaproto.Message):
    """EventRead contains read information of an event"""

    read: Optional[bool] = aristaproto.message_field(1, wraps=aristaproto.TYPE_BOOL)
    """read is the read state of an event"""

    reader: Optional[str] = aristaproto.message_field(2, wraps=aristaproto.TYPE_STRING)
    """reader is the user that read the event"""

    read_time: datetime = aristaproto.message_field(3)
    """read_time is the time of read"""


@dataclass(eq=False, repr=False)
class EventNoteConfig(aristaproto.Message):
    """
    EventNoteConfig configures a note

     NOTE: note is required when used as an argument
           to Set.
    """

    note: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """note is the text of the note"""


@dataclass(eq=False, repr=False)
class EventNote(aristaproto.Message):
    """EventNote is the state of a note"""

    note: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """note is the text of the note"""

    note_creator: Optional[str] = aristaproto.message_field(
        2, wraps=aristaproto.TYPE_STRING
    )
    """note_creator is the creator of the note"""


@dataclass(eq=False, repr=False)
class EventKey(aristaproto.Message):
    """
    EventKey uniquely identifies an event

     NOTE: All fields are required when used as an argument
           to GetOne, Set or Delete.
    """

    key: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """key is the event data identifier"""

    timestamp: datetime = aristaproto.message_field(2)
    """timestamp is the time the event occured"""


@dataclass(eq=False, repr=False)
class EventData(aristaproto.Message):
    """EventData is additional event data"""

    data: Dict[str, str] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_STRING
    )
    """data is event data specific to the type of this event"""


@dataclass(eq=False, repr=False)
class EventNotesConfig(aristaproto.Message):
    """
    EventNotesConfig configures the notes of an event

     NOTE: notes is required when used as an argument
           to Set.
    """

    notes: Dict[int, "EventNoteConfig"] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_MESSAGE
    )
    """notes is keyed by desired note time in Unix time, in milliseconds"""


@dataclass(eq=False, repr=False)
class EventAnnotationConfig(aristaproto.Message):
    """
    EventAnnotationConfig configures an event annotation

     NOTE: Either 1) key and ack or 2) key and notes or 3) key and read are
           required when used as an argument to Set.
    """

    key: "EventKey" = aristaproto.message_field(1)
    """key is the event instance identifier"""

    ack: Optional[bool] = aristaproto.message_field(2, wraps=aristaproto.TYPE_BOOL)
    """ack is the acknowledgement state of an event"""

    notes: "EventNotesConfig" = aristaproto.message_field(3)
    """notes is the notes on an event"""

    read: Optional[bool] = aristaproto.message_field(4, wraps=aristaproto.TYPE_BOOL)
    """
    read is the read state of an event. Setting this implies that an event has been read by a user
    """


@dataclass(eq=False, repr=False)
class EventNotes(aristaproto.Message):
    """EventNotes is the notes of an event state"""

    notes: Dict[int, "EventNote"] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_MESSAGE
    )
    """notes is keyed by the time desired"""


@dataclass(eq=False, repr=False)
class Event(aristaproto.Message):
    """Event is a telemetry event"""

    key: "EventKey" = aristaproto.message_field(1)
    """key is the event instance identifier"""

    severity: "EventSeverity" = aristaproto.enum_field(2)
    """severity is the severity of the event"""

    title: Optional[str] = aristaproto.message_field(3, wraps=aristaproto.TYPE_STRING)
    """title is the title of the event"""

    description: Optional[str] = aristaproto.message_field(
        4, wraps=aristaproto.TYPE_STRING
    )
    """description is the description of the event"""

    event_type: Optional[str] = aristaproto.message_field(
        5, wraps=aristaproto.TYPE_STRING
    )
    """event_type is the type of the event"""

    data: "EventData" = aristaproto.message_field(6)
    """data is the data of the event"""

    components: "EventComponents" = aristaproto.message_field(7)
    """components is the components on which the event occurred"""

    ack: "EventAck" = aristaproto.message_field(8)
    """ack is the acknowledgement status of the event"""

    notes: "EventNotes" = aristaproto.message_field(9)
    """notes is the notes of the event"""

    last_updated_time: datetime = aristaproto.message_field(10)
    """last_updated_time is the time of the most recent update to the event"""

    read: "EventRead" = aristaproto.message_field(11)
    """read is the read status of the event"""

    rule_id: Optional[str] = aristaproto.message_field(
        12, wraps=aristaproto.TYPE_STRING
    )
    """rule_id is the label of the rule associated with the event"""


@dataclass(eq=False, repr=False)
class EventRequest(aristaproto.Message):
    key: "EventKey" = aristaproto.message_field(1)
    """
    Key uniquely identifies a Event instance to retrieve.
     This value must be populated.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the time for which you are interested in the data.
     If no time is given, the server will use the time at which it makes the request.
    """


@dataclass(eq=False, repr=False)
class EventResponse(aristaproto.Message):
    value: "Event" = aristaproto.message_field(1)
    """
    Value is the value requested.
     This structure will be fully-populated as it exists in the datastore. If
     optional fields were not given at creation, these fields will be empty or
     set to default values.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time carries the (UTC) timestamp of the last-modification of the
     Event instance in this response.
    """


@dataclass(eq=False, repr=False)
class EventStreamRequest(aristaproto.Message):
    partial_eq_filter: List["Event"] = aristaproto.message_field(1)
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

       * end: Returns the state of each Event at end.
         * Each Event response is fully-specified (all fields set).
       * start: Returns the state of each Event at start, followed by updates until now.
         * Each Event response at start is fully-specified, but updates may be partial.
       * start and end: Returns the state of each Event at start, followed by updates
         until end.
         * Each Event response at start is fully-specified, but updates until end may
           be partial.

     This field is not allowed in the Subscribe RPC.
    """


@dataclass(eq=False, repr=False)
class EventStreamResponse(aristaproto.Message):
    value: "Event" = aristaproto.message_field(1)
    """
    Value is a value deemed relevant to the initiating request.
     This structure will always have its key-field populated. Which other fields are
     populated, and why, depends on the value of Operation and what triggered this notification.
    """

    time: datetime = aristaproto.message_field(2)
    """Time holds the timestamp of this Event's last modification."""

    type: "__subscriptions__.Operation" = aristaproto.enum_field(3)
    """
    Operation indicates how the Event value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigRequest(aristaproto.Message):
    key: "EventKey" = aristaproto.message_field(1)
    """
    Key uniquely identifies a EventAnnotationConfig instance to retrieve.
     This value must be populated.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the time for which you are interested in the data.
     If no time is given, the server will use the time at which it makes the request.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigResponse(aristaproto.Message):
    value: "EventAnnotationConfig" = aristaproto.message_field(1)
    """
    Value is the value requested.
     This structure will be fully-populated as it exists in the datastore. If
     optional fields were not given at creation, these fields will be empty or
     set to default values.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time carries the (UTC) timestamp of the last-modification of the
     EventAnnotationConfig instance in this response.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigStreamRequest(aristaproto.Message):
    partial_eq_filter: List["EventAnnotationConfig"] = aristaproto.message_field(1)
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

       * end: Returns the state of each EventAnnotationConfig at end.
         * Each EventAnnotationConfig response is fully-specified (all fields set).
       * start: Returns the state of each EventAnnotationConfig at start, followed by updates until now.
         * Each EventAnnotationConfig response at start is fully-specified, but updates may be partial.
       * start and end: Returns the state of each EventAnnotationConfig at start, followed by updates
         until end.
         * Each EventAnnotationConfig response at start is fully-specified, but updates until end may
           be partial.

     This field is not allowed in the Subscribe RPC.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigStreamResponse(aristaproto.Message):
    value: "EventAnnotationConfig" = aristaproto.message_field(1)
    """
    Value is a value deemed relevant to the initiating request.
     This structure will always have its key-field populated. Which other fields are
     populated, and why, depends on the value of Operation and what triggered this notification.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time holds the timestamp of this EventAnnotationConfig's last modification.
    """

    type: "__subscriptions__.Operation" = aristaproto.enum_field(3)
    """
    Operation indicates how the EventAnnotationConfig value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigSetRequest(aristaproto.Message):
    value: "EventAnnotationConfig" = aristaproto.message_field(1)
    """
    EventAnnotationConfig carries the value to set into the datastore.
     See the documentation on the EventAnnotationConfig struct for which fields are required.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigSetResponse(aristaproto.Message):
    value: "EventAnnotationConfig" = aristaproto.message_field(1)
    """
    Value carries all the values given in the EventAnnotationConfigSetRequest as well
     as any server-generated values.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the (UTC) timestamp at which the system recognizes the
     creation. The only guarantees made about this timestamp are:

        - it is after the time the request was received
        - a time-ranged query with StartTime==CreatedAt will include this instance.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigSetSomeRequest(aristaproto.Message):
    values: List["EventAnnotationConfig"] = aristaproto.message_field(1)
    """
    value contains a list of EventAnnotationConfig values to write.
     It is possible to provide more values than can fit within either:
         - the maxiumum send size of the client
         - the maximum receive size of the server
     If this error occurs you must reduce the number of values sent.
     See gRPC "maximum message size" documentation for more information.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigSetSomeResponse(aristaproto.Message):
    key: "EventKey" = aristaproto.message_field(1)
    error: str = aristaproto.string_field(2)


@dataclass(eq=False, repr=False)
class EventAnnotationConfigDeleteRequest(aristaproto.Message):
    key: "EventKey" = aristaproto.message_field(1)
    """
    Key indicates which EventAnnotationConfig instance to remove.
     This field must always be set.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigDeleteResponse(aristaproto.Message):
    key: "EventKey" = aristaproto.message_field(1)
    """
    Key echoes back the key of the deleted EventAnnotationConfig instance.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the (UTC) timestamp at which the system recognizes the
     deletion. The only guarantees made about this timestamp are:

        - it is after the time the request was received
        - a time-ranged query with StartTime==DeletedAt will not include this instance.
    """


@dataclass(eq=False, repr=False)
class EventAnnotationConfigDeleteAllRequest(aristaproto.Message):
    pass


@dataclass(eq=False, repr=False)
class EventAnnotationConfigDeleteAllResponse(aristaproto.Message):
    type: "___fmp__.DeleteError" = aristaproto.enum_field(1)
    """This describes the class of delete error."""

    error: Optional[str] = aristaproto.message_field(2, wraps=aristaproto.TYPE_STRING)
    """This indicates the error message from the delete failure."""

    key: "EventKey" = aristaproto.message_field(3)
    """
    This is the key of the EventAnnotationConfig instance that failed to be deleted.
    """

    time: datetime = aristaproto.message_field(4)
    """Time indicates the (UTC) timestamp when the key was being deleted."""


class EventServiceStub(aristaproto.ServiceStub):
    async def get_one(
        self,
        event_request: "EventRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "EventResponse":
        return await self._unary_unary(
            "/arista.event.v1.EventService/GetOne",
            event_request,
            EventResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_all(
        self,
        event_stream_request: "EventStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["EventStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.event.v1.EventService/GetAll",
            event_stream_request,
            EventStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def subscribe(
        self,
        event_stream_request: "EventStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["EventStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.event.v1.EventService/Subscribe",
            event_stream_request,
            EventStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class EventAnnotationConfigServiceStub(aristaproto.ServiceStub):
    async def get_one(
        self,
        event_annotation_config_request: "EventAnnotationConfigRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "EventAnnotationConfigResponse":
        return await self._unary_unary(
            "/arista.event.v1.EventAnnotationConfigService/GetOne",
            event_annotation_config_request,
            EventAnnotationConfigResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_all(
        self,
        event_annotation_config_stream_request: "EventAnnotationConfigStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["EventAnnotationConfigStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.event.v1.EventAnnotationConfigService/GetAll",
            event_annotation_config_stream_request,
            EventAnnotationConfigStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def subscribe(
        self,
        event_annotation_config_stream_request: "EventAnnotationConfigStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["EventAnnotationConfigStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.event.v1.EventAnnotationConfigService/Subscribe",
            event_annotation_config_stream_request,
            EventAnnotationConfigStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def set(
        self,
        event_annotation_config_set_request: "EventAnnotationConfigSetRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "EventAnnotationConfigSetResponse":
        return await self._unary_unary(
            "/arista.event.v1.EventAnnotationConfigService/Set",
            event_annotation_config_set_request,
            EventAnnotationConfigSetResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def set_some(
        self,
        event_annotation_config_set_some_request: "EventAnnotationConfigSetSomeRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["EventAnnotationConfigSetSomeResponse"]:
        async for response in self._unary_stream(
            "/arista.event.v1.EventAnnotationConfigService/SetSome",
            event_annotation_config_set_some_request,
            EventAnnotationConfigSetSomeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def delete(
        self,
        event_annotation_config_delete_request: "EventAnnotationConfigDeleteRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "EventAnnotationConfigDeleteResponse":
        return await self._unary_unary(
            "/arista.event.v1.EventAnnotationConfigService/Delete",
            event_annotation_config_delete_request,
            EventAnnotationConfigDeleteResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def delete_all(
        self,
        event_annotation_config_delete_all_request: "EventAnnotationConfigDeleteAllRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["EventAnnotationConfigDeleteAllResponse"]:
        async for response in self._unary_stream(
            "/arista.event.v1.EventAnnotationConfigService/DeleteAll",
            event_annotation_config_delete_all_request,
            EventAnnotationConfigDeleteAllResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class EventServiceBase(ServiceBase):
    async def get_one(self, event_request: "EventRequest") -> "EventResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_all(
        self, event_stream_request: "EventStreamRequest"
    ) -> AsyncIterator["EventStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe(
        self, event_stream_request: "EventStreamRequest"
    ) -> AsyncIterator["EventStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_one(
        self, stream: "grpclib.server.Stream[EventRequest, EventResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_one(request)
        await stream.send_message(response)

    async def __rpc_get_all(
        self, stream: "grpclib.server.Stream[EventStreamRequest, EventStreamResponse]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_all,
            stream,
            request,
        )

    async def __rpc_subscribe(
        self, stream: "grpclib.server.Stream[EventStreamRequest, EventStreamResponse]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/arista.event.v1.EventService/GetOne": grpclib.const.Handler(
                self.__rpc_get_one,
                grpclib.const.Cardinality.UNARY_UNARY,
                EventRequest,
                EventResponse,
            ),
            "/arista.event.v1.EventService/GetAll": grpclib.const.Handler(
                self.__rpc_get_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                EventStreamRequest,
                EventStreamResponse,
            ),
            "/arista.event.v1.EventService/Subscribe": grpclib.const.Handler(
                self.__rpc_subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                EventStreamRequest,
                EventStreamResponse,
            ),
        }


class EventAnnotationConfigServiceBase(ServiceBase):
    async def get_one(
        self, event_annotation_config_request: "EventAnnotationConfigRequest"
    ) -> "EventAnnotationConfigResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_all(
        self,
        event_annotation_config_stream_request: "EventAnnotationConfigStreamRequest",
    ) -> AsyncIterator["EventAnnotationConfigStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe(
        self,
        event_annotation_config_stream_request: "EventAnnotationConfigStreamRequest",
    ) -> AsyncIterator["EventAnnotationConfigStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set(
        self, event_annotation_config_set_request: "EventAnnotationConfigSetRequest"
    ) -> "EventAnnotationConfigSetResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_some(
        self,
        event_annotation_config_set_some_request: "EventAnnotationConfigSetSomeRequest",
    ) -> AsyncIterator["EventAnnotationConfigSetSomeResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delete(
        self,
        event_annotation_config_delete_request: "EventAnnotationConfigDeleteRequest",
    ) -> "EventAnnotationConfigDeleteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delete_all(
        self,
        event_annotation_config_delete_all_request: "EventAnnotationConfigDeleteAllRequest",
    ) -> AsyncIterator["EventAnnotationConfigDeleteAllResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_one(
        self,
        stream: "grpclib.server.Stream[EventAnnotationConfigRequest, EventAnnotationConfigResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_one(request)
        await stream.send_message(response)

    async def __rpc_get_all(
        self,
        stream: "grpclib.server.Stream[EventAnnotationConfigStreamRequest, EventAnnotationConfigStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_all,
            stream,
            request,
        )

    async def __rpc_subscribe(
        self,
        stream: "grpclib.server.Stream[EventAnnotationConfigStreamRequest, EventAnnotationConfigStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe,
            stream,
            request,
        )

    async def __rpc_set(
        self,
        stream: "grpclib.server.Stream[EventAnnotationConfigSetRequest, EventAnnotationConfigSetResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.set(request)
        await stream.send_message(response)

    async def __rpc_set_some(
        self,
        stream: "grpclib.server.Stream[EventAnnotationConfigSetSomeRequest, EventAnnotationConfigSetSomeResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.set_some,
            stream,
            request,
        )

    async def __rpc_delete(
        self,
        stream: "grpclib.server.Stream[EventAnnotationConfigDeleteRequest, EventAnnotationConfigDeleteResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.delete(request)
        await stream.send_message(response)

    async def __rpc_delete_all(
        self,
        stream: "grpclib.server.Stream[EventAnnotationConfigDeleteAllRequest, EventAnnotationConfigDeleteAllResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.delete_all,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/arista.event.v1.EventAnnotationConfigService/GetOne": grpclib.const.Handler(
                self.__rpc_get_one,
                grpclib.const.Cardinality.UNARY_UNARY,
                EventAnnotationConfigRequest,
                EventAnnotationConfigResponse,
            ),
            "/arista.event.v1.EventAnnotationConfigService/GetAll": grpclib.const.Handler(
                self.__rpc_get_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                EventAnnotationConfigStreamRequest,
                EventAnnotationConfigStreamResponse,
            ),
            "/arista.event.v1.EventAnnotationConfigService/Subscribe": grpclib.const.Handler(
                self.__rpc_subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                EventAnnotationConfigStreamRequest,
                EventAnnotationConfigStreamResponse,
            ),
            "/arista.event.v1.EventAnnotationConfigService/Set": grpclib.const.Handler(
                self.__rpc_set,
                grpclib.const.Cardinality.UNARY_UNARY,
                EventAnnotationConfigSetRequest,
                EventAnnotationConfigSetResponse,
            ),
            "/arista.event.v1.EventAnnotationConfigService/SetSome": grpclib.const.Handler(
                self.__rpc_set_some,
                grpclib.const.Cardinality.UNARY_STREAM,
                EventAnnotationConfigSetSomeRequest,
                EventAnnotationConfigSetSomeResponse,
            ),
            "/arista.event.v1.EventAnnotationConfigService/Delete": grpclib.const.Handler(
                self.__rpc_delete,
                grpclib.const.Cardinality.UNARY_UNARY,
                EventAnnotationConfigDeleteRequest,
                EventAnnotationConfigDeleteResponse,
            ),
            "/arista.event.v1.EventAnnotationConfigService/DeleteAll": grpclib.const.Handler(
                self.__rpc_delete_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                EventAnnotationConfigDeleteAllRequest,
                EventAnnotationConfigDeleteAllResponse,
            ),
        }
