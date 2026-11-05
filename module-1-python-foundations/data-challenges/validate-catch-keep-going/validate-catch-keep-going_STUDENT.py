#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "../data/service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = (f.read().splitlines())

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
EXPECTED_FIELDS = 5
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]

def validate_request(row):
    fields = row.split(",")
    
    # 
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    
    service_id, complaint, borough, days_open, status = fields
    
    #
    if borough == "":
        return False, "borough is empty"
    
    # 
    if status not in ALLOWED_STATUS:
        return False, "status not allowed: " + status
        
    return True, "ok"


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
# SR-1004 has a missing borough, so it correctly flags as False and says borough is empty
#
# Step 1, answer 2:
# SR-1009 uses "Escalated" for status, which isn't in our allowed list, so it catches it with status not allowed: Escalated
#


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
valid = 0
for row in rows:
    ok, reason = validate_request(row)
    if ok:
        valid += 1
    else:
        # Pull out just the ID (first column) and print the rejection reason
        print(row.split(",")[0], "REJECTED -", reason)

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1:
# The validator successfully caught every malformed or incomplete row instead of letting bad data slip through
#
# Step 2, answer 2:
# We ended up with a clean count of valid rows ready for analysis, while logging exactly why the bad ones were dropped
#


# ===== Day 3 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
total_days = 0
counted = 0

for row in rows:
     ok, reason = validate_request(row)
     if not ok:
         continue
     days_open = int(row.split(",")[3])
     total_days += days_open
     counted += 1
     print(row.split(",")[0], "days open:", days_open)

print("average days open:", total_days, counted)


# Step 3, answer 1:
# Rows that failed Day 1 checks (like missing boroughs or invalid statuses) were skipped right away using continue
#
# Step 3, answer 2:
# The script still crashed halfway through because one of the rows had text like 3 days instead of just a number in the days column, causing int() to throw a ValueError
#
# Step 3, answer 3:
# It crashed on the first row that contained non-numeric text in that 4th index position, proving we need error handling
#


# ===== Day 4 =====

def check_days_open(value):
    try:
        days = int(value)
    except ValueError:
        return False, "days_open is not a number: " + value
    
    if days < 0:
        return False, "days_open is negative: " + value
        
    return True, "ok"


total_days = 0
counted = 0
skipped = 0

for row in rows:
    ok, reason = validate_request(row)
    if ok:
        fields = row.split(",")
        ok, reason = check_days_open(fields[3])
        if ok:
            total_days += int(fields[3])
            counted += 1
        else:
            skipped += 1
            print(fields[0], "SKIPPED -", reason)
    else:
        skipped += 1

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
# Using the try/except block allowed us to catch formatting errors gracefully instead of letting the script completely break
#
# Step 4, answer 2:
# Any row with invalid or negative numbers got safely diverted into our skip counter with a clear explanation
#
# Step 4, answer 3:
# We successfully processed all clean records, resulting in 11 counted rows and 4 skipped rows with a final correct average
