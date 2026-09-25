
## Creates string variable from input
vlan = input("VLAN ID: ")
vlan = int(vlan)        # Converts str to int
print(vlan + 100)       # Prints variable int value plus 100

## Same concept as above but with less lines
VLAN = int(input("VLAN ID: "))
print(VLAN + 200)

##  String Methods practice
raw = "   GigabitEthernet0/1   "

print(raw.strip())                                     # Removes leading/trailing whitespace
print(raw.upper())                                     # "   GIGABITETHERNET0/1   "
print(raw.lower())                                     # "   gigabitethernet0/1   "

"Gi0/1".replace("Gi", "GigabitEthernet")        # "GigabitEthernet0/1"
"Gi0/1".startswith("Gi")                        # True

ip = "10.10.10.1"
ip.split(".")                                   # ['10', '10', '10', '1'] a list of strings

octets = "192.168.10.1".split(".")
print(octets[0])
print(octets[2])

user_input = "  gi0/1  "
clean = user_input.strip().replace("gi", "Gigabitethernet")
print(clean)


