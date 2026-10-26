#!/usr/bin/env python3
"""Day 2 code-along: Nested Loops & Conditionals. Run: python3 <file>"""

# ===== 1. Nested Loop, Live =====
# Print all six row and column pairs, starting at 0 0 and ending at 1 2.
#
# DISCUSS: Before you run the Nested Loop code, imagine both loops used
#          range(2). Put these outputs in the order Python prints them. A: 1 0.
#          B: 0 0. C: 1 1. D: 0 1.
# Your answer:
#
#
print('----- 1. Nested Loop, Live -----')
# TODO: write a nested loop that prints every (row, col) pair
# TODO: row goes through range(2), col through range(3)

# PREDICT before you run: Change the Nested Loop code to range(3) on the
#                         outside and range(2) on the inside. How many lines
#                         print?
# Your answer:
#
#
#
# DISCUSS: With range(3) outside and range(2) inside, a classmate's version
#          prints only 3 lines instead of 6. What's the most likely cause?
# Your answer:
#


# ===== 2. Nested Conditional, Live =====
# Check the operation type first, then if the quantity is positive.
print('----- 2. Nested Conditional, Live -----')
# TODO: check operation first; if it's "ADD", nest a second
# check confirming quantity is greater than 0
operation = "ADD"
quantity = -5

# DISCUSS: Suppose the inner quantity check in the Nested Conditional code
#          never seems to run. What should you trace first? Try it: set
#          operation to "SEARCH" and run.
# Your answer:
#
#


# ===== 3. Putting It Together: Loop + Nested Conditional =====
# Check each line: print whether it is valid, a bad quantity, or a remove.
print('----- 3. Putting It Together: Loop + Nested Conditional -----')
# TODO: loop over transactions; split each into operation and amount
# TODO: put the nested ADD/quantity check inside the loop
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]

# PREDICT before you run: In the Putting It Together code, which check flags
#                         "ADD -5" as invalid: operation == "ADD", amount > 0,
#                         or operation == "REMOVE"?
# Your answer:
#
#
