from pathlib import Path
from datetime import datetime
import ipaddress

valid_devices = []
errors = []
LAB_NET = ipaddress.ip_network("10.10.99.0/24")

def is_valid_vlan(vlan_id):
    """Return True if vlan_id is 1-4094 and not a reserved 1002-1005 VLAN."""
    return 1 <= vlan_id <= 4094 and vlan_id not in (1002, 1003, 1004, 1005)

def validate_line(line):
    fields = line.strip().split(",")
    
    if len(fields) != 4:
        raise ValueError("Expected 4 fields")

    hostname, ip, prefix, vlan = fields

    if not hostname:
        raise ValueError("Hostname is empty")

    if not 8 <= int(prefix) <= 30:
        raise ValueError("Prefix not valid")

    if not is_valid_vlan(int(vlan)):
        raise ValueError("VLAN not valid: Reserved or out-of-range VLAN")
    
    iface = ipaddress.ip_interface(f"{ip}/{prefix}")
    if iface.ip not in LAB_NET:
        raise ValueError(f"{iface.ip} not in {LAB_NET}")

    return {"hostname": hostname, "mgmt_ip": str(iface.ip), "mask": str(iface.netmask), "vlan": vlan}

out_dir = Path()
log_file = out_dir / f"errors-{datetime.now():%Y-%m-%d_%Hh%Mm%Ss}.log"
while True:
    filename = input("Filename: ")
    try:
        inv = open(filename, "r")
    except FileNotFoundError as err:
        print(f"{datetime.now():%Y-%m-%d %H:%M:%S}: Can't open file {err}")
    else:
        print("File opened, processing...")
        with inv:
            next(inv)
            for line_num, line in enumerate(inv, start=2):
                try:
                    device = validate_line(line)
                except ValueError as err:
                    stamp = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
                    errors.append(f"{stamp} | Line {line_num} | {line.strip()} | {err}")
                else:
                    valid_devices.append(device)
        with open(log_file, "w") as log:
            log.write("\n".join(errors) + "\n")
        with open("clean_inventory.txt", "w") as clean:
            clean.write("hostname,mgmt_ip,mask,vlan\n")
            for d in valid_devices:
                clean.write(f"{d['hostname']},{d['mgmt_ip']},{d['mask']},{d['vlan']}\n")
        print("Inventory cleaned.")
        print(f"{len(valid_devices)} valid, {len(errors)} rejected")
        if errors:
            print(f"See {log_file} for details")
        print("Goodbye!")
        break