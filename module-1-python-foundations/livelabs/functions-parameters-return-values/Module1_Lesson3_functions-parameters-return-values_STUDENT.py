#!/usr/bin/env python3
"""Day 3 code-along: Functions, Parameters & Return.... Run: python3 <file>"""


def greet(user_name):
    print("Welcome, " + user_name)
    #print("Welcome ", user_name)
    #print("Welcome f{user_name}")

greet("Heather")
greet("Micheal")
# ===== 1. Define and Call, Live =====
# Build a reusable greeting: one function, called twice, prints it twice.
print('----- 1. Define and Call, Live -----')
# TODO: define greet() to print a welcome message, then call it twice


# ===== 2. Parameters, Live =====
# Make greet work for anyone: pass in a name, then greet Jordan and Amara.
print('----- 2. Parameters, Live -----')
# TODO: add a name parameter to greet
# TODO: print a personal welcome for each of 2 names

# DISCUSS: Order double(5): A: n becomes 5. B: body runs. C: it gets called.
# Your answer:
#
# PREDICT before you run: If double(n) prints n * 2, what does double(5) print?
# Your answer:
#


# ===== 3. Return, Live =====
# Send a value back with return to use it in math. double(5) + 1 prints 11.
print('----- 3. Return, Live -----')
# TODO: write double(n) using return (not print)
# TODO: add 1 to its result and print that

# DISCUSS: A function should return a doubled value, but total + 1 raises
#          TypeError. Using what you just saw in the Return, Live code, what's
#          the most likely cause?
# Your answer:
#
#
