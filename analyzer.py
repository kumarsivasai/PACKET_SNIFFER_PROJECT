import pandas as pd
from collections import defaultdict
from datetime import datetime, timedelta

# Load malicious IPs
with open("malicious_ips.txt", "r") as file:
    MALICIOUS_IPS = set(line.strip() for line in file.readlines())

# Track traffic rate for anomaly detection
traffic_tracker = defaultdict(list)

# Thresholds
LARGE_PACKET_THRESHOLD = 1500         # Bytes
HIGH_TRAFFIC_THRESHOLD = 50           # Packets per 10 seconds per IP

def analyze_packet(packet_data):
    """
    Analyze a single packet and return a threat level.
    """
    src_ip = packet_data.get("Source IP", "")
    dst_ip = packet_data.get("Destination IP", "")
    protocol = packet_data.get("Protocol", "")
    length = packet_data.get("Length", 0)

    now = datetime.now()
    threat_flags = []

    # === 1. Check for malicious IP ===
    if src_ip in MALICIOUS_IPS or dst_ip in MALICIOUS_IPS:
        threat_flags.append("Malicious IP Detected")

    # === 2. Check for unusually large packet ===
    if length > LARGE_PACKET_THRESHOLD:
        threat_flags.append("Suspicious: Large Packet")

    # === 3. Track packet rate for DoS detection ===
    if src_ip:
        traffic_tracker[src_ip].append(now)
        # Keep only timestamps within the last 10 seconds
        traffic_tracker[src_ip] = [t for t in traffic_tracker[src_ip] if t > now - timedelta(seconds=10)]

        if len(traffic_tracker[src_ip]) > HIGH_TRAFFIC_THRESHOLD:
            threat_flags.append("Suspicious: High Traffic Rate")

    # === 4. Combine threat flags ===
    if len(threat_flags) == 0:
        return "Normal"
    elif len(threat_flags) == 1:
        return threat_flags[0]
    else:
        return f"Critical: {' & '.join(threat_flags)}"
