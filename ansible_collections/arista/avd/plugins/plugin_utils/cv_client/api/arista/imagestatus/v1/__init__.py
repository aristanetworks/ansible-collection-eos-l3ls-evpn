# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: arista/imagestatus.v1/imagestatus.proto, arista/imagestatus.v1/services.gen.proto
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

from ... import (
    subscriptions as __subscriptions__,
    time as __time__,
)


if TYPE_CHECKING:
    import grpclib.server
    from aristaproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class ExtensionInstallStatus(aristaproto.Enum):
    """
    ExtensionInstallStatus indicates whether an extension is installed, not installed
     or force installed.
    """

    UNSPECIFIED = 0
    """
    EXTENSION_INSTALL_STATUS_UNSPECIFIED indicates extensions install status is unspecified.
    """

    NOT_INSTALLED = 1
    """
    EXTENSION_INSTALL_STATUS_NOT_INSTALLED indicates extension is not installed on the device.
    """

    INSTALLED = 2
    """
    EXTENSION_INSTALL_STATUS_INSTALLED indicates extension is installed on the device.
    """

    FORCE_INSTALLED = 3
    """
    EXTENSION_INSTALL_STATUS_FORCE_INSTALLED indicates extension is force installed on
     device.
    """


class SoftwareComplianceCode(aristaproto.Enum):
    """SoftwareComplianceCode indicates possible compliance status."""

    UNSPECIFIED = 0
    """
    SOFTWARE_COMPLIANCE_CODE_UNSPECIFIED indicates compliance code is unspecified.
    """

    IN_SYNC = 1
    """
    SOFTWARE_COMPLIANCE_CODE_IN_SYNC indicates designed and running images/extensions
     are identical.
    """

    OUT_OF_SYNC = 2
    """
    SOFTWARE_COMPLIANCE_CODE_OUT_OF_SYNC indicates designed and running images/extensions
     are not identical.
    """


class DiffOp(aristaproto.Enum):
    """
    DiffOp represents the operation performed to get from one side of the diff
     to the other.
    """

    UNSPECIFIED = 0
    """DIFF_OP_UNSPECIFIED indicates op code is unspecified."""

    NOP = 1
    """DIFF_OP_NOP indicates no change."""

    ADD = 2
    """DIFF_OP_ADD is an addition of a software."""

    DELETE = 3
    """DIFF_OP_DELETE is deletion of a software."""

    CHANGE = 4
    """DIFF_OP_CHANGE is an update to the software."""


class ErrorCode(aristaproto.Enum):
    """ErrorCode indicates errors produced during image validations."""

    UNSPECIFIED = 0
    """ERROR_CODE_UNSPECIFIED indicates error code is unspecified."""

    SUPPORT_NOT_INTRODUCED = 1
    """
    ERROR_CODE_SUPPORT_NOT_INTRODUCED represents case where the given EOS version does
     not support the SKU.
     Deprecated - use ERROR_CODE_EOS_SUPPORT_NOT_INTRODUCED
    """

    SUPPORT_REMOVED = 2
    """
    ERROR_CODE_SUPPORT_REMOVED represents case where the given EOS version no longer
     supports the SKU.
     Deprecated - use ERROR_CODE_EOS_SUPPORT_REMOVED
    """

    DEVICE_UNREACHABLE = 3
    """
    ERROR_CODE_DEVICE_UNREACHABLE represents the case where the device
     is unreachable during a compliance computation.
    """

    VALIDATION_FAILED = 4
    """
    ERROR_CODE_VALIDATION_FAILED represents case where the validations checks
     failed.
    """

    GET_PROPOSED_IMAGE_INFO_FAILED = 5
    """
    ERROR_CODE_GET_PROPOSED_IMAGE_INFO_FAILED represents case where we are
     unable to get proposed image information for a device.
    """

    GET_RUNNING_IMAGE_INFO_FROM_ACTIVE_SUPERVISOR_FAILED = 6
    """
    ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_ACTIVE_SUPERVISOR_FAILED represents case where we
     fail to get running image information from an active supervisor.
    """

    GET_RUNNING_IMAGE_INFO_FROM_PEER_SUPERVISOR_FAILED = 7
    """
    ERROR_CODE_GET_RUNNING_IMAGE_INFO_FROM_PEER_SUPERVISOR_FAILED represents case when we
     fail to get information from peer supervisor.
    """

    EOS_TA_ARCHITECTURE_INCOMPATIBLE = 8
    """
    ERROR_CODE_EOS_TA_ARCHITECTURE_INCOMPATIBLE represents the case where EOS architecture and
     TerminAttr architecture are incompatible.
    """

    TA_CV_INCOMPATIBLE = 9
    """
    ERROR_CODE_TA_CV_INCOMPATIBLE represents the case where TerminAttr is incompatible with
     CloudVision; i.e., the TerminAttr version is below CloudVision's minimum supported version.
    """

    EOS_CV_INCOMPATIBLE = 10
    """
    ERROR_CODE_EOS_CV_INCOMPATIBLE represents the case where the EOS version is incompatible with
     CloudVision; i.e., the EOS version is outside of CloudVision's supported range of versions.
    """

    EOS_SUPPORT_NOT_INTRODUCED = 11
    """
    ERROR_CODE_EOS_SUPPORT_NOT_INTRODUCED represents the case where the given EOS version does
     not support the SKU.
    """

    EOS_SUPPORT_REMOVED = 12
    """
    ERROR_CODE_EOS_SUPPORT_REMOVED represents the case where the given EOS version no longer
     supports the SKU.
    """

    PHYSICAL_DEVICE_EOS_INCOMPATIBLE = 13
    """
    ERROR_CODE_PHYSICAL_DEVICE_EOS_INCOMPATIBLE represents the case where the physical device
     does not support the given EOS type.
    """


