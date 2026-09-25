# print("Router online")
hostname = "R1"
vlan_id = 10
cpu_util = 42.5
is_reachable = True

# print(type(hostname))
# print(type(vlan_id))
# print(type(cpu_util))
# print(type(is_reachable))

### F-String examples | Using f-strings put variables into strings of text
# print(f"{hostname} is reachable: {is_reachable }")
# print(f"{hostname} has a CPU utilization of {cpu_util}%")
# print(f"{hostname} has a VLAN ID of {vlan_id}")

# Multi-line f-string example
# config = f"""hostname {hostname}
# interface Vlan{vlan_id}
#  no shutdown"""
# print(config)

site = input ("Site name: ")