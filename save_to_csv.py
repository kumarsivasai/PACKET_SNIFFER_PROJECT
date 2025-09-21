import csv

def save_packets_to_csv(packets, filename):
    print(f"[DEBUG] save_packets_to_csv called with {len(packets)} packets")
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Added Timestamp and Session ID columns
            writer.writerow(["Timestamp", "Session ID", "Source", "Destination", "Protocol", "Length", "Threat"])
            for pkt in packets:
                writer.writerow([
                    pkt["timestamp"],
                    pkt["session_id"],
                    pkt["src"],
                    pkt["dst"],
                    pkt["protocol"],
                    pkt["length"],
                    pkt["threat"]
                ])
        print(f"[+] Saved {len(packets)} packets to {filename}")
    except Exception as e:
        print(f"[ERROR] Could not save packets to CSV: {e}")
