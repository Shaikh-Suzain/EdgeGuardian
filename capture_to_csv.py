import pandas as pd
from scapy.all import sniff

packet_data = []

def packet_callback(packet):
    packet_data.append({
        'time': packet.time,
        'src': packet[0][1].src if packet.haslayer(1) else 'N/A',
        'dst': packet[0][1].dst if packet.haslayer(1) else 'N/A',
        'proto': packet[0].proto if hasattr(packet[0], 'proto') else 'N/A'
    })

sniff(prn=packet_callback, count=50)

df = pd.DataFrame(packet_data)
df.to_csv('packets.csv', index=False)
print("Packets saved to packets.csv")
