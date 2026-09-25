DOMAIN = "lab.local"
BANNER = "^Authorized Access only^"

hostname = input("Hostname: ")
management_interface = input("Interface: ")
ip_address = input("IP Address: ")
subnet_mask = input("Subnet Mask: ")
interface_description = input("Interface Description: ")

output = f"""hostname {hostname}
ip domain-name {DOMAIN}
banner motd {BANNER}
!
interface {management_interface}
 description {interface_description}
 ip address {ip_address} {subnet_mask}
 no shutdown
!
end"""

print("\n--- Generated Config ---")
print(output)
print(f"\nConfig generated for {hostname} ({ip_address})\n")

filename = f"{hostname}_config.txt"
with open(filename, "w") as f:
    f.write(output)
print(f"Saved to {filename}")