class WarningCode(aristaproto.Enum):
    """WarningCode indicates warnings produced during image validations."""

    UNSPECIFIED = 0
    """WARNING_CODE_UNSPECIFIED indicates warning code is unspecified."""

    NOT_APPLICABLE = 1
    """
    WARNING_CODE_NOT_APPLICABLE represents cases where EOS <-> SKU/TA compatibility
     is not applicable for non physical switches like vEos.
    """

    SKUINFO_UNAVAILABLE = 2
    """
    WARNING_CODE_SKUINFO_UNAVAILABLE represents case where
     information about certain skus is missing.
    """

    DEVICE_SKU_UNAVAILABLE = 3
    """
    WARNING_CODE_DEVICE_SKU_UNAVAILABLE represents unavailability of skus for an EOS Device.
    """

    SWI_UNKNOWN = 4
    """
    WARNING_CODE_SWI_UNKNOWN represents cases where EOS version is not found in release database.
    """

    TA_EOS_INCOMPATIBLE = 5
    """
    WARNING_CODE_TA_EOS_INCOMPATIBLE represents cases where TA and EOS are not compatible.
     TA is lower than embedded TA in swi or given TA is unsupported by the EOS.
    """

    TA_CV_INCOMPATIBLE = 6
    """
    WARNING_CODE_TA_CV_INCOMPATIBLE represents cases where TA is incompatible with CV.
     TA is lower than minimum supported TA on CV.
     Deprecated - use ERROR_CODE_TA_CV_INCOMPATIBLE.
    """

    EOS_CV_INCOMPATIBLE = 7
    """
    WARNING_CODE_EOS_CV_INCOMPATIBLE represents cases where EOS is no longer or not yet
     supported by CV. Given EOS is outside range of CV's minimum and maximum EOS.
     Deprecated - use ERROR_CODE_EOS_CV_INCOMPATIBLE.
    """

    EOS_ARCH_UNKNOWN = 8
    """
    WARNING_CODE_EOS_ARCH_UNKNOWN represents cases where the specified architecture is
     not valid for EOS.
    """

    TA_EMBEDDEDEXT_INCOMPATIBLE = 9
    """
    WARNING_CODE_TA_EMBEDDEDEXT_INCOMPATIBLE represents cases where TA extension is lower
     in version than embedded TA in SWI.
    """

    ARCH_INCOMPATIBLE = 10
    """
    WARNING_CODE_ARCH_INCOMPATIBLE represents cases where EOS arch and TA arch are
     different. Deprecated.
    """

    EOS_END_OF_LIFE_DATE_PASSED = 11
    """
    WARNING_CODE_EOS_END_OF_LIFE_DATE_PASSED represents cases where the given EOS has passed
     its end of life date.
    """

    SUPPORT_NOT_INTRODUCED = 12
    """
    WARNING_CODE_SUPPORT_NOT_INTRODUCED represents cases where the given EOS version does
     not support the SKUs.
    """

    SUPPORT_REMOVED = 13
    """
    WARNING_CODE_SUPPORT_REMOVED represents cases where the given EOS version no longer
     supports the SKUs.
    """


