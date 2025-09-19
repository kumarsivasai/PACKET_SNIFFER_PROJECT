from scapy.all import sniff

def start_sniffing(callback, iface="eth0"):
    """
    Starts live packet capture using Scapy.
    """
    sniff(prn=callback, iface=iface, store=False)
