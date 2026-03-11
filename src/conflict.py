# CONFLICT DETECTION ALGORITHM
# COMPLEXITY: O(n log n) - SORTS FIRST, THEN SINGLE PASS COMPARISON

import sorting
from event_creator import Event

# NAIVE CONFLICT DETECTION IMPLEMENTATION
# COMPARES EVERY EVENT WITH EVERY OTHER EVENT TO FIND MATCHING LOCATION, DATE, AND TIME
# THIS IMPLEMENTATION DOES NOT SORT AND THEREFORE HAS O(n^2) TIME COMPLEXITY
def conflict_naive(events):
    """
    CHECKS IF EVENTS OVERLAP ON THE SAME LOCATION/DATE-TIME
    ASSUMES EVENTS WITH THE SAME LOCATION AND DATE-TIME ARE IN CONFLICT
    DOESN'T IMPLEMENT SORTING. TIME COMPLEXITY O(N^2)
    PARAMS:
        events - LIST OF EVENTS
    RETURNS:
        conflicts - LIST OF CONFLICTNG EVENT LISTS
    """
    
    # EXTRACT UNDERLYING EVENT DATA FROM THE CONTAINER USING list_all()
    # THIS RETURNS A STANDARD PYTHON LIST OF Event OBJECTS
    data = events.list_all()

    # INITIALIZE EMPTY LIST THAT WILL STORE PAIRS OF CONFLICTING EVENTS
    conflicts = []
        
    # STORE TOTAL NUMBER OF EVENTS FOR LOOP ITERATION
    n = len(data)

    # DOUBLE NESTED LOOP IMPLEMENTS BRUTE FORCE COMPARISON
    # EACH EVENT IS COMPARED AGAINST ALL EVENTS AFTER IT IN THE LIST
    for i in range(n):
        for j in range(i + 1, n):
            # FIRST CHECK SAME LOCATION
            if data[i].location == data[j].location:
                # THEN CHECK THE SAME DATE
                if data[i].date == data[j].date:
                    # FINALLY CHECK SAME TIME
                    # IF ALL THREE MATCH, THE EVENTS ARE CONSIDERED A CONFLICT
                    if data[i].time == data[j].time:
                        conflicts.append([data[i], data[j]])

    return conflicts

# OPTIMIZED CONFLICT DETECTION IMPLEMENTATION
# SORTS EVENTS FIRST SO POTENTIAL CONFLICTS APPEAR NEXT TO EACH OTHER
# THEN PERFORMS A SINGLE PASS COMPARING ONLY ADJACENT EVENTS
def conflict_optimized(events, sort_func):
    """
    OPTIMIZED CONFLICT CHECK. SORTS ACCORDING TO SORT FUNCTION ARG BEFORE
    EVALUATING CONFLICTS. CHECKS IF EVENTS OVERLAP ON THE SAME LOCATION
    OR DATE-TIME. ASSUMES EVENTS WITH THE SAME LOCATION AND DATE-TIME
    ARE IN CONFLICT. TIME COMPLEXITY INHERITED FROM SORT ALGORITHM.
    PARAMS:
        events - LIST OF EVENTS
        sort_func - SORTING FUNCTION IMPORTED FROM sorting.py TO SORT
            EVENTS BEFORE CHECKING FOR CONFLICTS
    RETURNS:
        conflicts - LIST OF CONFLICTNG EVENT LISTS
    """
    # EXTRACT EVENT DATA FROM THE CONTAINER STRUCTURE USING list_all()
    data = events.list_all()
    
    # SORT EVENTS USING HTE PROVIDED SORT FUNCTION
    # sortKey() RETURNS A COMPOSITE KEY (DATE, TIME, LOCATION) SO EVENTS
    # WITH IDENTICAL VALUES WILL BECOME ADJACENT AFTER SORTING
    sorted_events = sort_func(data, key = lambda e: e.sortKey())

    # INITIALIZE EMPTY LIST TO STORE CONFLICTING EVENT PAIRS
    conflicts = []
    
    # SINGLE PASS THROUGH THE SORTED LIST
    # ONLY COMPARE EACH EVENT WITH THE NEXT ONE BECAUSE CONFLICTS WILL NOW BE ADJACENT
    for i in range(len(sorted_events)-1):
        curr = sorted_events[i]
        next = sorted_events[i+1]
        
        # IF SORT KEY MATCHES, THE EVENTS SHARE THE SAME DATE, TIME, AND LOCATION
        # THEREFORE THEY ARE IN CONFLICT
        if curr.sortKey() == next.sortKey():
            conflicts.append((curr, next))
    return conflicts

