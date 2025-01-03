# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re

MATCH_PATTERN = re.compile(r"^([0-9a-fA-F]{2})([0-9a-fA-F]{2}):([0-9a-fA-F]{2})([0-9a-fA-F]{2}):([0-9a-fA-F]{2})([0-9a-fA-F]{2})$")
REPL = r"\1:\2:\3:\4:\5:\6"


def short_esi_to_route_target(short_esi: str) -> str:
    return re.sub(MATCH_PATTERN, REPL, short_esi)
