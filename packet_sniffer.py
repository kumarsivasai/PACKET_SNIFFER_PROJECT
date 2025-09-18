# packet_sniffer.py
from scapy.all import sniff, IP, TCP, UDP

def analyze_packet(packet):
    """Extract useful information from a captured packet."""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else str(packet[IP].proto)
        length = len(packet)

        return {
            "Source IP": src_ip,
            "Destination IP": dst_ip,
            "Protocol": protocol,
            "Length": length
        }
    return None


def start_sniffing(packet_callback, iface=None, count=0):
    """
    Start sniffing packets.
    - iface: Network interface (e.g., 'eth0', 'wlan0'). None = default interface
    - count: 0 means unlimited until stopped manually
    """
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(iface=iface, prn=packet_callback, store=False, count=count)
