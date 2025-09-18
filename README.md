# Packet Capturing & Analysis Tool

## Overview
A mini-project that captures network packets, analyzes them, and saves them for further analysis. Similar to a simplified version of Wireshark.

## Features
- Capture live packets
- Display source/destination IPs, protocol, and length
- Save captured data to CSV
- Optional Streamlit dashboard for visualization

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the sniffer:
   ```bash
   sudo python main.py
   ```


2. Run the sniffer:
   ```bash
   sudo python main.py
   ```


3. Stop capture with Ctrl + C. Data will be saved to captured_packets.csv:


2. View captured data using dashboard:
   ```bash
   streamlit run dashboard.py
   ```


## Requirements.txt

```
Python 3.8+
Scapy, Pandas, Streamlit
```





---

## **How It Works**
### Workflow:
1. **Run `main.py`**
   - Starts live packet capture.
   - Displays packet info in real-time.
   - Saves all data to a list.

2. **Stop Capture**
   - Press `Ctrl + C`.
   - Data automatically saved into `captured_packets.csv`.

3. **View Data**
   - Open the CSV file or run `dashboard.py` for visualization.

---

## **Example Run**
**Terminal Output:**
```
Starting packet capture... Press Ctrl+C to stop.
192.168.1.5 --> 142.250.180.14 | Protocol: TCP | Length: 66
192.168.1.5 --> 224.0.0.252 | Protocol: UDP | Length: 82
192.168.1.5 --> 142.250.180.14 | Protocol: TCP | Length: 54
```



**Saved CSV Example:**
| Source IP   | Destination IP | Protocol | Length |
|-------------|---------------|----------|--------|
| 192.168.1.5 | 142.250.180.14 | TCP      | 66     |
| 192.168.1.5 | 224.0.0.252    | UDP      | 82     |

---

## **Mini Project Summary**
- **Core Code:** `packet_sniffer.py` (capture logic)
- **Main Program:** `main.py` (execution + saving data)
- **CSV Exporter:** `save_to_csv.py`
- **Optional UI:** `dashboard.py`
- **Dependencies:** `requirements.txt`
- **Docs:** `README.md`

This structure is **clean**, **modular**, and perfect for submission as a mini project.