# UNIFIED CONFLICT DETECTION INTERFACE
# THIS FUNCTION ACTS AS A CONTROLLER THAT DECIDES WHICH CONFLICT ALGORITHM TO RUN
# IF sort_func IS PROVIDED IT RUNS THE OPTIMIZED VERSION, OTHERWISE IT USES THE NAIVE VERSION
def conflict(events, sort_func=None):
    """
    UNIFIED CONFLICT DETECTION. IF A SORTING FUNCTION IS PROVIDED,
    USES THE OPTIMIZED CONFLICT FUNCTION. OTHERWISE, USES A NAIVE
    CONFLICT DETECTION.
    PARAMS:
        events - LIST OF EVENT OBJECTS
        sort_func - SORTING FUNCTION IMPORTED FROM sorting.py TO SORT
            EVENTS BEFORE CHECKING FOR CONFLICTS
    RETURNS:
        conflicts - LIST OF CONFLICTNG EVENT LISTS
    """
    # SELECT WHICH CONFLICT DETECTION STRATEGY TO USE
    if sort_func == None:
        return conflict_naive(events)
    else:
        return conflict_optimized(events, sort_func)



# QUICK SMOKE TEST
# THIS SECTION RUNS A SIMPLE TEST WHEN THE FILE IS EXECUTED DIRECTLY
# IT BUILDS A MOCK SCHEDULE, ADDS TWO INTENTIONAL CONFLICTING EVENTS,
# AND RUNS THE OPTIMIZED CONFLICT DETECTION TO VERIFY CORRECT BEHAVIOR
if __name__ == "__main__":
    import sorting
    from randEvent import genEvents
    from sample_array import friday
    from dynamic_array import DynamicArrayEvent
    from event_creator import Event

    # CREATE EMPTY DynamicArrayEvent STRUCTURE FOR TESTING
    mock_sched = DynamicArrayEvent()

    # LOAD PREDEFINED 'friday' EVENTS INTO THE MOCK SCHEDULE
    for e in friday:
        mock_sched.append(e)
        
    # MANUALLY CREATE TWO EVENTS THAT SHARE THE SAME LOCATION, DATE, AND TIME
    # THESE ARE INTENTIONAL CONFLICTS USED TO VERIFY THE ALGORITHM
    conflict_1 = Event("Rap Battle team tryouts", "2026-11-25", "09:00", "Folsom Field")
    conflict_2 = Event("Rival Football Game", "2026-11-25", "09:00", "Folsom Field")
    mock_sched.append(conflict_1)
    mock_sched.append(conflict_2)

    # RUN OPTIMIZED CONFLICT DETECTION USING mergeSort AS THE SORTING ALGORITHM
    print("Checking mock schedule total events for conflicts")
    total = mock_sched.list_all()
    conflicts = conflict_optimized(mock_sched, sorting.mergeSort)

    # DISPLAY FULL EVENT LIST AND ANY DETECTED CONFLICT PAIRS
    print(mock_sched.list_all())
    print(f"found {len(conflicts)} conflicts:")
    for e1, e2 in conflicts:
        print(f" {e1.title} conflicts with {e2.title} at {e1.location}, {e1.date}, {e1.time}")
