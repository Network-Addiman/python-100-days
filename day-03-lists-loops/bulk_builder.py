# Bulk builder for configuring Switches

## Variables
hostname = input("Hostname: ")
raw_vlans = input("List Vlans (Comma separated): ")
list_vlans = raw_vlans.split(",")
vlans = [int(vlan.strip()) for vlan in list_vlans]
vlans.sort()
starting_port = input("Starting port: ")
ending_port = input("Ending port: ")
ports = []
port_count = 0
ports.append(int(starting_port))
ports.append(int(ending_port))
config = []
vlan_config = []

## Filling in VLAN Configuration
for vlan in vlans:
    vlan_name = input(f"VLAN name for VLAN ID {vlan}: ").strip().upper()
    vlan_config.append(f"vlan {vlan}")
    vlan_config.append(f" name {vlan_name}")
    
## Filling in port configuration
for port in range(ports[0], ports[1] + 1):
    assigned_raw = input(f"Assigned VLAN for Gi0/{port}: ")
    assigned_vlan = int(assigned_raw.strip())
    if assigned_vlan not in vlans:
        print(f"WARNING: VLAN {assigned_vlan} on Gi0/{port} is not in the VLAN list.")
    config.append(f"interface GigabitEthernet0/{port}")
    config.append(" switchport mode access")
    config.append(f" switchport access vlan {assigned_vlan}")
    config.append(f" spanning-tree portfast")
    config.append(f" no shutdown")
    port_count += 1

## Printing Configuration
print(f"""hostname {hostname}\n
!
""")
for item in vlan_config:
    print(item)
print(f"""
!
""")
for item in config:
    print(item)
print(f"Created {len(vlans)} VLANs and {port_count} access ports on {hostname}.")
