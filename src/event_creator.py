# FOR USE IN ASSIGNING RANDOM ID NUMBERS
import random

# IMPLEMENTATION OF EVENT CLASS
# THIS CLASS REPRESENTS A SINGLE SCHEDULED EVENT OBJECT WITH BASIC ATTRIBUTES
# SUCH AS title, date, time, location, AND A UNIQUE id
class Event:
    # CONSTRUCTOR FOR Event OBJECTS
    # INITIALIZES ALL EVENT ATTRIBUTES AND ENSURES EACH EVENT HAS A UNIQUE id
    def __init__(self, title, date, time, location, id=None):
        # IF AN id IS PROVIDED, USE IT
        # OTHERWISE CALL unique_ID() TO AUTOMATICALLY GENERATE A UNIQUE RANDOM id
        self.id = id if id is not None else unique_ID() # ALLOWS FOR MANUAL OR AUTO ASSIGNED ID
        # STORE BASIC EVENT INFORMATION
        self.title = title
        self.date = date
        self.time = time
        self.location = location
    
    # __repr__() DEFINES HOW THE OBJECT IS DISPLAYED WHEN PRINTED OR INSPECTED
    # THIS RETURNS A READABLE STRING INSTEAD OF A DEFAULT MEMORY ADDRESS
    def __repr__(self):
        return f"Event({self.id}, {self.title}, {self.date}, {self.time}, {self.location})"

    # __eq__() DEFINES HOW TWO Event OBJECTS ARE COMPARED USING ==
    # EVENTS ARE CONSIDERED EQUAL IF THEIR UNIQUE id VALUES MATCH
    def __eq__(self, other):
        # IF other IS NOT AN Event OBJECT, RETURN NotImplemented
        if not isinstance(other, Event): return NotImplemented
        # COMPARE EVENTS BY THEIR UNIQUE id VALUES
        return self.id == other.id

    # sortKey() RETURNS A TUPLE USED FOR SORTING EVENTS
    # EVENTS WILL BE SORTED BY date FIRST, THEN time, THEN location
    # THIS METHOD IS USED BY SORTING ALGORITHMS TO DETERMINE ORDER
    def sortKey(self):
        return (self.date, self.time, self.location)

# EMPTY SET USED TO TRACK ALL GENERATED EVENT IDS
# THIS PREVENTS DUPLICATE IDS FROM BEING CREATED
_usedIDs = set() 

# FUNCTION THAT GENERATES A UNIQUE RANDOM EVENT ID
def unique_ID():
    # LOOP UNTIL A UNIQUE ID IS FOUND
    while True:
        # GENERATE A RANDOM 6-DIGIT NUMBER
        newID = random.randint(100000, 999999)     
        # CHECK IF GENERATED ID ALREADY BEEN USED
        if newID not in _usedIDs:                  
            # ADD NEW ID TO SET OF USED IDS
            _usedIDs.add(newID)                 
            return newID
