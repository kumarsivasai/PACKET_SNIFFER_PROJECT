# dashboard.py
import streamlit as st
import pandas as pd

st.title("Network Packet Analyzer Dashboard")

try:
    df = pd.read_csv("captured_packets.csv")
    st.subheader("Captured Packets")
    st.dataframe(df)

    st.subheader("Protocol Distribution")
    st.bar_chart(df["Protocol"].value_counts())

except FileNotFoundError:
    st.error("No captured_packets.csv file found! Run main.py first to capture data.")
