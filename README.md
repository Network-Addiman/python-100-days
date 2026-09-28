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

## Running the Scripts

Requires Python 3. Most scripts are interactive, so run them and answer the prompts (the Day 4 validator runs on its built-in sample data):

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
