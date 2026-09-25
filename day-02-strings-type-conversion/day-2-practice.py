network_address = input("Network address (/24): ")
interface_id = input("Interface ID (e.g. gi0/0 or fa0/0): ")
vlan_name = input("VLAN Name: ")

###     Creates VLAN ID as an int
octets = network_address.split(".")
vlan_id = int(octets[2])
offset_id = vlan_id + 1000

###     Creates Gateway IP
octets[3] = "1"
gateway_ip = f"{octets[0]}.{octets[1]}.{octets[2]}.{octets[3]}"
# print(gateway_ip)

###     Create Broadcast Address
octets[3] = "255"
broadcast_address = f"{octets[0]}.{octets[1]}.{octets[2]}.{octets[3]}"
# print(broadcast_address)

###     Normalizing Interface ID
clean_interface = interface_id.strip().lower().replace("gi", "GigabitEthernet").replace("fa", "FastEthernet")

###     Create & Print Output
output = f"""\n=== Subnet Info ===
VLAN ID:        {vlan_id}
Gateway:        {gateway_ip}
Broadcast:      {broadcast_address}
Offset check:   {offset_id}

=== Config ===
vlan {vlan_id}
 name {vlan_name.upper()}
!
interface Vlan{vlan_id}
 ip address {gateway_ip} 255.255.255.0
 no shutdown
!
interface {clean_interface}
 switchport mode access
 switchport access vlan {vlan_id}
 no shutdown
"""
print(output)

