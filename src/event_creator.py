# functions to create campus events at random
# Both linked list and array implementation can call this script

# IMPLEMENTATION OF EVENT CLASS
class Event:
    def __init__(self, id, title, date, time, location):
        self.id = id if id is not None else unique_ID() # ALLOWS FOR MANUAL OR AUTO ASSIGNED IDS
        self.title = title
        self.date = date
        self.time = time
        self.location = location
    
    # FOR EASE OF DISPLAYING THE INFORMATION IN EACH EVENT, INSTEAD OF A MEMORY LOCATION
    def __repr__(self):
        return f"Event({self.id}, {self.title}, {self.date}, {self.time}, {self.location})"


# Create a unique ID
import random

_usedIDs = set()  # INITIALIZE AS EMPTY SET. WE DON'T WANT ANY REPEATS

# TRACKS USED ID NUMBERS
def unique_ID():
    while True:
        newID = random.randint(100000, 999999) # 6 DIGIT RANGE
        if newID not in _usedIDs:
            _usedIDs.add(newID)
            return newID
