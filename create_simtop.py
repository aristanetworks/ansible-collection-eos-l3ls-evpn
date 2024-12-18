import csv
import re
from collections import defaultdict
from pathlib import Path
import json
import logging
from pathlib import Path

from yaml import load
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, YamlLoader, write_file


def natural_sort_key(s):
    """Key function for natural sorting."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def is_valid_interface(name):
    pattern = r'^(Ethernet|Management)\d+$'
    return bool(re.match(pattern, name))

def create_reciprocal_map(csv_file):
    """
    Creates a reciprocal map of network connections from a CSV file.

    Parameters:
        csv_file (str): Path to the CSV file.
        directory (str): Path to the directory (not used here but included for future extension).
        yaml_file (str): Path to the YAML file (not used here but included for future extension).

    Returns:
        dict: Reciprocal map of network connections.
    """
    connection_map = defaultdict(dict)

    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        _ = next(reader)  # Skip the header row

        for row in reader:
            device = row[1].strip() if len(row) > 1 else None
            interface = row[2].strip() if len(row) > 2 else None
            peer = row[4].strip() if len(row) > 4 else None
            peer_interface = row[5].strip() if len(row) > 5 else None

            if not device or not interface:
                # Skip rows with missing essential info
                continue

            if not(is_valid_interface(interface) and is_valid_interface(peer_interface)):
                continue

            # Add connection to the map
            if interface in connection_map[device]:
                existing_peer, existing_peer_interface = connection_map[device][interface]
                if (peer and peer != existing_peer) or (peer_interface and peer_interface != existing_peer_interface):
                    raise ValueError(f"Conflicting information for {device} {interface}")

            # Add reciprocal connection to the map
            if peer and peer_interface:
                connection_map[device][interface] = (peer, peer_interface)

                if peer_interface in connection_map[peer]:
                    existing_device, existing_device_interface = connection_map[peer][peer_interface]
                    if (device and device != existing_device) or (interface and interface != existing_device_interface):
                        raise ValueError(f"Conflicting information for {peer} {peer_interface}")

                connection_map[peer][peer_interface] = (device, interface)

    return connection_map

def output_connections(connection_map, device_hostname_to_id):
    """
    Outputs connections in the specified format.

    Parameters:
        connection_map (dict): Reciprocal map of network connections.
        device_hostname_to_id (dict): Mapping from device hostname to device ID.
    """
    device_id_to_hostname = {}
    for device_id, device_hostname in device_hostname_to_id.items():
        device_id_to_hostname[device_hostname] = device_id

    printed = defaultdict(lambda:None)
    for device_id, device_hostname in sorted(device_id_to_hostname.items(), key=lambda x : natural_sort_key(x[0])):
        interfaces = connection_map[device_hostname]
        for interface, (peer, peer_interface) in sorted(interfaces.items(), key=lambda x : natural_sort_key(x[0])):
            if printed[(device_id, interface)]:
                continue

            if not peer or not peer_interface:
                # Above we are adding only connections which have both ends
                raise ValueError(f"Unexpected Connection")

            peer_id = device_hostname_to_id.get(peer, None)
            if not peer_id:
                raise ValueError(f"Missing deviceID for {peer}")


            short_intf = interface.replace("Ethernet","Et")
            short_peer_intf = peer_interface.replace("Ethernet", "Et")
            connection = f"{device_id}({short_intf})---({short_peer_intf}){peer_id}"
            printed[(peer_id, peer_interface)] = True
            print(connection)

def prettyPrintMap(inputMap, inverse=False):
    mapToPrint = inputMap
    if inverse:
        inverse = defaultdict(list)
        for key, value in mapToPrint.items():
            inverse[value].append(key)
        mapToPrint = inverse

    if not mapToPrint:
        return
    # Determine the alignment width
    max_value_length = max(len(value) for value in mapToPrint)

    # Print the inverted dictionary
    for value, keys in sorted(inverse.items(), key=lambda x: natural_sort_key(x[0])):
        keys_str = ", ".join(keys)
        print(f"# {value:<{max_value_length}} -> {keys_str}")

def read_configs(self, device_list: list[str], config_dir: str, config_suffix: str) -> dict[str, dict]:
    return {device: self.read_config(device, config_dir, config_suffix) for device in device_list}

def read_one_config(device: str, config_dir: str, config_suffix: str) -> dict:
    path = Path(config_dir, f"{device}.{config_suffix}")
    if not path.exists():
        raise Exception(f"Could not find structured config file for '{device}'. The documentation may be incomplete.")

    config = path.open(encoding="UTF-8").read()
    return config

def read_structured_configs(device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict[str, dict]:
        return {device: read_one_structured_config(device, structured_config_dir, structured_config_suffix) for device in device_list}

def read_one_structured_config(device: str, structured_config_dir: str, structured_config_suffix: str) -> dict:
    path = Path(structured_config_dir, f"{device}.{structured_config_suffix}")
    if not path.exists():
        logging.warning("Could not find structured config file for '%s'. The documentation may be incomplete.", device)

    with path.open(encoding="UTF-8") as stream:
        if structured_config_suffix in ["yml", "yaml"]:
            return load(stream, Loader=YamlLoader)  # noqa: S506

        # JSON
        return json.load(stream)

# Example usage
example_dir = "cv-pathfinder"
fabric_name = "CWAN"
csv_file_path = f"/workspaces/ayush-avd/ansible_collections/arista/avd/examples/{example_dir}/documentation/fabric/{fabric_name}-topology.csv"
directory_path = f"/workspaces/ayush-avd/ansible_collections/arista/avd/examples/{example_dir}/intended/configs/"

structured_config_dir = f"/workspaces/ayush-avd/ansible_collections/arista/avd/examples/{example_dir}/intended/structured_configs/"
structured_config_suffix = "yml"
yaml_file_path = "path/to/your/yaml_file.yaml"

try:
    connection_map = create_reciprocal_map(csv_file_path)
    diMap = {}
    devTypeCounter = defaultdict(lambda:1)
    for i, device in enumerate(connection_map):
        ymlinputs = read_one_structured_config(device, structured_config_dir, structured_config_suffix)
        vlans = ymlinputs.get("vlans")
        devType = "evpnsfe"
        if vlans:
            devType = "evpnrtr"
        counter = devTypeCounter[devType]
        diMap[device] = f"{devType}{counter}"
        devTypeCounter[devType]  = counter + 1
    print("############################q")
    print("### DeviceID -> Hostname ###")
    prettyPrintMap(diMap, inverse=True)
    print("############################\n\n")

    print("############################")
    print("######## Connections #######")
    output_connections(connection_map, diMap)
    print("############################\n\n")

    device_id_to_hostname = {}
    for device_id, device_hostname in diMap.items():
        device_id_to_hostname[device_hostname] = device_id

    sorted_devs = sorted(device_id_to_hostname.keys(), key=natural_sort_key)
    for dev in sorted_devs:
        print(f"###################### {dev}")
        print(f"dut:{dev}")
        print("[numExtPorts 15]")
        print("[agentsToRun StunClient SuperServer]")
        print("[agentArgv SuperServer --service=SslManager --service=StunServer --service=SswanManager]")
        print("[dirsToClone /etc/sswan /etc/turnserver]")
        print(f"prompt {device_id_to_hostname[dev]}%P")
        print(read_one_config(device_id_to_hostname[dev], directory_path, "cfg"))
        print("\n\n")
except ValueError as e:
    print(f"Error: {e}")
