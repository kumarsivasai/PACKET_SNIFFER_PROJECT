# save_to_csv.py
import pandas as pd

def save_packets_to_csv(packets_list, filename="captured_packets.csv"):
    """Save the captured packets to a CSV file."""
    if packets_list:
        df = pd.DataFrame(packets_list)
        df.to_csv(filename, index=False)
        print(f"Packets saved to {filename}")
    else:
        print("No packets were captured to save!")
