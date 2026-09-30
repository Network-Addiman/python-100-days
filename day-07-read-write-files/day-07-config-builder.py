## Imports
from pathlib import Path
from datetime import datetime

BANNER = "banner motd ^AUTHORIZED ACCESS ONLY - Private lab network. Activity is monitored and logged.^"
routers = 0
switches = 0
configs = 0

def build_config(hostname, ip, mask, role):
    lines = [
        f"hostname {hostname}",
        "no ip domain-lookup",
        "ip domain-name lab.local",
        BANNER,
    ]
    if role == "router":
        lines += ["interface GigabitEthernet0/0"]
    elif role == "switch":
        lines += ["ip default-gateway 10.10.99.254", "interface Vlan99"]
    else:
        return None
    lines += [f" ip address {ip} {mask}", " no shutdown", "end"]
    return lines

out_dir = Path("configs")
out_dir.mkdir(exist_ok=True)
log_file = out_dir / f"build.log"     

with open(log_file, "a") as log:
    log.write(f"\n=== Run {datetime.now():%Y-%m-%d %H:%M:%S} ===\n")
with open("inventory.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        hostname, ip, mask, role = line.split(",")
        cfg_file = out_dir / f"{hostname}.cfg"       
        output = build_config(hostname, ip, mask, role)
        if output is None:
            print(f"WARNING: unknown role '{role}' for {hostname}, skipping")
            with open(log_file, "a") as log:
                log.write(f"WARNING: unknown role '{role}' for {hostname}, device skipped\n")
            continue
        if role == "router":
            routers += 1
        elif role == "switch":
            switches += 1
        configs += 1 
        with open(cfg_file, "w") as f2:
            f2.write("\n".join(output) + "\n")
        with open(log_file, "a") as log:
            log.write(f"Generated configs/{hostname}.cfg ({role})\n")
print(f"Built {configs} configs: {routers} routers, {switches} switches")