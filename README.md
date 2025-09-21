# Live Packet Capturing & Analysis Tool

## **Overview**
This is a mini-project that captures network packets, analyzes them, and saves them for further analysis. It is a simplified version of Wireshark, designed to be lightweight and easy to use.

## **Features**
- Capture live network packets
- Display source/destination IPs, protocol, and packet length
- Save captured data to a CSV file
- Optional Streamlit dashboard for visualization

## **Project Structure**
```
packet_capture_project/
│
├── main.py # Main program to run the sniffer
├── packet_sniffer.py # Core packet capture logic
├── save_to_csv.py # Save captured data to CSV
├── dashboard.py # Optional Streamlit dashboard for visualization
├── captured_packets.csv # Generated CSV file after capture
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```



## **How It Works**
1. **Run `main.py`**  
   - Starts live packet capture.
   - Displays packet information in real-time.
   - Stores captured data in memory.

2. **Stop Capture**  
   - Press `Ctrl + C`.
   - Captured data will automatically be saved into `captured_packets.csv`.

3. **View Data**  
   - Open the CSV file directly, or run the Streamlit dashboard for visualization:
     ```bash
     streamlit run dashboard.py
     ```

## Installation & Running


1. Clone the project from github:
   ```bash
   git clone https://github.com/kumarsivasai/PACKET_SNIFFER_PROJECT.git
   ```


2. Install dependencies in your main Folder:
   ```bash
   pip install -r requirements.txt
   ```


3. Activate the virtual Environment:
   ```bash
   source venv/bin/activate
   ```

4. first List the files:
   ```bash
   ls
   ```


5. List of files In the project folder:
   ```bash
   main.py
   packet_sniffer.py
   save_to_csv.py
   dashboard.py
   captured_packets.csv
   requirements.txt
   README.md
   ``` 

6. run the main.py file:
   ```bash
   sudo python main.
   ```
   **NOTE :   Befour going to run this code please do some modifications in your code  that is open the main.py  code and modify the iface based on your connected internet like etho or wlan0 like that**

   **If you run the code you can see the packet are caputuring wait some time and collect the packets and enter ctrl+c**




7. All That Packets are stored in the project folder:
   ```
   you can see like this the stored csv file:

   [INFO] Capture stopped by user.
   [INFO] Total packets captured: 14
   [INFO] Session saved: captured_packets_20250921_035042.csv
   ```


8. THIS INDICATES captured_packets_20250921_035042.csv:
   ```
    20250921 → Date in YYYYMMDD format → 2025-09-21
    035042 → Time in HHMMSS format → 03:50:42 (3:50 AM + 42 seconds).
    .csv → File type
   ```

9. We can see that packets in live Capturing also
   ```
    open another terminal and run this command:
   
     run dashboard.py
   ```
10. If Any address capture the maor that 1500 packets that packet should be highlight with red color that feature also can see in the live capturing



## **Learning Outcomes**

By completing this project, you will be able to:

1. **Understand Network Packets**  
   - Learn the structure of network packets (headers, payload, protocols).  
   - Identify source and destination IPs, ports, and protocols.

2. **Capture Live Network Traffic**  
   - Use Python and Scapy to capture packets in real-time.  
   - Understand how packet sniffers work for monitoring network traffic.

3. **Analyze Network Data**  
   - Extract meaningful information like packet length, protocol type, and timestamps.  
   - Learn to interpret traffic patterns and timing between packets.

4. **Data Storage and Export**  
   - Save captured packet data into CSV files for further analysis.  
   - Understand best practices for storing and organizing network logs.

5. **Visualization**  
   - Use Streamlit and matplotlib to create visual dashboards.  
   - Learn how to plot packet statistics, protocols distribution, and traffic over time.

6. **Ethical Hacking Awareness**  
   - Understand the importance of ethical packet sniffing.  
   - Learn to capture traffic only on networks you own or have permission to monitor.

7. **Python Programming Skills**  
   - Improve modular programming by splitting functionality across multiple files.  
   - Work with external libraries like Scapy, Pandas, and Streamlit.



## **Disclaimer**
- This project is **for educational and ethical purposes only**.  
- Do **NOT** use this tool to capture network traffic on networks you do not own or have explicit permission to monitor.  
- Capturing or analyzing packets on unauthorized systems **without consent is illegal**.  
- The author of this project is **not responsible** for any misuse or damages caused by using this tool.  
- **Use it responsibly and at your own risk.**


## **Conclusion**

The Packet Capturing & Analysis Tool is a lightweight, educational project that demonstrates the fundamentals of network packet capture, analysis, and visualization.  

By completing this project, you gain hands-on experience with:  
- Capturing live network traffic using Python and Scapy  
- Analyzing packet information such as IP addresses, protocols, lengths, and timestamps  
- Saving and visualizing network data for further insights  
- Understanding the ethical and legal considerations of network monitoring  

This project provides a solid foundation for further exploration in network security, ethical hacking, and network administration. It is designed to be modular, easy to use, and suitable for study purposes.
