# FUNCTION FOR CREATION OF RANDOM EVENTS
"""
WHY THIS EXISTS:
    WE NEED TO TEST AT n = 50, 500, 5000, 50000 TO SEE MEANINGFUL CURVES
    THIS GENERATOR PRODUCES RANDOM, UNSORTED EVENTS SO OUR SORTING BENCHMARKS 
    REFLECT REAL WORLD "MESSY" INPUT CONDITIONS, NOT BEST CASE SCENARIOS
    
"""

import random
from event_creator import Event

# COMMON TITLES FOR DIFFERENT TYPES OF EVENTS THAT GENERATOR CAN RANDOMLY PULL FROM
titles = [
    "Club Meeting", "Guest Lecture", "Hackathon", "Concert", "Exam Review",
    "Career Fair", "Art Show", "Movie Night", "Study Hall", "Workshop",
    "Orientation", "Panel Discussion", "Fitness Class", "Game Night", "Seminar",
    "Research Symposium", "Open Mic", "Networking Event", "Fundraiser", "Sports Game"
]

# COMMON EVENT LOCATIONS AROUND CU BOULDER CAMPUS THAT GENERATOR CAN RANDOMLY PULL FROM
locations = [
    "UMC", "C4C", "Norlin Library", "CASE", "ATLAS", "Rec Center",
    "Macky Auditorium", "Fleming Law", "Muenzinger", "Duane Physics",
    "Ekeley", "Ketchum Arts", "Wolf Law", "Engineering Center", "Folsom Field"
]

# FUNCTION TO CREATE A SINGLE EVENT
def createEvent():
    """
    CREATES A SINGLE RANDOM EVENT.
    DATE FORMAT:  YYYY-MM-DD  
    TIME FORMAT:  HH:MM       
    RANDOM DATE:
        - YEAR ALWAYS 2026 
        - MONTH IS 1-12
        - DAY IS 1-28 TO AVOID FEB 30, APRIL 31, ETC.
    RANDOM TIME:
        - HOUR: 0-23 (24 HOUR CLOCK) 
                REALISTICALLY, MOST EVENTS WILL FALL BETWEEN 0800-1800
                BUT THERE MIGHT BE SOME OVERNIGHT CLEANING OR STARGAZING EVENT
                THAT COULD RUN AFTER HOURS, SO WE KEEP THE FULL 0-23 
        - MINUTE: 00, 15, 30, or 45
    """
    year  = 2026
    month = random.randint(1, 12)
    day   = random.randint(1, 28)
    hour  = random.randint(0, 23)
    minute = random.choice([0, 15, 30, 45])

    # zfill(2) PADS OUR SINGLE DIGIT TIMES WITH A LEADING ZERO: 3 = "03", 11 = "11"
    # ENSURES FORMAT ALWAYS YYYY-MM-DD and HH:MM, SINCE SORT COMPARES DATES AS STRINGS
    # ONLY WORKS CORRECTLY IF FORMAT IS ZERO-PADDED
    date = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    time = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"

    title    = random.choice(titles)
    location = random.choice(locations)

    # ID is auto-assigned by event_creator.unique_ID()
    return Event(title, date, time, location)


# FUNCTION TO CREATE A LIST OF n RANDOM EVENTS
def genEvents(n):
    """
    CREATES lIST OF n RANDOM, UNSORTED EVENT OBJECTS
    PARAMS:
        n - NUMBER OF EVENTS TO GENERATE
    RETURNS:
        events - LIST OF n EVENT OBJECTS
        
    """
    events = []
    for i in range(n):    
        events.append(createEvent())
    return events



# ─────────────────────────────────────────────────────
# QUICK SMOKE TEST - WHEN RUN THIS FILE DIRECTLY, THIS BLOCK EXECUTES
# WHEN IMPORTED BY ANOTHER FILE, THIS BLOCK SKIPPED
# THAT'S WHAT "if __name__ == '__main__'" DOES.
# ─────────────────────────────────────────────────────

if __name__ == "__main__":
    sample = genEvents(5)
    print("Sample of 5 randomly generated events:")
    for e in sample:
        print(" ", e)
