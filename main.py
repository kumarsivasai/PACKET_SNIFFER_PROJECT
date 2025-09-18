# main.py
from packet_sniffer import analyze_packet, start_sniffing
from save_to_csv import save_packets_to_csv

packets_data = []

def packet_callback(packet):
    """Callback for every captured packet."""
    packet_info = analyze_packet(packet)
    if packet_info:
        packets_data.append(packet_info)
        print(f"{packet_info['Source IP']} --> {packet_info['Destination IP']} | "
              f"Protocol: {packet_info['Protocol']} | Length: {packet_info['Length']}")

try:
    start_sniffing(packet_callback)
except KeyboardInterrupt:
    print("\nCapture stopped by user.")
    save_packets_to_csv(packets_data)
