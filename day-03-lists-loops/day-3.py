vlans = [10, 20, 30]
switches = ["SW1", "SW2", "SW3"]

# print(switches[0])
# print(vlans[0])

# vlans.append(99)         Adds to VLANs
# print(len(vlans))        Counts VLANs in List
# print(vlans[3])          Prints 4th item in vlans list
# print(20 in vlans)           
# print(50 in vlans)
# vlans.remove(20)
# vlans.append(20)
# print(vlans[3])
# print(vlans)
# vlans.sort()
# print(vlans)
# switches.append("SW0")
# print(switches)
# switches.sort()
# print(switches)


raw = input("Enter VLANIDS (comma-separated): ")
raw_vlan_list = raw.split(",")
clean_vlan = [int(vlan.strip()) for vlan in raw_vlan_list]
# print(clean_vlan)

for sw in switches:
    print(f"Backing up config on {sw}...")
for vlan in clean_vlan:
    print(f"vlan {vlan}")
    print(f" name DATA_{vlan}")
print("End")

for i in range(1, 5):
    print(f"interface GigabitEthernet0/{i}")
    print(f" switchport access vlan 99")
    print(f" switchport mode access")



