from scapy.all import IP, IPv6
from packet_sniffer import start_sniffing
from save_to_csv import save_packets_to_csv
from analyzer import analyze_packet

captured_packets = []

def packet_callback(packet):
    try:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto
        elif IPv6 in packet:
            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst
            protocol = packet[IPv6].nh
        else:
            return  # Skip non-IP packets

        length = len(packet)

        packet_data = {
            "Source IP": src_ip,
            "Destination IP": dst_ip,
            "Protocol": protocol,
            "Length": length
        }

        # Analyze the packet
        threat = analyze_packet(packet_data)
        packet_data["Threat"] = threat

        print(f"{src_ip} --> {dst_ip} | Protocol: {protocol} | Length: {length} | Threat: {threat}")

        captured_packets.append(packet_data)

    except Exception as e:
        print(f"Error processing packet: {e}")

try:
    print("\nStarting packet capture on eth0... Press Ctrl+C to stop.")
    start_sniffing(packet_callback, iface="eth0")

except KeyboardInterrupt:
    print("\nCapture stopped by user.")
    save_packets_to_csv(captured_packets)
