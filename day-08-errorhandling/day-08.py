
## Concept 1: Exceptions and 'try'/'except'
# raw = input("VLAN ID: ")
# try:
#     vlan = int(raw)
#     print(f"VLAN {vlan} accepted")
# except ValueError:
#     print(f"'{raw}' is not a number")

## Concept 2: else, finally, and grabbing the error message
# try:
#     f = open("inventory.txt")
# except FileNotFoundError as err:
#     print(f"Can't open file: {err}")   # 'err' holds the actual error message
# else:
#     print("File opened, processing...")  # runs ONLY if no exception
#     f.close()
# finally:
#     print("Done.")                       # runs NO MATTER WHAT

## Concept 3: Raising your own exceptions
# def validate_vlan(vlan_id):
#     vlan_id = int(vlan_id)              # may raise ValueError on its own
#     if not 1 <= vlan_id <= 4094:
#         raise ValueError(f"VLAN {vlan_id} out of range 1-4094")
#     return vlan_id

# vlan = input("VLAN: ").strip()
# try:
#     int(vlan)
# except ValueError:
#     print(f"VLAN {vlan} is not a number")
# else:
#     try:
#         validate_vlan(vlan)
#     except ValueError as err:
#         print(f"Rejected: {err}")           # Rejected: VLAN 5000 out of range 1-4094
#     else:
#         print(f"VLAN {vlan} accepted")
# finally:
#     print("Done!")

## Concept 4: The ipaddress module (standard library)
import ipaddress

ip = ipaddress.ip_address("10.10.20.5")
print(ip.is_private)                 # True

try:
    ipaddress.ip_address("10.10.300.5")  # ValueError: does not appear to be an IPv4 or IPv6 address
except ValueError as err:
    print(f"{err}")
    
net = ipaddress.ip_network("10.10.20.0/24")
print(net.netmask)                   # 255.255.255.0  <- handy for IOS configs!
print(net.num_addresses)             # 256
print(ip in net)                     # True

iface = ipaddress.ip_interface("10.10.20.1/24")
print(iface.ip, iface.network)       # 10.10.20.1 10.10.20.0/24