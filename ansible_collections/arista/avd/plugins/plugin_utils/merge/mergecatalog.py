# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ansible.errors import AnsibleActionFail

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

try:
    from deepmerge import always_merger
except ImportError as imp_exc:
    DEEPMERGE_IMPORT_ERROR = imp_exc
else:
    DEEPMERGE_IMPORT_ERROR = None


def merge_catalogs(*args: dict) -> dict:
    """Merge catalogs according to the ANTA catalog structure.

    Args:
    ----
        *args (dict): Catalogs to merge.

    Returns:
    -------
        dict: The merged catalog.

    Raises:
    ------
        AristaAvdError: Raised if the required 'deepmerge' Python library cannot be imported.
    """
    if DEEPMERGE_IMPORT_ERROR:
        raise AristaAvdError(message="AVD requires Python deepmerge to be installed") from DEEPMERGE_IMPORT_ERROR

    merged_catalog = {}
    for catalog in args:
        always_merger.merge(merged_catalog, catalog)

    return merged_catalog
