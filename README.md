# 100 Days of Python for Network Automation

I'm a network and systems administrator with four years of MSP experience (Tier 1 → Tier 2 Sysadmin/Network Admin) and a newly certified CCNA. This repo tracks my progress through a 100-day Python course focused on **network automation and sysadmin tasks**. Every lesson ends with a practical script built around a real networking scenario, with the goal of running them against my Cisco Modeling Labs (CML) home lab.

**Goal:** Build the Python skills to automate day-to-day network work and move into a network admin / automation role.

**Certifications:** CompTIA A+, Network+, Security+ · LPI Linux Essentials · Microsoft AZ-900, SC-900, MS-700 · Cisco CCNA

> All scripts use lab-only values (`lab.local`, RFC 1918 addressing). No production data or credentials live in this repo.

---

## Progress

| Day | Topics | Project Script | What It Does |
|:---:|--------|----------------|--------------|
| 1 | Variables, data types, `input()`, f-strings, writing files | [`Day-1.py`](day-01-variables-fstrings/Day-1.py) | Prompts for device details and generates a base IOS config, saved to `<hostname>_config.txt` |
| 2 | Type conversion, string methods, `split()` and indexing | [`day-2-practice.py`](day-02-strings-type-conversion/day-2-practice.py) | Takes a /24 network and builds the VLAN, SVI and access-port config, deriving the VLAN ID, gateway and broadcast from the octets |
| 3 | Lists, list comprehensions, `for` loops, `range()` | [`bulk_builder.py`](day-03-lists-loops/bulk_builder.py) | Bulk switch builder: creates multiple named VLANs and configures a range of access ports, with a check for undefined VLANs |
| 4 | `if`/`elif`/`else`, comparison and boolean operators, `in`, truthiness, `continue` | [`day-04-conditionals-vlan_validator.py`](day-04-if-elif-else/day-04-conditionals-vlan_validator.py) | Validates a batch of VLAN requests (non-numeric, out-of-range, reserved, existing and duplicate IDs), then builds clean IOS config for the valid ones |
| 5 | Dictionaries, `.get()`, `.items()`/`.keys()`/`.values()`, nested dicts, `while` loops | [`lab_inventory.py`](day-05-dictionaries/lab_inventory.py) | Interactive CML lab inventory: look up devices to generate interface description config, add validated devices, and view a summary table |
| 6 | Functions, parameters and arguments, `return`, default values, scope, docstrings, nested `while` loops and `break` | [`lab_config_builder.py`](day-06-functions/lab_config_builder.py) | Menu-driven switch config builder: helper functions assemble mgmt, VLAN and access-port config per device (or all devices), skipping invalid VLANs |
| 7 | Reading and writing files, `with open()` and file modes (`r`/`w`/`a`), `pathlib`, parsing CSV-style lines | [`day-07-config-builder.py`](day-07-read-write-files/day-07-config-builder.py) | Bulk config generator: reads a device inventory file and writes one IOS config file per router/switch, with a timestamped build log and bad-role warnings |
| 8 | Exceptions, `try`/`except`/`else`/`finally`, `raise`, the `ipaddress` module | [`inventory-checker.py`](day-08-errorhandling/inventory-checker.py) | Inventory validator: checks every line of a raw device inventory, writes the good devices to a clean file and logs each rejected line with a timestamp and reason |

---

## Daily Log

### Day 1: Variables, f-strings and a Config Generator
**Folder:** [`day-01-variables-fstrings`](day-01-variables-fstrings/)

**Concepts:** variables and core data types (`str`, `int`, `float`, `bool`), `type()`, constants, `input()`, single- and multi-line f-strings, writing output to a file with `with open()`.

**Project: IOS base config generator.** The script asks for hostname, management interface, IP, mask and description, then fills them into an IOS config template (hostname, domain name, MOTD banner and interface config). It prints the result and saves it to a `.txt` file named after the device. Sample output: [`R1_config.txt`](day-01-variables-fstrings/R1_config.txt), [`R2_config.txt`](day-01-variables-fstrings/R2_config.txt).

**Practice file:** `hello.py`, used to experiment with data types and f-strings.

**Takeaway:** A multi-line f-string is basically a config template. Swap in variables and one script can generate configs for any number of devices.

---

### Day 2: Strings, Type Conversion and a VLAN/SVI Builder
**Folder:** [`day-02-strings-type-conversion`](day-02-strings-type-conversion/)

**Concepts:** converting `str` → `int` (with math on user input), string methods (`strip()`, `upper()`, `lower()`, `replace()`, `startswith()`), `split()` to break an IP into octets, and list indexing.

**Project: SVI and access-port builder.** Given a /24 network address, the script:
- Splits the address into octets and uses the third octet as the VLAN ID
- Derives the gateway (`.1`) and broadcast (`.255`) addresses
- Normalizes interface shorthand (`gi0/1` → `GigabitEthernet0/1`, `fa0/1` → `FastEthernet0/1`)
- Outputs a subnet summary plus the VLAN, SVI and access-port config

