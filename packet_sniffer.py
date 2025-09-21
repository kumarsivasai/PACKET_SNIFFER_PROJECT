from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6

# Protocol number to name mapping
PROTOCOL_MAP = {
    6: "TCP",
    17: "UDP",
    1: "ICMP",
    58: "ICMPv6",
    67: "DHCP",
    68: "DHCP",
}

def process_packet(packet, captured_packets, session_id, session_csv_filename, *args):
    """
    Processes each network packet, extracts details, appends them to captured_packets,
    and writes to CSV for live Streamlit dashboard updates.
    """
    try:
        # Extract IP details
        if IP in packet:  # IPv4
            src = packet[IP].src
            dst = packet[IP].dst
            proto_num = packet[IP].proto
            length = packet[IP].len
        elif IPv6 in packet:  # IPv6
            src = packet[IPv6].src
            dst = packet[IPv6].dst
            proto_num = packet[IPv6].nh
            length = packet[IPv6].plen
        else:
            return  # Skip non-IP packets

        proto = PROTOCOL_MAP.get(proto_num, f"Unknown({proto_num})")
        threat = "Normal" if length <= 1500 else "Suspicious: Large Packet"

        # Print live in terminal
        print(f"{src} --> {dst} | Protocol: {proto} | Length: {length} | Threat: {threat}")

        # Append to memory
        captured_packets.append({
            "Timestamp": session_id,
            "Source": src,
            "Destination": dst,
            "Protocol": proto,
            "Length": length,
            "Threat": threat
        })

        # Save to CSV in real-time
        import pandas as pd
        df = pd.DataFrame(captured_packets)
        df.to_csv(session_csv_filename, index=False)

    except Exception as e:
        print(f"[ERROR] Failed to process packet: {e}")