@dataclass(eq=False, repr=False)
class SoftwareImage(aristaproto.Message):
    """
    SoftwareImage provides information of the running/designed EOS image.
    """

    name: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """name is the name of the EOS image."""

    version: Optional[str] = aristaproto.message_field(2, wraps=aristaproto.TYPE_STRING)
    """version is the version of the EOS image."""

    metadata: "ImageMetadata" = aristaproto.message_field(3)
    """metadata  is the metadata of EOS image."""


@dataclass(eq=False, repr=False)
class ImageMetadata(aristaproto.Message):
    """ImageMetadata provides information regarding the software image."""

    version: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """version is the version of the EOS image."""

    release: Optional[str] = aristaproto.message_field(2, wraps=aristaproto.TYPE_STRING)
    """release is the release name of the EOS image."""

    flavor: Optional[str] = aristaproto.message_field(3, wraps=aristaproto.TYPE_STRING)
    """
    flavor is the flavor information of the EOS image.
     default flavor is DEFAULT. Other flavors can be DPE, 2GB, etc.
    """

    variant: Optional[str] = aristaproto.message_field(4, wraps=aristaproto.TYPE_STRING)
    """
    variant is the variant information of the EOS image.
     possible values: INT or US.
    """

    arch: Optional[str] = aristaproto.message_field(5, wraps=aristaproto.TYPE_STRING)
    """arch is the architecture of the EOS image."""


@dataclass(eq=False, repr=False)
class Extension(aristaproto.Message):
    """Extension provides information of the running/designed extensions."""

    name: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """name is the name of the extension."""

    version: Optional[str] = aristaproto.message_field(2, wraps=aristaproto.TYPE_STRING)
    """version is the version of the extension."""

    reboot_required: Optional[bool] = aristaproto.message_field(
        3, wraps=aristaproto.TYPE_BOOL
    )
    """
    reboot_required indicates whether applying/deleting this extension
     would result in a reboot.
    """

    present: Optional[bool] = aristaproto.message_field(4, wraps=aristaproto.TYPE_BOOL)
    """
    present indicates whether the extension is present in the device
     or not.
    """

    installed: "ExtensionInstallStatus" = aristaproto.enum_field(5)
    """
    installed indicates whether the extension is installed, not
     installed or force installed.
    """

    status_detail: Optional[str] = aristaproto.message_field(
        6, wraps=aristaproto.TYPE_STRING
    )
    """
    status_detail gives the details behind installation of the extension.
    """

    is_embedded: Optional[bool] = aristaproto.message_field(
        7, wraps=aristaproto.TYPE_BOOL
    )
    """
    is_embedded indicates whether the extension is embedded in the EOS swi
     or not.
    """


@dataclass(eq=False, repr=False)
class Extensions(aristaproto.Message):
    """Extensions provides an ordered list of running/designed extensions."""

    values: List["Extension"] = aristaproto.message_field(1)
    """values represents extension information."""


@dataclass(eq=False, repr=False)
class ComplianceStatus(aristaproto.Message):
    """
    ComplianceStatus indicates compliance status for software image, terminattr
     and extensions.
    """

    software_image_compliance_code: "SoftwareComplianceCode" = aristaproto.enum_field(1)
    """software_image_compliance_code is the compliance code for images."""

    terminattr_compliance_code: "SoftwareComplianceCode" = aristaproto.enum_field(2)
    """terminattr_compliance_code is the compliance code for TerminAttr."""

    extensions_compliance_code: "SoftwareComplianceCode" = aristaproto.enum_field(3)
    """extensions_compliance_code is the compliance code for extensions."""


@dataclass(eq=False, repr=False)
class ComplianceStatusBySup(aristaproto.Message):
    """
    ComplianceStatusBySup is a map that indicates the compliance code for each
     supervisor.
    """

    values: Dict[str, "ComplianceStatus"] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_MESSAGE
    )
    """values is the mapping of supervisor type to compliance code."""


