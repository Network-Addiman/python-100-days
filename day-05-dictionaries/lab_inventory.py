inventory = {
    "R0-CORE": {"mgmt_ip": "192.168.1.40", "role": "router", "interfaces": {"Gi0/0": "TO-ISP", "Gi0/1": "TO-R1", "Gi0/2": "TO-R2", "Gi0/3": "TO-R3"}},
    "R1": {"mgmt_ip": "192.168.1.41", "role": "router", "interfaces": {"Gi0/0": "TO-DSW1", "Gi0/1": "TO-R0-Core", "Gi0/2": "TO-R2"}},
    "R2": {"mgmt_ip": "192.168.1.42", "role": "router", "interfaces": {"Gi0/0": "TO-DSW2", "Gi0/1": "TO-R1", "Gi0/2": "TO-R0-Core", "Gi0/3": "TO-R3"}},
    "R3": {"mgmt_ip": "192.168.1.43", "role": "router", "interfaces": {"Gi0/0": "TO-SW1", "Gi0/1": "TO-R2", "Gi0/3": "TO-R0-Core"}},
    "DSW1": {"mgmt_ip": "192.168.1.131", "role": "switch", "interfaces": {"Gi0/0": "TO-R1", "Gi0/1": "TO-DSW2", "Gi0/2": "TO-ASW1", "Gi0/3": "TO-ASW2"}},
    "DSW2": {"mgmt_ip": "192.168.1.132", "role": "switch", "interfaces": {"Gi0/0": "TO-R2", "Gi0/1": "TO-DSW1", "Gi0/2": "TO-ASW2", "Gi0/3": "TO-ASW1"}},
    "ASW1": {"mgmt_ip": "192.168.1.133", "role": "switch", "interfaces": {"Gi0/0": "TO-ASW2", "Gi0/1": "TO-HR1", "Gi0/2": "TO-DSW1", "Gi0/3": "TO-DSW2", "Gi1/0": "TO-Pro-DT2", "Gi1/1": "TO-Pro-DT1"}},
    "ASW2": {"mgmt_ip": "192.168.1.134", "role": "switch", "interfaces": {"Gi0/0": "TO-ASW1", "Gi0/1": "TO-Pro-DT3", "Gi0/2": "TO-DSW2", "Gi0/3": "TO-DSW1", "Gi1/0": "TO-HR2"}},
    "SW1": {"mgmt_ip": "192.168.1.67", "role": "switch", "interfaces": {"Gi0/0": "TO-R3", "Gi0/1": "TO-Pro-SRV1", "Gi0/2": "TO-MGMT-DT", "Gi0/3": "TO-HR-SRV1"}},
}
run = 1
print(f"\n{'Summary Table':-^40}")
print(f"{'HOSTNAME':<10} | {'ROLE':<10} | {'MGMT IP':<15}")
print("-----------|------------|---------------")
for hostname, info in inventory.items():
    print(f"{hostname:<10} | {info['role']:<10} | {info['mgmt_ip']:<15}")
while run == 1:
    select = input("""\n1. Query inventory
2. Add device to inventory
3. Show Summary Table
4. Quit
Make a selection: """)
    if select == "1":
        query = input("Enter device name to query: ").upper().strip()
        devices = [item.strip() for item in query.split(",") if item.strip()]

        for item in devices:
            print("")
            print(f"Looking up: {item}")
            if item in inventory:
                info = inventory[item]
                print(f"hostname {item}")
                for intf, desc in info["interfaces"].items():
                    print(f"interface {intf}")
                    print(f" description {desc}")
            else:
                print(f"{item} not found in inventory.")
                print(f"Valid devices: {', '.join(inventory.keys())}")
    elif select == "2":
        name = input("Enter Hostname: ").upper().strip()
        r = input("Enter device role: ").lower().strip()
        ip = input("Enter Management IP: ").strip()
        types = ["switch", "router"]

        ip_in_use = False
        for info in inventory.values():
            if info["mgmt_ip"] == ip:
                ip_in_use = True
                break
        if not name or not ip:
            print("Invalid input detected!")
        elif r not in types:
            print("Invalid device type")
        elif name in inventory:
            print(f"{name} already exists. Not added")
        elif ip_in_use:
            print(f"{ip} is already assigned to another device. Not added.")
        else:
            inventory[name] = {"mgmt_ip": ip, "role": r, "interfaces": {}}
            print(f"{name} added to inventory.")
    elif select == "3":
        print(f"\n{'Summary Table':-^40}")
        print(f"{'HOSTNAME':<10} | {'ROLE':<10} | {'MGMT IP':<15}")
        print("-----------|------------|---------------")
        for hostname, info in inventory.items():
            print(f"{hostname:<10} | {info['role']:<10} | {info['mgmt_ip']:<15}")
    elif select == "4" or select == "quit":
        print("Goodbye!")
        run = 0
    else:
        print("Invalid input.")