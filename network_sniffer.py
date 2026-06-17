from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):

    if IP in packet:

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"

        print("\n" + "="*50)
        print("Source IP      :", src_ip)
        print("Destination IP :", dst_ip)
        print("Protocol       :", protocol)
        print("Packet Length  :", len(packet))

        try:
            payload = bytes(packet.payload)
            print("Payload        :", payload[:50])
        except:
            print("Payload        : Not Available")

print("Starting Network Sniffer...")
print("Press Ctrl + C to Stop\n")

sniff(prn=process_packet, store=False)