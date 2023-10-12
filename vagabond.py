from scapy.all import ARP, Ether, srp


target_ip = input("Enter target IP. Ex: 192.168.1.69/24 ")
# create ARP packet to send to local devices 
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
#combines two object packets into one. ether refers to Ethernet Framework. Arp refers to ARP packet
packet = ether/arp

#receives the packet back. Gaining IP and MAC info
result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients on a network
clients = []

load_module()

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))