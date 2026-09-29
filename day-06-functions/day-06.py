
## Creating a Banner Function
def show_banner():
    print("=" * 40)
    print("       CML Lan Confg Generator ")
    print("=" * 40)
show_banner()

## VLAN Config Function
def make_vlan(vlan_id, name):
    return f"vlan {vlan_id}\n name {name}\n"
config = make_vlan(10, "USERS")
config += make_vlan(20, "VOICE")
# print(config)

## Function for checking if VLAN is in valid range
# vid = int(input("Check VLAN:"))
def is_valid_vlan(vlan_id):
    """Return True if vlan_id is 1-4094 and not a reserved 1002-1005 VLAN."""
    return 1 <= vlan_id <= 4094 and vlan_id not in (1002, 1003, 1004, 1005)

#if not is_valid_vlan(vid):
#    print("Reserved or out-of-range VLAN")
#else:
#    print("All good!")

## Function that creates acces port config lines
def access_port(interface, vlan, description="USER-PORT", portfast=True):
    lines = [
        f"interface {interface}",
        f" description {description}",
        " switchport mode access",
        f" switchport access vlan {vlan}",
    ]
    if portfast:
        lines.append(" spanning-tree portfast")
    return "\n".join(lines) + "\n"

print(access_port("Gi0/1", 10))
print(access_port("Gi0/2", 20, description="PHONE", portfast=False))

def build():
    hostname = "SW1"    # local to build()
    return hostname

build()
# print(hostname)  # -> NameError. Capture the return value instead:
name = build()
# print(name)