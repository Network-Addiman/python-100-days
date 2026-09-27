# if/elif/else Practice

## Creating VLAN and confirming usable
vlan = int(input("Create VLAN: "))
if vlan < 1 or vlan > 4094:
    print(f"VLAN {vlan}: out of range")
elif 1002 <= vlan <= 1005:
    print(f"VLAN {vlan}: reserved (legacy FDDI/Token Ring)")
else:
    print(f"VLAN {vlan}: OK")

## Setting VLAN name
name = input("VLAN name: ").strip().upper()
if not name:
    name = "UNNAMED"

## Printing Config
print(f"""
vlan {vlan}
 name {name}
""")

## continue Practice
interfaces = ["Gi0/1", "Gi0/2", "Gi0/3"]
statuses = ["up", "err-disabled", "down"]

for i in range(len(interfaces)):
    if statuses[i] == "up":
        continue
    print(f"{interfaces[i]} needs attention: {statuses[i]}")


## Practicing 
mtu = 9000
if mtu > 1500:
    print("jumbo")
elif mtu == 1500:
    print("standard")
else:
    print("low")

trunk_allowed = [10, 20, 30]

if vlan in trunk_allowed:
    print("Allowed")
else:
    print("Unauthorized")

## bool practice
ports = input("How many ports? ")
if ports:
    print("Configuring ports...")
else:
    print("Invalid entry")

