device = {
    "hostname": "R1",
    "mgmt_ip": "10.0.0.1",
    "role": "router",
    "os": "iosv",
}
vlans = {10: "USERS", 20: "VOICE", 30: "SERVERS", 99: "MGMT"}
inventory = {
    "R1": {"mgmt_ip": "10.0.0.1", "role": "router"},
    "SW1": {"mgmt_ip": "10.0.0.11", "role": "switch"},
}

# print(device["hostname"])
# print(device["mgmt_ip"])

device["role"] = "edge-router"      # change an existing key
device["site"] = "SAT-LAB"          # add a new key (just assign it)
del device["os"]                    # removes a key

# print(device)

# print(device.get("vendor"))           # None
# print(device.get("vendor", "cisco"))  # cisco | cisco is defining the default response
# print(device)                         

if "mgmt_ip" in device:                 # checks KEYS, not values
    print("Has a management IP")

for vlan_id, name in vlans.items():     # .items() gives you (key, value) pairs
    print(f"vlan {vlan_id}")
    print(f" name {name}")

# print(list(vlans.keys()))             # [10, 20, 30, 99]
# print(len(vlans))                     # 4

print(inventory["SW1"]["mgmt_ip"])      # 10.0.0.11

for hostname, info in inventory.items():
    print(f"{'':-<27}")
    print(f"{hostname:<6}| {info['role']:<8}| {info['mgmt_ip']}")

## Practicing Format Specifiers
print(f"{' Summary Table ':=^30}")       # centered
print("Summary Table".center(30, "-"))   # centered
print("Summary Table".ljust(30, "-"))    # left, padded on the right
print("Summary Table".rjust(30, "-"))    # right, padded on the left