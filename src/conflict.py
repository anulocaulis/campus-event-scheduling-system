# CONFLICT DETECTION ALGORITHM
# COMPLEXITY: O(n log n) - SORTS FIRST, THEN SINGLE PASS COMPARISON

from sorting import insertSort

def conflict(events):
    """
    CHECKS IF ANY TWO EVENTS OVERLAP ON THE SAME DATE/TIME/LOCATION
    ASSUMES EVENTS WITH SAME DATE/TIME/LOCATION = CONFLICT
    PARAMS:
        events - LIST OF EVENT OBJECTS
    RETURNS:
        conflicts - LIST OF CONFLICTING EVENT PAIRS
    """
    # SORT BY DATE THEN TIME THEN LOCATION (sortKey) SO CONFLICTS ARE ADJACENT
    sorted_events = insertSort(events[:], key=lambda e: e.sortKey())

    # EMPTY LIST READY FOR ADDING CONFLICT PAIRS
    conflicts = []  
    i = 0
    # ITERATE THROUGH SORTED LIST COMPARING ADJACENT EVENTS FOR CONFLICTS
    while i < len(sorted_events) - 1:
        curr = sorted_events[i]
        next = sorted_events[i + 1]
        # CONFLICT IF SAME DATE, SAME TIME, AND SAME LOCATION
        if curr.date == next.date and curr.time == next.time and curr.location == next.location:
            conflicts.append((curr, next))
        i += 1

    return conflicts
