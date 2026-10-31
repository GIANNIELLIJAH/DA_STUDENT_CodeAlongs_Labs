#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = ("data/station_taps.csv") # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    comparisons = 0
    for row in records:
        comparisons += 1 
        if row[0] == tap_id:
            return comparisons
    return comparisons 
#T040:
#T999:

print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1:
#T001 is one of the earlier variables found, needing less comparisons.
# Step 1, answer 2:
#T999 needs more comparison due to the fact that it is a O(1) going one by one needing more comparison. 


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
print("rows:", size, "| worst-case comparisons:", worst)

pairs = 0
for row1 in taps:
    for row2 in taps:
        pairs += 1

print("total rows:", len(taps), "total pairs:", pairs)
big = len(taps) * 10
print("scan's worst case on big rows:", len(taps), "| pair loop's count:", len(taps) * len(taps))
# Step 2, answer 1:
# The worst-case scan scales are linear (O(n)) with the number of rows.
# Step 2, answer 2:
# The nested loop is multipled twice making it an exponent and this means it grows faster at a linear rate.


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
card_ids = []
tap_counts = []
comparisons = 0

for row in taps:
    card = row[1]
    found = False
    for i in range(len(card_ids)):
        comparisons += 1
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
    if not found:
        card_ids.append(card)
        tap_counts.append(1)
busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
# The list being parrallel makes the list harder to track and requires higher comparisons.
# Step 3, answer 2:
# Searching for lists on every cylinder requires more tedious work due to the fact that special datas will inevitably grow within the set.


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
taps_by_card = {}
lookups = 0

for row in taps:
    lookups += 1
    card = row[1]
    if card in taps_by_card:
        taps_by_card[card] += 1
    else:
        taps_by_card[card] = 1

stations = set()
for row in taps:
    stations.add(row[2])

repeat_riders = 0
for count in taps_by_card.values():
    if count > 1:
        repeat_riders += 1 > 1
#T001:
#T040:
#T999:
print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1: Dictionaries provide O(1) average time complexity lookups, avoiding manual nested loops.
# Step 4, answer 2: Sets automatically discard duplicates, making unique collection effortless.
# Step 4, answer 3: Tracking frequencies with a dictionary is cleaner and drastically faster than parallel lists.
# Step 4, answer 4: Code design matches the problem structure (Key-Value associations map naturally to dictionaries).

# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None with your Day 2 value; keep `stations` a set
summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": stations,
    "taps_by_card": taps_by_card,
}

print("about to serialize", len(summary), "keys")

#text = json.dumps(summary, indent=2)
#print(text)

# Step 5, answer 1: json.dumps() crashes with a TypeError because sets are not natively JSON serializable.
# Step 5, answer 2: JSON only supports basic data types like strings, numbers, lists, dictionaries, booleans, and null.
# Step 5, answer 3: To fix this, Python sets must be converted into lists before serialization.


import json

# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# TODO: assign summary["stations"] to a type JSON can hold; keep the key
summary["stations"] = list(stations)  # Convert tuple/set to a JSON-supported list

# TODO: json.dump() `summary` into a with open("tap_summary.json", "w")
with open("tap_summary.json", "w") as f:
    json.dump(summary, f)

# TODO: replace None with json.load() of "tap_summary.json"
with open("tap_summary.json", "r") as f:
    reloaded = json.load(f)

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1: 
# JSON converts dictionary keys (like card IDs) from integers/other types to strings 
# during serialization, which is why round trip may or may not fail or require key conversion

# Step 6, answer 2: 
# Tuples do not run a JSON round trip because JSON only supports lists
# tuples are reloaded back as Python lists
#