@dataclass(eq=False, repr=False)
class RebootRequired(aristaproto.Message):
    """
    RebootRequired indicates the reboot information per software image,
     terminattr and extension for the switch as a whole.
    """

    software_image_reboot_required: Optional[bool] = aristaproto.message_field(
        1, wraps=aristaproto.TYPE_BOOL
    )
    """
    software_image_reboot_required indicates whether reboot is required
     for the software image being applied.
    """

    terminattr_reboot_required: Optional[bool] = aristaproto.message_field(
        2, wraps=aristaproto.TYPE_BOOL
    )
    """
    terminattr_reboot_required indicates whether reboot is required
     for the terminattr being applied/deleted.
    """

    extension_reboot_required: Optional[bool] = aristaproto.message_field(
        3, wraps=aristaproto.TYPE_BOOL
    )
    """
    extension_reboot_required indicates whether reboot is required
     for the extensions being applied/deleted.
    """


@dataclass(eq=False, repr=False)
class SoftwareImageDiff(aristaproto.Message):
    """SoftwareImageDiff is the diff for the running/designed images."""

    code: "DiffOp" = aristaproto.enum_field(1)
    """
    code indicates the operation performed to get from one side of the diff
     to the other.
    """

    a: "SoftwareImage" = aristaproto.message_field(2)
    """a is the software image on the a side (left hand side)."""

    b: "SoftwareImage" = aristaproto.message_field(3)
    """b is the software image on the b side (right hand side)."""


@dataclass(eq=False, repr=False)
class SoftwareImageDiffsBySup(aristaproto.Message):
    """
    SoftwareImageDiffsBySup is software image diff information for each
     supervisor.
    """

    values: Dict[str, "SoftwareImageDiff"] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_MESSAGE
    )
    """values is the mapping of supervisor type to image diff."""


@dataclass(eq=False, repr=False)
class ExtensionDiff(aristaproto.Message):
    """ExtensionDiff is the diff for the running/designed extensions."""

    code: "DiffOp" = aristaproto.enum_field(1)
    """
    code indicates the operation performed to get from one side of the diff
     to the other.
    """

    a: "Extension" = aristaproto.message_field(2)
    """a is the extension on the a side (left hand side)."""

    b: "Extension" = aristaproto.message_field(3)
    """b is the extension on the b side (right hand side)."""


@dataclass(eq=False, repr=False)
class TerminAttrDiffsBySup(aristaproto.Message):
    """
    TerminAttrDiffsBySup is the terminattr diff information for each supervisor.
    """

    values: Dict[str, "ExtensionDiff"] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_MESSAGE
    )
    """values is the mapping of supervisor type to terminattr diff."""


@dataclass(eq=False, repr=False)
class ExtensionDiffs(aristaproto.Message):
    """
    ExtensionDiffs is a list of extension diff information in the order they
     will be applied.
    """

    values: List["ExtensionDiff"] = aristaproto.message_field(1)
    """values is an ordered list of extension diffs applied to the device."""


@dataclass(eq=False, repr=False)
class ExtensionDiffsBySup(aristaproto.Message):
    """
    ExtensionDiffsBySup is the extension diff information for each supervisor.
    """

    values: Dict[str, "ExtensionDiffs"] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_MESSAGE
    )
    """values is the mapping of supervisor type to extension diff."""


