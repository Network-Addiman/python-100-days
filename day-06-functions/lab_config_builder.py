## Lab Data
lab = {
    "SW1": {"mgmt_ip": "10.10.99.11", "vlans": {10: "USERS", 20: "VOICE", 99: "MGMT"},
            "access_ports": {"Gi0/1": 10, "Gi0/2": 20, "Gi0/3": 10}},
    "SW2": {"mgmt_ip": "10.10.99.12", "vlans": {10: "USERS", 30: "PRINTERS", 1003: "OLD"},
            "access_ports": {"Gi0/1": 30, "Gi0/2": 10}},
}

## Device Summary table
def summary_table(lab):
    """Return a summary table of hostnames and management IPs."""
    lines = [
        f"\n{'Summary Table':-^30}",
        f"{'HOSTNAME':<12} | {'MGMT IP':<15}",
        "-------------|---------------",
    ]
    for hostname, data in lab.items():
        lines.append(f"{hostname:<12} | {data['mgmt_ip']:<15}")
    return "\n".join(lines)

## VLAN Validator Function
def is_valid_vlan(vlan_id):
    """Return True if vlan_id is 1-4094 and not a reserved 1002-1005 VLAN."""
    return 1 <= vlan_id <= 4094 and vlan_id not in (1002, 1003, 1004, 1005)

## VLAN Config generator
def vlan_config(vlan_id, name):
    """ Returns VLAN config block as a string """
    lines = [
        f"!\n"
        f"vlan {vlan_id}",
        f" name {name}",
    ]
    return "\n".join(lines) + "\n"

## Access port config generator
def access_port_config(interface, vlan, description="USER-PORT"):
    """ Returns interface block as a string """
    lines = [
        f"!\n"
        f"interface {interface}",
        f" description {description}",
        f" switchport access vlan {vlan}",
        f" switchport mode access",
        f" no shutdown",
    ]
    return "\n".join(lines) + "\n"

## Generates MGMT interface config
def mgmt_config(hostname, mgmt_ip, mask="255.255.255.0", mgmt_vlan=99):
    """ Returns hostname and management interface config """
    lines = [
        f"!\n"
        f"hostname {hostname}",
        f"interface Vlan{mgmt_vlan}",
        f" ip address {mgmt_ip} {mask}",
        f" no shutdown",
    ]
    return "\n".join(lines) + "\n"

## Builds entire config file
def build_device_config(hostname, device_data):
    """ Calls other functions to build and return full config for single device """
    config = ""
    # Adds mgmt interface config based on the supplied hostname
    config += mgmt_config(hostname, device_data["mgmt_ip"])
    # Adds the VLAN configs skipping any invalid VLANs
    for vlan_id, name in device_data["vlans"].items():
        if not is_valid_vlan(vlan_id):
            print(f"{vlan_id} is not valid!")
        else:
            config += vlan_config(vlan_id, name)
    # Adds Access port configurations 
    for port_id, vlan in device_data["access_ports"].items():
        config += access_port_config(port_id, vlan)
    return config
print(summary_table(lab))
while True:
    response = input("""\n1. Build a config file
2. Show Summary Table
3. Quit
Make a selection: """).strip()
    if response == "1":
        while True:
            select = input("Enter hostname, ALL, or BACK: ").strip().upper()
            if select in lab:
                print(build_device_config(select, lab[select]))
            elif select == "ALL":
                for hostname in lab:
                    print(build_device_config(hostname, lab[hostname]))
            elif select == "BACK":
                break
            else:
                print(f"{select} is an invalid selection")
    elif response == "2":
        print(summary_table(lab))
    elif response == "3":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, or 3.")