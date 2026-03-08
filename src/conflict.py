# CONFLICT DETECTION ALGORITHM
# COMPLEXITY: O(n log n) - SORTS FIRST, THEN SINGLE PASS COMPARISON

import sorting
import benchmark

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
    # DEFINE DATA FROM EVENT LIST AS .list_all
    data = events.list_all()

    # EMPTY LIST OF CONFLICT LISTS
    conflict = []

    # NUMBER OF EVENTS
    n = len(data)

    # ITERATE THROUGH EVENTS, COMPARE LOCATION THEN DATE THEN TIME
    for i in range(n):
        for j in range(i + 1, n):
            if data[i].location == data[j].location:
                if data[i].date == data[j].date:
                    if data[i].time == data[j].time:
                        conflict.append([data[i], data[j]])

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
    # BRING IN EVENTS  WITH LIST_ALL METHOD
    data = events.list_all()
    # SORT BY DATE THEN TIME THEN LOCATION (sortKey) SO CONFLICTS ARE ADJACENT
    sorted_events = sort_func(data, key = lambda e: e.sortKey())

    # EMPTY LIST READY FOR ADDING CONFLICT PAIRS
    conflicts = []
    # ITERATE THROUGH SORTED LIST COMPARING ADJACENT EVENTS FOR CONFLICTS
    for i in range(len(sorted_events)-1):
        curr = sorted_events[i]
        next = sorted_events[i+1]
        if curr.sortKey() == next.sortKey():
            conflicts.append((curr, next))
    return conflicts
                            
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
    if sort_func == None:
        return conflict_naive(events)
    else:
        return conflict_optimized(events, sort_func)

# Mike here -- I replaced this with a global function that can accept sorting functions
# or brute force conflict detection. see above.
# def conflict(events):
#     """
#     CHECKS IF ANY TWO EVENTS OVERLAP ON THE SAME DATE/TIME/LOCATION
#     ASSUMES EVENTS WITH SAME DATE/TIME/LOCATION = CONFLICT
#     PARAMS:
#         events - LIST OF EVENT OBJECTS
#     RETURNS:
#         conflicts - LIST OF CONFLICTING EVENT PAIRS
#     """
#     # SORT BY DATE THEN TIME THEN LOCATION (sortKey) SO CONFLICTS ARE ADJACENT
#     sorted_events = sorting.insertSort(events[:], key=lambda e: e.sortKey())

#     # EMPTY LIST READY FOR ADDING CONFLICT PAIRS
#     conflicts = []  
#     i = 0
#     # ITERATE THROUGH SORTED LIST COMPARING ADJACENT EVENTS FOR CONFLICTS
#     while i < len(sorted_events) - 1:
#         curr = sorted_events[i]
#         next = sorted_events[i + 1]
#         # CONFLICT IF SAME DATE, SAME TIME, AND SAME LOCATION
#         if curr.date == next.date and curr.time == next.time and curr.location == next.location:
#             conflicts.append((curr, next))
#         i += 1

#     return conflicts


# ─────────────────────────────────────────────────────
# QUICK SMOKE TEST
# ─────────────────────────────────────────────────────
if __name__ == "__main__":
    import sorting
    from randEvent import genEvents
    from sample_array import friday
    from dynamic_array import DynamicArrayEvent
    from event_creator import Event

    # EMPTY DYNAMIC ARRAY FOR SMOKE TEST
    mock_sched = DynamicArrayEvent()

    # USING EXISTING 'FRIDAY' EVENTS
    for e in friday:
        mock_sched.append(e)
        
    # MANUALLY CREATE A CONFLICT AND APPEND TO MOCK SCHEDULE
    conflict_1 = Event("Rap Battle team tryouts", "2026-11-25", "09:00", "Folsom Field")
    conflict_2 = Event("Rival Football Game", "2026-11-25", "09:00", "Folsom Field")
    mock_sched.append(conflict_1)
    mock_sched.append(conflict_2)

    # RUN CONFLICT DETECTION
    print("Checking mock schedule total events for conflicts")
    total = mock_sched.list_all()
    conflicts = conflict_optimized(mock_sched, sorting.mergeSort)

    # DISPLAY CONFLICTS AND TOTAL LIST
    print(mock_sched.list_all())
    print(f"found {len(conflicts)} conflicts:")
    for e1, e2 in conflicts:
        print(f" {e1.title} conflicts with {e2.title} at {e1.location}, {e1.date}, {e1.time}")