#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.
# The coordinator needs to track tool inventory, whether each tool is
# available, and the condition of each tool before it is used.

tools = ["wrenches", "drills", "screws", "flatheads", "screwdrivers", "nuts", "bolts"]
tools_availability = {
    "wrenches": True,
    "drills": False,
    "screws": True,
    "flatheads": True,
    "screwdrivers": True,
    "nuts": True,
    "bolts": False,
}
tools_condition = {
    "wrenches": "good",
    "drills": "needs battery",
    "screws": "new",
    "flatheads": "worn",
    "screwdrivers": "good",
    "nuts": "new",
    "bolts": "rusted",
}

# Your answer:
# I used a list for the tool names and dictionaries for availability and
# condition so each tool can be tracked individually by name.
#

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====
# name: identifies which tool the record is about.
# available: the coordinator needs to know if the tool can be used right now.
# condition: the stakeholder needs to know whether the tool is usable or worn out.

# Your answer:
# name explains what tool is being tracked.
# available comes from the need to know if a tool is ready to be borrowed.
# condition comes from the need to know whether a tool is safe or usable.
#

# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.

class Tool:
    def __init__(self, name, condition, available):
        self.name = name
        self.condition = condition
        self.available = available

    def is_ready_for_use(self):
        usable_conditions = {"good", "new", "like new"}
        return self.available and self.condition.lower() in usable_conditions

# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

wrench = Tool("wrench", "good", True)
drill = Tool("drill", "needs battery", False)

print(wrench.name, wrench.condition, wrench.available)
print(drill.name, drill.condition, drill.available)
print(wrench.is_ready_for_use())
print(drill.is_ready_for_use())

wrench.available = False
print(wrench.available, drill.available)
print(wrench.is_ready_for_use(), drill.is_ready_for_use())

# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
# I designed the class around the three facts the coordinator needs most: the
# tool's name, whether it is available, and whether it is in usable condition.
# I rejected adding more general metadata because the stakeholder's request is
# focused on inventory readiness, not broad catalog details.
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
#