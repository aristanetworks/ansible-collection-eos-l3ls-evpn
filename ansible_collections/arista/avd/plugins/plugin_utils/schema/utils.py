WORDLIST = {
    "aaa": "AAA",
    "af": "AF",
    "api": "API",
    "arp": "ARP",
    "bfd": "BFD",
    "bgp": "BGP",
    "cli": "CLI",
    "cos": "COS",
    "cpu": "CPU",
    "cvp": "CVP",
    "cvx": "CVX",
    "dhcp": "DHCP",
    "dns": "DNS",
    "dot1br": "dot1br",
    "dot1x": "dot1x",
    "dr": "DR",
    "dscp": "DSCP",
    "eos": "EOS",
    "fcs": "FCS",
    "http": "HTTP",
    "icmp": "ICMP",
    "id": "ID",
    "ids": "IDs",
    "igmp": "IGMP",
    "ip": "IP",
    "ipv4": "IPv4",
    "ipv6": "IPv6",
    "is": "IS",
    "isis": "ISIS",
    "lag": "LAG",
    "ldp": "LDP",
    "lfa": "LFA",
    "lldp": "LLDP",
    "lsa": "LSA",
    "l2": "L2",
    "mac": "MAC",
    "mcs": "MCS",
    "mib": "MIB",
    "mka": "MKA",
    "mlag": "MLAG",
    "mpls": "MPLS",
    "mtu": "MTU",
    "nd": "ND",
    "ospf": "OSPF",
    "pbr": "PBR",
    "pim": "PIM",
    "pvlan": "PVLAN",
    "qos": "QOS",
    "ra": "RA",
    "rcf": "RCF",
    "regexp": "RegExp",
    "rp": "RP",
    "rps": "RPs",
    "rs": "RS",
    "rx": "RX",
    "sbfd": "SBFD",
    "sci": "SCI",
    "sha512": "SHA512",
    "spf": "SPF",
    "srlg": "SRLG",
    "ssh": "SSH",
    "ssl": "SSL",
    "tcam": "TCAM",
    "tcp": "TCP",
    "ti": "TI",
    "tls": "TLS",
    "tlvs": "TLVs",
    "ttl": "TTL",
    "tx": "TX",
    "udp": "UDP",
    "url": "URL",
    "vlan": "VLAN",
    "vlans": "VLANs",
    "vn": "VN",
    "vpn": "VPN",
    "vrf": "VRF",
    "vrfs": "VRFs",
    "vrrp": "VRRP",
    "vxlan": "VxLAN",
}


def key_to_display_name(key: str) -> str:
    if not isinstance(key, str):
        raise ValueError(f"Invalid argument passed to 'key_to_display_name'. Must be a string. Got '{type(key)}'")

    words = key.split("_")
    output = []
    for word in words:
        output.append(WORDLIST.get(word.lower(), word.title()))

    return " ".join(output)
