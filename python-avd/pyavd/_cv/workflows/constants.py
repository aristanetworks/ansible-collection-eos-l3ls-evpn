# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

EOS_CLI_PORTFAST_WARNING = (
    "! portfast should only be enabled on ports connected to a single host. Connecting hubs, concentrators, switches, bridges, etc. "
    "to this interface when portfast is enabled can cause temporary bridging loops. Use with CAUTION."
)
"""Text pattern to match EoS CLI warning regarding utilization of the spanning-tree portfast feature."""