@dataclass(eq=False, repr=False)
class ImageSummary(aristaproto.Message):
    """ImageSummary represents device image summary."""

    sku: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """sku indicates the top-level sku or model number."""

    running_image_update_time: datetime = aristaproto.message_field(2)
    """
    running_image_update_time is the most recent timestamp at which one of
     running image side properties is updated.
    """

    designed_image_update_time: datetime = aristaproto.message_field(3)
    """
    designed_image_update_time is the most recent timestamp at which one of
     designed image side properties is updated.
    """

    dual_sup: Optional[bool] = aristaproto.message_field(4, wraps=aristaproto.TYPE_BOOL)
    """dual_sup indicates if a device is a dual supervisor."""

    active_slot: Optional[int] = aristaproto.message_field(
        5, wraps=aristaproto.TYPE_INT32
    )
    """
    active_slot indicates the physical slot number for the the active
     supervisor.
    """

    standby_slot: Optional[int] = aristaproto.message_field(
        6, wraps=aristaproto.TYPE_INT32
    )
    """
    standby_slot indicates the physical slot number for the standby
     supervisor.
    """

    software_image_diff: "SoftwareImageDiffsBySup" = aristaproto.message_field(7)
    """software_image_diff indicates the image diff for each supervisor."""

    terminattr_diff: "TerminAttrDiffsBySup" = aristaproto.message_field(8)
    """terminattr_diff indicates the terminattr diff for each supervisor."""

    extensions_diff: "ExtensionDiffsBySup" = aristaproto.message_field(9)
    """extensions_diff indicates the extension diff for each supervisor."""

    compliance_status: "SoftwareComplianceCode" = aristaproto.enum_field(10)
    """
    compliance_status is the aggregated compliance status (including both
     active/standby and image/TA/extension compliance).
    """

    compliance: "ComplianceStatusBySup" = aristaproto.message_field(11)
    """compliance provides compliance information for each supervisor."""

    reboot_required: "RebootRequired" = aristaproto.message_field(12)
    """
    reboot_required indicates whether a reboot is required if the designed
     image is pushed to the device.
    """

    digest: Optional[str] = aristaproto.message_field(13, wraps=aristaproto.TYPE_STRING)
    """
    digest is the digest of the image summary. It can use SHA-256 hash
     algorithm for example. It is computed by stringifying the
    software_image_diff, terminattr_diff and extensions_diff and computing the
     hash.
    """


@dataclass(eq=False, repr=False)
class SummaryKey(aristaproto.Message):
    """SummaryKey uniquely identifies a device summary request."""

    device_id: Optional[str] = aristaproto.message_field(
        1, wraps=aristaproto.TYPE_STRING
    )
    """device_id is the serial number of the device"""


@dataclass(eq=False, repr=False)
class Summary(aristaproto.Message):
    """Summary represents the device image summary."""

    key: "SummaryKey" = aristaproto.message_field(1)
    """key represents the image summary key."""

    summary: "ImageSummary" = aristaproto.message_field(2)
    """summary is the image diff summary."""

    errors: "ImageErrors" = aristaproto.message_field(3)
    """
    errors are the image errors encountered while validating the image. These are
     displayed on the change control review page (for changes made outside the workspace).
    """

    warnings: "ImageWarnings" = aristaproto.message_field(4)
    """
    warnings are the image warnings encountered while validating the image. These are
     displayed on the change control review page (for changes made outside the workspace).
    """


@dataclass(eq=False, repr=False)
class ImageError(aristaproto.Message):
    """ImageError wraps `ErrorCode` enum with a reason string."""

    sku: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """sku represents the name of the sku."""

    error_code: "ErrorCode" = aristaproto.enum_field(2)
    """error_code is the error code."""

    error_msg: Optional[str] = aristaproto.message_field(
        3, wraps=aristaproto.TYPE_STRING
    )
    """error_msg provides a description of the error."""


@dataclass(eq=False, repr=False)
class ImageErrors(aristaproto.Message):
    """
    ImageErrors is the list of errors reported by CVP when handling image
     validations.
    """

    values: List["ImageError"] = aristaproto.message_field(1)
    """values is a list of image errors."""


@dataclass(eq=False, repr=False)
class ImageWarning(aristaproto.Message):
    """ImageWarning wraps `WarningCode` enum with a reason string."""

    sku: Optional[str] = aristaproto.message_field(1, wraps=aristaproto.TYPE_STRING)
    """sku represents the name of the sku."""

    warning_code: "WarningCode" = aristaproto.enum_field(2)
    """warning_code is the warning code."""

    warning_msg: Optional[str] = aristaproto.message_field(
        3, wraps=aristaproto.TYPE_STRING
    )
    """warning_msg provides a description of the warning."""


@dataclass(eq=False, repr=False)
class ImageWarnings(aristaproto.Message):
    """
    ImageWarnings is the list of warnings reported by CVP when handling image
     validations.
    """

    values: List["ImageWarning"] = aristaproto.message_field(1)
    """values is a list of image warnings."""


@dataclass(eq=False, repr=False)
class SummaryRequest(aristaproto.Message):
    key: "SummaryKey" = aristaproto.message_field(1)
    """
    Key uniquely identifies a Summary instance to retrieve.
     This value must be populated.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time indicates the time for which you are interested in the data.
     If no time is given, the server will use the time at which it makes the request.
    """


