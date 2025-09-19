import pandas as pd

def save_packets_to_csv(packets):
    if not packets:
        print("No packets to save.")
        return
    df = pd.DataFrame(packets)
    df.to_csv("captured_packets.csv", index=False)
    print("Captured packets saved to captured_packets.csv")