**Practice file:** `day-2.py`, with string method and type conversion drills.

**Takeaway:** Cleaning user input matters. `strip()`, `lower()` and `replace()` turn messy typing like `"  gi0/1 "` into valid IOS syntax.

---

### Day 3: Lists, Loops and a Bulk Switch Builder
**Folder:** [`day-03-lists-loops`](day-03-lists-loops/)

**Concepts:** creating and changing lists (`append()`, `remove()`, `sort()`, `len()`, `in`), list comprehensions, `for` loops, `range()` for port ranges, and counters.

**Project: bulk VLAN and access-port builder.** The script:
- Takes a comma-separated VLAN list, cleans it into sorted integers with a list comprehension, and asks for a name for each VLAN
- Loops through a start-to-end port range and asks which VLAN each `Gi0/x` port belongs to
- Warns if a port is assigned to a VLAN that wasn't defined
- Generates access-port config with PortFast for every port, plus a summary of VLANs created and ports configured

**Practice file:** `day-3.py`, with list methods, looping over switches and VLANs, and generating interface config with `range()`.

**Takeaway:** Loops are where automation starts paying off. Configuring 24 ports takes the same amount of code as configuring 2.

---

### Day 4: Conditionals and a VLAN Request Validator
**Folder:** [`day-04-if-elif-else`](day-04-if-elif-else/)

**Concepts:** `if`/`elif`/`else` chains, comparison operators and chained comparisons (`1002 <= vid <= 1005`), `and`/`or`/`not`, membership tests with `in`, truthiness (empty strings and lists are `False`), `continue`, string slicing, and zero-padded f-string formatting (`{vid:04d}`).

**Project: VLAN request validator.** Takes a batch of messy, human-typed VLAN requests (`"id:name"`) and checks each one before anything reaches the switch. The script:
- Rejects non-numeric IDs, IDs above 4094 and the reserved range 1002–1005
- Skips VLANs that already exist on the switch and duplicates within the same batch
- Uses the IOS default name (`VLAN0040`) when no name is given
- Cleans names to IOS style (trimmed, uppercase, spaces → underscores, max 32 characters)
- Prints a rejection report, then a config block ready to paste, then an accepted/rejected summary

**Practice file:** `day-4.py`, with VLAN range checks, default names, `continue` for interface status triage, and truthiness drills.

**Takeaway:** Validate before you configure. A few `if` checks catch bad input that would otherwise produce a failed or broken config on the device.

---

### Day 5: Dictionaries and a CML Lab Inventory
**Folder:** [`day-05-dictionaries`](day-05-dictionaries/)

**Concepts:** creating dictionaries, reading, changing, adding and deleting keys, `.get()` with defaults, `in` for key checks, `.items()`/`.keys()`/`.values()`, nested dictionaries (`inventory["SW1"]["mgmt_ip"]`), `while` loops for menus, and f-string alignment specifiers (`:<10`, `:-^40`).

**Project: interactive CML lab inventory.** My CML lab topology (core router, distribution and access switches) is stored as a nested dictionary of hostname → management IP, role and interface descriptions. A menu-driven script lets me:
- Query one or more devices (comma-separated) and generate their `interface` / `description` config
- Add a new device, with checks for blank input, invalid roles, duplicate hostnames and management IPs already in use
- View a formatted summary table of hostname, role and management IP
- Get a list of valid devices when a lookup fails

**Practice file:** `day-05.py`, with dictionary CRUD, `.get()` defaults, looping with `.items()`, nested lookups and format specifier drills.

**Takeaway:** Nested dictionaries are basically a source of truth. Once the lab lives in one structure, generating config or reports from it is just a loop.

---

### Day 6: Functions and a Lab Config Builder
**Folder:** [`day-06-functions`](day-06-functions/)

**Concepts:** defining and calling functions, parameters vs. arguments (positional and keyword), `return` vs. `print()`, default parameter values, local scope, docstrings, `"\n".join()` to build multi-line config, and nested `while` loops with `break` for sub-menus.

**Project: lab config builder.** The inline logic from earlier days is refactored into small, reusable functions, each returning a config block as a string:
- `is_valid_vlan()` checks the 1–4094 range and blocks reserved VLANs 1002–1005
- `mgmt_config()`, `vlan_config()` and `access_port_config()` each build one section of IOS config, with defaults for mask, management VLAN and port description
- `build_device_config()` takes a hostname and that device's data and assembles the full config, skipping (and warning about) invalid VLANs
- A menu builds config for one switch or `ALL`, has a `BACK` option to return to the main menu, and shows a hostname/management IP summary table

**Practice file:** `day-06.py`, with a banner function, returning config strings, a boolean validator, default parameters (`portfast=True`) and scope drills.

**Takeaway:** Functions should return data, not print it. Keeping the printing in the main program means the same functions can later push config to a device with Netmiko instead of just displaying it.

---

