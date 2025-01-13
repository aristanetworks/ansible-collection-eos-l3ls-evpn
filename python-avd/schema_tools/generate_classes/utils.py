# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


def generate_class_name(class_key: str) -> str:
    """
    Generate ClassName in from class_key.

    "some_key_using_snake_case" => "SomeKeyUsingSnakeCase"
    """
    return "".join(element.capitalize() for element in class_key.split("_"))


def generate_class_name_from_ref(ref: str) -> str:
    """
    Generate ClassName in from a schema ref.

    "eos_cli_config_gen#/keys/ethernet_interfaces/items" => "EosCliConfigGen.EthernetInterfacesItem"
    "eos_cli_config_gen#/keys/router_bgp/keys/vlans/items => "EosCliConfigGen.RouterBgp.VlansItem"
    """
    if "#" not in ref:
        msg = "Schema tooling only works with fully qualified refs with '<schema>#<path>' like 'eos_cli_config_gen#/'"
        raise ValueError(msg)

    # Replacing ref with only the part after #
    ref_schema, ref = ref.split("#", maxsplit=1)

    base_class_elements = [generate_class_name(ref_schema)]

    ref_elements = ref.split("/")
    for ref_index, ref_element in enumerate(ref_elements):
        if ref_element in {"", "keys", "items"}:
            continue

        if len(ref_elements) > ref_index + 1 and ref_elements[ref_index + 1] == "items":
            class_name = generate_class_name(f"{ref_element}_Item")
        else:
            class_name = generate_class_name(ref_element)

        base_class_elements.append(class_name)

    return ".".join(base_class_elements)
