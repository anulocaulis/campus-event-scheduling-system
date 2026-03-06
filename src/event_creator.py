# FOR USE IN ASSIGNING RANDOM ID NUMBERS
import random

# IMPLEMENTATION OF EVENT CLASS
class Event:
    def __init__(self, title, date, time, location, id=None):
        self.id = id if id is not None else unique_ID() # ALLOWS FOR MANUAL OR AUTO ASSIGNED IDS
        self.title = title
        self.date = date
        self.time = time
        self.location = location
    
    # FOR EASE OF DISPLAYING THE INFORMATION IN EACH EVENT, INSTEAD OF A MEMORY LOCATION
    def __repr__(self):
        return f"Event({self.id}, {self.title}, {self.date}, {self.time}, {self.location})"


# EMPTY SET TO KEEP TRACK OF WHICH IDS HAVE BEEN USED. WE DON'T WANT ANY REPEATS
_usedIDs = set() 

# TRACKS USED ID NUMBERS
def unique_ID():
    while True:
        newID = random.randint(100000, 999999)     # 6 DIGIT RANGE FOR MORE VARIABILITY
        if newID not in _usedIDs:                  # CHECK IF newID ALREADY IN USED SET
            _usedIDs.add(newID)                    # ADD newID TO USED SET
            return newID