### Day 7: File I/O and a Bulk Config Generator
**Folder:** [`day-07-read-write-files`](day-07-read-write-files/)

**Concepts:** opening files with `with open()`, file modes (`"r"` read, `"w"` overwrite, `"a"` append), `read()` vs. `readlines()` vs. looping over the file line by line, `strip()` and `split(",")` with unpacking to parse CSV-style lines, skipping blank lines and `#` comments, writing with `write()` and `"\n".join()`, `pathlib.Path` (`mkdir(exist_ok=True)` and the `/` operator for joining paths), constants, and a first look at `datetime` for timestamps.

**Project: CML bulk config generator.** Instead of typing base configs by hand, I keep the lab in an [`inventory.txt`](day-07-read-write-files/inventory.txt) file (hostname, management IP, mask, role) and the script builds a config file for every device. The script:
- Reads the inventory, ignoring blank lines and commented-out devices that aren't deployed yet
- Uses `build_config()` to assemble shared base config (hostname, domain, MOTD banner), then adds the role-specific management interface (`Gi0/0` for routers; `Vlan99` plus a default gateway for switches)
- Writes each device to its own file in `configs/`, for example [`R1.cfg`](day-07-read-write-files/configs/R1.cfg) and [`SW1.cfg`](day-07-read-write-files/configs/SW1.cfg)
- Handles bad inventory lines gracefully: an unknown role (like a `siwtch` typo) prints a warning and skips that device instead of crashing
- Appends each run to a timestamped `build.log` and prints a summary (`Built 5 configs: 3 routers, 2 switches`)

**Practice file:** `day-07.py`, with read/write/append drills, writing a single config and log entry from a function, and creating folders and files with `pathlib`.

**Takeaway:** Separating data from code is the big shift. The inventory file is the source of truth, so adding a device to the lab means adding one line of text, not editing the script.

---

### Day 8: Error Handling and an Inventory Validator
**Folder:** [`day-08-errorhandling`](day-08-errorhandling/)

**Concepts:** exceptions and tracebacks, `try`/`except` with specific exception types (`ValueError`, `FileNotFoundError`), capturing the message with `except ... as err`, `else` and `finally`, raising my own exceptions with `raise ValueError(...)`, the standard-library `ipaddress` module (`ip_address()`, `ip_network()`, `ip_interface()`, `.netmask`, `in` for subnet membership), `enumerate()` for line numbers, and `next()` to skip a header row.

**Project: inventory validator.** Before any inventory feeds a config generator like Day 7's, this script checks it line by line so one bad entry can't crash the run or produce a broken config. The script:
- Prompts for the inventory file and asks again if the file doesn't exist, instead of crashing
- Uses `validate_line()` to check each line for the right number of fields, an empty hostname, a valid prefix length (/8–/30), a valid VLAN (1–4094, not reserved 1002–1005), a real IP address, and an IP inside the lab management subnet (`10.10.99.0/24`)
- Catches both my own `raise`d errors and Python's built-in ones (like `int("abc")` or `10.10.99.300`) in a single `except ValueError`, so every bad line is handled the same way
- Writes the valid devices to [`clean_inventory.txt`](day-08-errorhandling/clean_inventory.txt), converting each prefix to a dotted-decimal mask ready for IOS
- Writes a separate log for each run (for example `errors_2026-10-01_14h53m57s.log`), with one `timestamp | line number | original line | reason` entry per rejected device

Sample input: [`raw_inventory.txt`](day-08-errorhandling/raw_inventory.txt) has 9 devices, of which 4 pass and 5 are rejected.

**Practice file:** `day-08.py`, with `try`/`except` on user input, `else`/`finally` flow, raising custom errors, and `ipaddress` drills.

**Takeaway:** Validate and log, don't crash. Collecting errors with their line numbers and reasons turns a script that dies on the first typo into a tool that tells you exactly what to fix. Timestamps belong in one place, where the log entry is written, not scattered through every error message.

---

## Running the Scripts

Requires Python 3. Most scripts are interactive, so run them and answer the prompts (the Day 4 validator runs on its built-in sample data, the Day 7 generator reads `inventory.txt`, and the Day 8 validator asks for an inventory filename such as `raw_inventory.txt`, so run those two from inside their own folders):

```bash
cd day-03-lists-loops
python bulk_builder.py
```

<!--
=====================================================================
DAILY TEMPLATE: copy this block for each new day (this comment doesn't
show on GitHub). Also add a row to the Progress table above.
=====================================================================

### Day X: <Topic> and <Project Name>
**Folder:** [`day-XX-topic-name`](day-XX-topic-name/)

**Concepts:** <comma-separated list of what the lesson covered>

**Project: <project name>.** <One or two sentences on the scenario the script solves.>
- <Key feature 1>
- <Key feature 2>
- <Key feature 3>

**Practice file:** `<file>.py`, <what you drilled>.

**Takeaway:** <One sentence: what clicked, or how it applies to real network work.>

---
-->
