import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import glob
import os
import time

st.set_page_config(page_title="Live Packet Capture Dashboard", layout="wide")
st.title("📡 Live Packet Analysis Dashboard")

# --- Function to get latest CSV ---
def get_latest_csv():
    csv_files = glob.glob("captured_packets_*.csv")
    if not csv_files:
        return None
    return max(csv_files, key=os.path.getctime)

# --- Highlight suspicious packets ---
def highlight_suspicious(row):
    if "Threat" in row and "Suspicious" in row["Threat"]:
        return ['background-color: #ffcccc; color: red; font-weight: bold'] * len(row)
    return [''] * len(row)

# --- Create placeholders for table and chart ---
table_placeholder = st.empty()
chart_placeholder = st.empty()

# --- Sidebar placeholders for metrics ---
st.sidebar.subheader("📈 Session Stats")
total_packets_placeholder = st.sidebar.empty()
suspicious_packets_placeholder = st.sidebar.empty()

# --- Live dashboard loop ---
while True:
    latest_csv = get_latest_csv()
    if not latest_csv:
        st.error("⚠ No capture files found! Run main.py first.")
        break

    try:
        df = pd.read_csv(latest_csv)
    except Exception as e:
        st.error(f"Error reading {latest_csv}: {e}")
        break

    # Sort packets chronologically
    if "Timestamp" in df.columns:
        df = df.sort_values(by="Timestamp", ascending=True).reset_index(drop=True)

    # --- Display table ---
    table_placeholder.dataframe(
        df.style.apply(highlight_suspicious, axis=1),
        height=400,
        use_container_width=True
    )

    # --- Display threat distribution chart ---
    if not df.empty and "Threat" in df.columns:
        threat_counts = df["Threat"].value_counts()

        # Extra small and compact graph
        fig, ax = plt.subplots(figsize=(2, 0.8))  # Width=2, Height=0.8 inches

        ax.bar(threat_counts.index, threat_counts.values, color=['green', 'red'])
        ax.set_title("Threats", fontsize=5)       # Very small title font
        ax.set_xlabel("Type", fontsize=4)         # Smaller x-label
        ax.set_ylabel("Count", fontsize=4)        # Smaller y-label
        ax.tick_params(axis='both', labelsize=4)  # Tiny tick labels

        chart_placeholder.pyplot(fig)
    else:
        chart_placeholder.warning("No 'Threat' data found!")

    # --- Update sidebar metrics ---
    total_packets_placeholder.metric("Total Packets Captured", len(df))
    suspicious_count = len(df[df["Threat"].str.contains("Suspicious")])
    suspicious_packets_placeholder.metric("Suspicious Packets", suspicious_count)

    # --- Refresh every 1 second ---
    time.sleep(1)
