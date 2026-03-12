# IMPORT Event CLASS SO WE CAN MANUALLY CREATE EVENT OBJECTS
from event_creator import Event

# MANUALLY CREATED EVENT OBJECTS USED FOR SIMPLE TESTING
# THESE EVENTS ALL OCCUR ON THE SAME DAY BUT AT DIFFERENT TIME AND LOCATIONS
# PROVIDES A SMALL, PREDICTABLE DATASET FOR DEBUGGING AND FUNCTION TESTS
brunch = Event( "Brunch Buddies", "2026-03-06", "09:00", "C4C", id = 0)
lunch = Event("Lunch & Learn", "2026-03-06", "11:30", "UMC", id = 1)
hhour = Event("Bites & Beers", "2026-03-06", "16:30", "Avery", id = 2)
play = Event("Play & Pals", "2026-03-06", "18:30", "Mary Rippon Outdoor Theatre", id = 3)
stars = Event("Stars & Stares", "2026-03-06", "22:00", "Flagstaff", id = 4)

# GROUP ALL TEST EVENTS INTO A SIMPLY PYTHON LIST
# THIS LIST REPRESENTS A SINGLE DAY OF SCHEDULED EVENTS AND CAN BE USED
# FOR TESTING SORTING, SEARCHING, AND CONFLICT DETECTION FUNCTIONS
friday = [brunch, lunch, hhour, play, stars]

