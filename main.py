import signal
import sys
from datetime import datetime
from scapy.all import sniff
from packet_sniffer import process_packet

captured_packets = []
session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
session_csv_filename = f"captured_packets_{session_id}.csv"

def stop_sniffer(sig, frame):
    print("\n[INFO] Capture stopped by user.")
    print(f"[INFO] Total packets captured: {len(captured_packets)}")
    print(f"[INFO] Session saved: {session_csv_filename}")
    sys.exit(0)

def main():
    print(f"[INFO] Starting packet capture (Session ID: {session_id})...")
    print("[INFO] Press Ctrl+C to stop capture.")

    signal.signal(signal.SIGINT, stop_sniffer)

    try:
        # Change iface="eth0" to your actual interface (run `ip a` to check)
        sniff(
            iface="eth0",
            prn=lambda pkt: process_packet(pkt, captured_packets, session_id, session_csv_filename),
            store=False
        )
    except PermissionError:
        print("[ERROR] Permission denied! Run the script with sudo.")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
