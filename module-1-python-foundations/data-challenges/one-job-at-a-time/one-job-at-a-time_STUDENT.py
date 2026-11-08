#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    """Return whether a donation record has the required fields and pounds."""
    parts = record.split(",")

    if len(parts) != 5:
        return False, "wrong field count"
    if parts[2].strip() == "":
        return False, "missing category"

    try:
        float(parts[3])
    except ValueError:
        return False, "pounds is not a number"
    return True, ""


records = read_donations(DATA_FILE)
valid = []
for record in records:
    ok, reason = validate_donation(record)
    if ok:
        valid.append(record)
    else:
        print("rejected", record.split(",")[0] + ":", reason)
print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
#
# Step 1, answer 2:
#


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    """Summarize valid donations by category and total pounds."""
    by_category = {}
    total_pounds = 0.0
    count = 0
    for record in valid_records:
        parts = record.split(",")
        category = parts[2].strip()
        pounds = float(parts[3])
        if category not in by_category:
            by_category[category] = {"donations": 0, "pounds": 0.0}
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        total_pounds += pounds
        count += 1
    return {
        "records": count,
        "total_pounds": total_pounds,
        "by_category": by_category,
    }


summary = summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
#


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    """Write a summary as indented JSON and return the output path."""
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    return path


def run_pipeline(in_path, out_path, summarize):
    """Validate donations, summarize the valid records, and export the result"""
    kept = []
    for record in read_donations(in_path):
        ok, _reason = validate_donation(record)
        if ok:
            kept.append(record)
    return export_summary(summarize(kept), out_path)


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    """Summarize valid donations by day and total pounds"""
    by_day = {}
    total_pounds = 0.0
    count = 0
    for record in valid_records:
        parts = record.split(",")
        day = parts[4].strip()
        pounds = float(parts[3])
        if day not in by_day:
            by_day[day] = {"donations": 0, "pounds": 0.0}
        by_day[day]["donations"] += 1
        by_day[day]["pounds"] += pounds
        total_pounds += pounds
        count += 1
    return {"records": count, "total_pounds": total_pounds, "by_day": by_day}


run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
with open("donation_summary.json") as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:
#
# Step 4, answer 2:
#
