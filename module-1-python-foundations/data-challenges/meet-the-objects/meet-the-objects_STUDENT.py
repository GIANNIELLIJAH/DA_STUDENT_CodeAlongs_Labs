#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "bike_stations.json"  # edit the filepath with the data

with open("../data/" + DATA_FILE) as f:    
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
names = []
bikes = []
# TODO: loop over `stations`; append each one's "name" to `names`
for station in stations:
    names.append(station['name'])
    bikes.append(station['bikes_available'])

names.pop(2)

print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")

# Step 1, answer 1:
#each station contains an attribute name, bikes,, sation is the object in the string.
# Step 1, answer 2:
#name and bikes have empty lists.
# Step 1, answer 3:
#printed name and bikes


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    # TODO: in __init__, assign each parameter to self.<same name>
    # TODO: add a parameter and self.<name> for each extra field you agreed
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def __init__(self,station_id, name, capacity, bikes_available, needs_maintenance, ):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

    def __str__(self) -> str:
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

    def __repr__(self) -> str:
        return f"Station({self.name!r}, {self.bikes_available})"


fleet = [
    Station(
        s.get("station_id"),
        s["name"],
        s["capacity"],
        s["bikes_available"],
        s.get("needs_maintenance", False),
    )
    for s in stations
]

busy, quiet = next(
    (first, second)
    for i, first in enumerate(fleet)
    for second in fleet[i + 1 :]
    if first.needs_restock() == second.needs_restock()
)
print(busy.needs_restock(), quiet.needs_restock())
busy.bikes_available = 0
print(busy.needs_restock(), quiet.needs_restock())

# Step 2, answer 1:
#created a fleet list for name capacity bikes available and scheduled maintenance
# Step 2, answer 2:
#printed needed restocks in the options
# Step 2, answer 3:
# busy and quiet are our objects that go within the list.
# Step 2, answer 4:
#


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
# printed the lists within steps 2.
# Step 3, answer 2:
#prints out the enumerated objects.


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
van_list = [station for station in fleet if station.needs_restock()]

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
# printed the last and final which were the lists we created in steps 2 and 3.
# Step 4, answer 2:
# if they needed restock within the stations.
# Step 4, answer 3:
#Printed the stations themselves.

