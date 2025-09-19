import pandas as pd

# Load malicious IPs
with open("malicious_ips.txt", "r") as file:
    MALICIOUS_IPS = set(line.strip() for line in file.readlines())

def analyze_packet(packet_data):
    """
    Analyze a single packet and return a threat level.
    """
    src_ip = packet_data.get("Source IP", "")
    dst_ip = packet_data.get("Destination IP", "")
    protocol = packet_data.get("Protocol", "")
    length = packet_data.get("Length", 0)

    threat = "Normal"

    # Check for malicious IP
    if src_ip in MALICIOUS_IPS or dst_ip in MALICIOUS_IPS:
        threat = "Malicious IP Detected"

    # Unusually large packets
    elif length > 1500:
        threat = "Suspicious: Large Packet"

    return threat