@dataclass(eq=False, repr=False)
class SummaryResponse(aristaproto.Message):
    value: "Summary" = aristaproto.message_field(1)
    """
    Value is the value requested.
     This structure will be fully-populated as it exists in the datastore. If
     optional fields were not given at creation, these fields will be empty or
     set to default values.
    """

    time: datetime = aristaproto.message_field(2)
    """
    Time carries the (UTC) timestamp of the last-modification of the
     Summary instance in this response.
    """


@dataclass(eq=False, repr=False)
class SummaryStreamRequest(aristaproto.Message):
    partial_eq_filter: List["Summary"] = aristaproto.message_field(1)
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

       * end: Returns the state of each Summary at end.
         * Each Summary response is fully-specified (all fields set).
       * start: Returns the state of each Summary at start, followed by updates until now.
         * Each Summary response at start is fully-specified, but updates may be partial.
       * start and end: Returns the state of each Summary at start, followed by updates
         until end.
         * Each Summary response at start is fully-specified, but updates until end may
           be partial.

     This field is not allowed in the Subscribe RPC.
    """


@dataclass(eq=False, repr=False)
class SummaryStreamResponse(aristaproto.Message):
    value: "Summary" = aristaproto.message_field(1)
    """
    Value is a value deemed relevant to the initiating request.
     This structure will always have its key-field populated. Which other fields are
     populated, and why, depends on the value of Operation and what triggered this notification.
    """

    time: datetime = aristaproto.message_field(2)
    """Time holds the timestamp of this Summary's last modification."""

    type: "__subscriptions__.Operation" = aristaproto.enum_field(3)
    """
    Operation indicates how the Summary value in this response should be considered.
     Under non-subscribe requests, this value should always be INITIAL. In a subscription,
     once all initial data is streamed and the client begins to receive modification updates,
     you should not see INITIAL again.
    """


class SummaryServiceStub(aristaproto.ServiceStub):
    async def get_one(
        self,
        summary_request: "SummaryRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "SummaryResponse":
        return await self._unary_unary(
            "/arista.imagestatus.v1.SummaryService/GetOne",
            summary_request,
            SummaryResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_all(
        self,
        summary_stream_request: "SummaryStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["SummaryStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.imagestatus.v1.SummaryService/GetAll",
            summary_stream_request,
            SummaryStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def subscribe(
        self,
        summary_stream_request: "SummaryStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["SummaryStreamResponse"]:
        async for response in self._unary_stream(
            "/arista.imagestatus.v1.SummaryService/Subscribe",
            summary_stream_request,
            SummaryStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class SummaryServiceBase(ServiceBase):
    async def get_one(self, summary_request: "SummaryRequest") -> "SummaryResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_all(
        self, summary_stream_request: "SummaryStreamRequest"
    ) -> AsyncIterator["SummaryStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def subscribe(
        self, summary_stream_request: "SummaryStreamRequest"
    ) -> AsyncIterator["SummaryStreamResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_one(
        self, stream: "grpclib.server.Stream[SummaryRequest, SummaryResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_one(request)
        await stream.send_message(response)

    async def __rpc_get_all(
        self,
        stream: "grpclib.server.Stream[SummaryStreamRequest, SummaryStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.get_all,
            stream,
            request,
        )

    async def __rpc_subscribe(
        self,
        stream: "grpclib.server.Stream[SummaryStreamRequest, SummaryStreamResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.subscribe,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/arista.imagestatus.v1.SummaryService/GetOne": grpclib.const.Handler(
                self.__rpc_get_one,
                grpclib.const.Cardinality.UNARY_UNARY,
                SummaryRequest,
                SummaryResponse,
            ),
            "/arista.imagestatus.v1.SummaryService/GetAll": grpclib.const.Handler(
                self.__rpc_get_all,
                grpclib.const.Cardinality.UNARY_STREAM,
                SummaryStreamRequest,
                SummaryStreamResponse,
            ),
            "/arista.imagestatus.v1.SummaryService/Subscribe": grpclib.const.Handler(
                self.__rpc_subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                SummaryStreamRequest,
                SummaryStreamResponse,
            ),
        }
