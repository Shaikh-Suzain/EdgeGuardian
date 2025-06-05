import pandas as pd
from scapy.all import sniff, Ether, IP

packet_data = []

def packet_callback(packet):
    # Check for Ethernet layer for src and dst MAC addresses
    src = packet[Ether].src if packet.haslayer(Ether) else 'N/A'
    dst = packet[Ether].dst if packet.haslayer(Ether) else 'N/A'
    
    # Check for IP layer for protocol number
    proto = packet[IP].proto if packet.haslayer(IP) else 'N/A'
    
    packet_data.append({
        'time': packet.time,
        'length': len(packet),
        'src': src,
        'dst': dst,
        'proto': proto
    })

print("Starting packet capture...")
sniff(prn=packet_callback, count=50)
print("Packet capture complete.")

df = pd.DataFrame(packet_data)
df.to_csv('packets.csv', index=False)
print("Packets saved to packets.csv")
