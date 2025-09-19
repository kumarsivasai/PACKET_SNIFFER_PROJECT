import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Packet Analysis Dashboard")

try:
    df = pd.read_csv("captured_packets.csv")
except FileNotFoundError:
    st.error("No captured_packets.csv file found! Run main.py first to capture packets.")
    st.stop()

st.subheader("Captured Packets")
st.dataframe(df)

st.subheader("Threat Distribution")
threat_counts = df["Threat"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(threat_counts.index, threat_counts.values)
plt.title("Threat Level Distribution")
plt.xlabel("Threat Type")
plt.ylabel("Count")
st.pyplot(plt)
