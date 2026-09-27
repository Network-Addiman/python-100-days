existing_vlans = [1, 10, 20, 99]
requests = [
    "30:Servers",
    "20:Voice",
    "abc:Printers",
    "1003:Legacy",
    "5000:TooBig",
    "40:",
    "30:Servers Again",
    "50:guest wifi",
    "60:this vlan name is way too long for ios to accept",
]
accepted = []
config_lines = []
accepted_count = 0
rejected_count = 0

for i in requests:
    info = i.split(":")
    # print(info)
    if not info[0].isdigit():
        print(f"[REJECT] {info[0]}      -> is not a number")
        rejected_count =+ 1
        continue
        # print(rejected_count)
    elif int(info[0]) in existing_vlans:
        print(f"[SKIP]   {info[0]}      -> already exists")
        rejected_count += 1
        continue
    elif int(info[0]) > 4094:
        print(f"[REJECT] {info[0]}      -> out of range")
        rejected_count += 1
        continue
    elif 1002 <= int(info[0]) <= 1005:
        print(f"[REJECT] {info[0]}      -> reserved")
        rejected_count += 1
        continue
    elif int(info[0]) in accepted:
        print(f"[SKIP]   {info[0]}      -> duplicate in request")
        rejected_count += 1
        continue
    vid = int(info[0])
    if not info[1]:
        info[1] = f"VLAN{vid:04d}"
    name = info[1]
    name = name.strip().upper().replace(" ", "_")
    name = name[:32]
    accepted.append(vid)
    config_lines.append(f"vlan {vid}")
    config_lines.append(f" name {name}")
    accepted_count += 1

print(f"""\n! ---- Config to apply ---- """)
for line in config_lines:
    print(line)
print(f"\nSummary: {accepted_count} accepted, {rejected_count} rejected/skipped")


    


