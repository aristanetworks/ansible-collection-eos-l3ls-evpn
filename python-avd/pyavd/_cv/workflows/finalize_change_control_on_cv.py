# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.changecontrol.v1 import ChangeControl, ChangeControlStatus
from pyavd._cv.client.exceptions import CVChangeControlFailed

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVChangeControl

LOGGER = getLogger(__name__)

CHANGE_CONTROL_STATUS_TO_FINAL_STATE_MAP = {
    ChangeControlStatus.COMPLETED: "completed",
    ChangeControlStatus.RUNNING: "running",
    ChangeControlStatus.SCHEDULED: "scheduled",
    ChangeControlStatus.UNSPECIFIED: None,
}

CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP = {True: "approved", False: None}


def get_change_control_state(cv_change_control: ChangeControl) -> str:
    return (
        CHANGE_CONTROL_STATUS_TO_FINAL_STATE_MAP[cv_change_control.status]
        or CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP[cv_change_control.approve.value]
        or "failed"
        if cv_change_control.error is not None
        else "pending approval"
    )


async def finalize_change_control_on_cv(change_control: CVChangeControl, cv_client: CVClient) -> None:
    """
    Update and finalize a Change Control on CloudVision from the given result.CVChangeControl object.

    Depending on the requested state the Change Control will be left in pending approval, approved, started, completed or canceled.
    In-place update the CVChangeControl object.
    """
    LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)

    # Update missing fields on our local model with data from the CloudVision object.
    change_control.state = get_change_control_state(cv_change_control=cv_change_control)
    if change_control.description is None:
        change_control.name = cv_change_control.change.name
    if change_control.description is None:
        change_control.description = cv_change_control.change.notes

    # TODO: Add CC template

    # Update the change control with name, description etc from our local object if needed.
    if change_control.name != cv_change_control.change.name or change_control.description != cv_change_control.change.notes:
        await cv_client.set_change_control(change_control_id=change_control.id, name=change_control.name, description=change_control.description)
        # Update the local copy to get the exact "last updated" timestamp needed for approval.
        cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
        change_control.state = get_change_control_state(cv_change_control=cv_change_control)
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # If requested state is "pending approval" we are done
    if change_control.requested_state == "pending approval":
        return

    # TODO: Add cancel/delete

    # For all other requested states we first need to approve.
    if change_control.state != "approved":
        await cv_client.approve_change_control(
            change_control_id=change_control.id,
            timestamp=cv_change_control.change.time,
            description="Automatic approval by AVD",
        )
        change_control.state = "approved"
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # If requested state is "approved" we are done.
    if change_control.requested_state == "approved":
        return

    await cv_client.start_change_control(change_control_id=change_control.id, description="Automatically started by AVD")
    change_control.state = "running"
    LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # If requested state is "running" we are done.
    if change_control.requested_state == "running":
        return

    cv_change_control = await cv_client.wait_for_change_control_state(cc_id=change_control.id, state="completed")
    if cv_change_control.error is not None:
        change_control.state = "failed"
        LOGGER.info("finalize_change_control_on_cv: %s", change_control)
        msg = f"Change control failed during execution {change_control.id}: {cv_change_control.error}"
        raise CVChangeControlFailed(msg)

    change_control.state = "completed"
    LOGGER.info("finalize_change_control_on_cv: %s", change_control)

    # If requested state is "Completed" we are done.
    if change_control.requested_state == "completed":
        return
