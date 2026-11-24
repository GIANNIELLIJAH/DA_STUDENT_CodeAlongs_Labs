#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE) as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    # TODO: assign `comparisons` to 0
    comparisons = 0
    for row in members:
        comparisons += 1
        if row["member_id"] == member_id:
            return row, comparisons
    return None, comparisons


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# find_linear returns the matching row and the number of rows checked in a o(n) fashion.


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()

linear_total = 0
not_members = 0

for member_id in swipes:
    row, count = find_linear(members, member_id)
    if row is None:
        name = "NOT A MEMBER"
        not_members += 1
    else:
        name = row["name"]
    print(member_id, "|", name, "| comparisons:", count)
    linear_total += count

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
# The search in which swipes there are in the rows of Linear search requires one row check per position examined until a match or end.
# Step 2, answer 2:
# The code itself explains the total of rows within if row returns as NONE then there will result in a check of the entire set of data.
# Linear search requires one row check per position examined until a match or end.
# A swipe with no member may require checks across the entire directory.
# The count will raise a sum to each non member row by 1.



# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off



members_by_id = {}



build_steps = 0

for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1


def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1


print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

linear_running = 0
dict_running = build_steps
pays_off_at = None
swipe_number = 0

for member_id in swipes:
    swipe_number += 1
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    linear_running += linear_count
    dict_running += dict_count
    print("swipe", swipe_number, "|", member_id,
          "| running linear:", linear_running,
          "| running dict:", dict_running)
    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# Building the dictionary costs one step for each member directory row.             
# Prediction: Runs the amount of swipes by adding one to each corresponding member ID.
# Step 3, answer 2:
# Each dictionary lookup costs one counted lookup, plus the earlier build cost.    
# Prediction: The thing that costs the most is the pays at the swipes in which the linear scan runs.
# Building the dictionary costs one step for each member directory row.
# Step 3, answer 2:
# Each dictionary lookup costs one counted lookup, plus the earlier build cost.
# Step 3, answer 3:
# The dictionary amortizes its build cost once running totals cross over.


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
ai_claim = "A dictionary lookup is faster than a linear search for every swipe."
print("AI CLAIM:", ai_claim)

_, front_count = find_linear(members, swipes[0])
_, absent_count = find_linear(members, "M1313")
ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

verdict = (
    "The claim is partly true: dictionary lookups use one comparison per swipe"
    "but include a one-time build cost, so they do not instantly surpass linear"
    "search until enough swipes have been processed."
)
print("VERDICT:", verdict)

# Step 4, answer 1:
# The whole-morning comparison is a ratio of linear work to dictionary work.
# Step 4, answer 2:
# The verdict is based on the printed running totals and the pay-off swipe.

