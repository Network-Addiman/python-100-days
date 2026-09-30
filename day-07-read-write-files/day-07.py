# ## Read, write, append practice 
# with open("inventory.txt", "a") as f:
#     f.write("hostname R1\n")
#     f.write("ip domain-name lab.local\n")
# with open("inventory.txt", "r") as f:
#     whole = f.read()
# print(whole)

# ## Function for creating R1 config and updating a log file
# config_lines = ["hostname R1", "no ip domain-lookup", "end"]
# def write_config():
#     with open("R1.cfg", "w") as f:
#         f.write("\n".join(config_lines) + "\n")
#     with open("build.log", "a") as f:
#         f.write("Generated R1.cfg\n")
#     print("Config generated and log updated")

# write_config()

# from pathlib import Path

# out_dir = Path("configs")
# out_dir.mkdir(exist_ok=True)        # create the folder, no error if it already exists

# cfg_file = out_dir / "R1.cfg"       # the / operator joins path parts
# with open(cfg_file, "w") as f:
#     f.write("hostname R1\n")

# print(cfg_file.exists())            # True
from pathlib import Path
with open("inventory.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        hostname, interface, ip, mask = line.split(",")
        out_dir = Path("configs")
        out_dir.mkdir(exist_ok=True)        # create the folder, no error if it already exists

        cfg_file = out_dir / f"{hostname}.cfg"       # the / operator joins path parts
        with open(cfg_file, "w") as f2:
            f2.write(f"hostname {hostname}\n")
            f2.write(f"interface {interface}\n")
            f2.write(f" ip address {ip} {mask}\n")
            f2.write(f" no shutdown")

        print(cfg_file.exists())            # True

