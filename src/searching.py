# LINEAR AND BINARY SEARCH ALGORITHMS

# LINEAR SEARCH FOR ARRAY IMPLEMENTATION
'''
LINEAR SEARCH ALGORITHM: Complexity = O(n)
    PARAMS:
        target - INTEGER THE USER WANTS TO SEARCH FOR
        range  - RANGE OF SORTED NUMBERS TO SEARCH THROUGH
    RETURNS:
        i      - INDEX WHERE TARGET FOUND
        OR
        -1     - IF TARGET NOT FOUND
        AND
        iter - NUMBER OF LOOP ITERATIONS
'''
def linear(target, events):
    # IMPORT converter() TO ALLOW LINKED LISTS TO BE TRANSFORMED INTO ARRAYS
    from converter import converter  # IMPORTING CONVERTER METHOD
    # IMPORT EventLinkedList CLASS SO WE CAN CHECK INPUT TYPE
    from linked_list import EventLinkedList # IMPORTING EventLinkedList

    # IF INPUT IS ACTUALLY A LINKED LIST, CONVERT IT TO A STANDARD ARRAY
    # THIS ALLOWS THE SEARCH ALGORITHM TO WORK UNIFORMLY ON BOTH DATA STRUCTURES
    if isinstance(events, EventLinkedList):  # CHECKING TO SEE IF THE ARRAY IS ACTUALLY A LINKED LIST
        events = converter(events)
    
    # INITIALIZE ITERATION COUNTER TO TRACK HOW MANY ELEMENTS ARE CHECKED
    iter = 0
    # LOOP THROUGH events USING enumerate() TO TRACK BOTH INDEX AND VALUE
    for i, val in enumerate(events):  # USING enumerate() TO TRACK INDEX & VALUE
        # INCREMENT ITERATION COUNTER EACH TIME A NEW ELEMENT IS EXAMINED
        iter += 1
        # CHECK WHETHER CURRENT EVENT id MATCHES target VALUE
        if val.id == target:            # TARGET NUMBER FOUND IN GIVEN LIST/ARRAY
            # PRINT DEBUG INFORMATION SHOWING HOW MANY SEARCH STEPS WERE REQUIRED
            print(f"After {iter} 'guesses', target number ({target}) found at index {i}.")       
            # RETURN THE INDEX WHERE TARGET WAS FOUND AND NUMBER OF ITERATIONS
            return i, iter

    # EXECUTED IF LOOP FINISHES WITHOUT FINDING TARGET
    # PRINT MESSAGE INDICATING TARGET WAS NOT FOUND
    print(f"After {iter} 'guesses', target number ({target}) NOT found in the given range.")

    # RETURN -1 TO INDICATE FAILURE AND PROVIDE ITERATION COUNT
    return -1, iter

# BINARY SEARCH FOR ARRAY IMPLEMENTATION
'''
BINARY SEARCH ALGORITHM: Complexity = O(log n)
    PARAMS:
        target - VALUE TO SEARCH FOR (MUST MATCH THE KEY TYPE)
        array  - LIST/LINKED LIST OF EVENT OBJECTS TO SEARCH THROUGH
        key    - FUNCTION THAT EXTRACTS THE SEARCH KEY FROM AN EVENT.
                 DEFAULTS TO lambda e: e.id (SEARCH BY ID).
                 *** ARRAY MUST BE PRE-SORTED BY THIS SAME KEY ***
    RETURNS:
        middle - INDEX WHERE TARGET IS FOUND
        OR
        -1     - IF TARGET NOT FOUND
        AND
        iter   - NUMBER OF LOOP ITERATIONS
    EXAMPLE USAGE:
        # SEARCH BY ID (MUST BE SORTED BY ID FIRST):
        id_sorted = quickSort(events, key=lambda e: e.id)
        binary(target_id, id_sorted)

        # SEARCH BY DATE (MUST BE SORTED BY DATE FIRST):
        date_sorted = quickSort(events, key=lambda e: e.date)
        binary("2026-03-06", date_sorted, key=lambda e: e.date)
'''
def binary(target, array, key=None):
    # IMPORT converter() TO SUPPORT SEARCHING LINKED LIST INPUTS
    from converter import converter  # IMPORTING CONVERTER METHOD
    # IMPORT LINKED LIST CLASS FOR TYPE CHECKING
    from linked_list import EventLinkedList # IMPORTING EventLinkedList

    # IF INPUT DATA STRUCTURE IS A LINKED LIST, CONVERT IT INTO A STANDARD ARRAY
    if isinstance(array, EventLinkedList):  # CHECKING TO SEE IF THE ARRAY IS ACTUALLY A LINKED LIST
        array = converter(array)
    # IF NO KEY FUNCTION IS PROVIDED, DEFAULT TO SEARCHING BY EVENT id
    if key is None: key = lambda e: e.id
    
    # INITIALIZE ITERATION COUNTER TO TRACK NUMBER OF BINARY SEARCH STEPS
    iter = 0
    # SET INITIAL LOWER BOUND OF SEARCH RANGE
    low = 0
    # SET INITIAL UPPER BOUND OF SEARCH RANGE
    high = len(array) - 1
    # CONTINUE SEARCH WHILE SEARCH WINDOW IS VALID
    while low <= high:
        # COUNT EACH ITERATION OF THE BINARY SEARCH LOOP
        iter += 1
        # CALCULATE MIDDLE INDEX OF CURRENT SEARCH RANGE
        middle = (low + high) // 2
        # EXTRACT VALUE AT middle USING PROVIDED KEY FUNCTION
        m_val = key(array[middle])
        # CHECK IF MIDDLE VALUE MATCHES TARGET
        if m_val == target:
            # PRINT DEBUG INFORMATION SHOWING NUMBER OF SEARCH STEPS
            print(f"After {iter} 'guesses', target number ({target}) found at index {middle}.")
            # RETURN INDEX WHERE TARGET FOUND AND NUMBER OF ITERATIONS
            return middle, iter
        # IF TARGET IS GREATER THAN MIDDLE VALUE, SEARCH RIGHT HALF
        elif m_val < target:
            low = middle + 1
        # OTHERWISE TARGET IS SMALLER, SEARCH LEFT HALF
        else:
            high = middle - 1

    # EXECUTED IF SEARCH RANGE COLLAPSES WITHOUT FINDING TARGET
    print(f"After {iter} 'guesses', target number ({target}) NOT found in the given range.")
    # RETURN -1 TO INDICATE FAILURE AND RETURN ITERATION COUNT
    return -1, iter

