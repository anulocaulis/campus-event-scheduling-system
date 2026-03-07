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
def linear(target, range):
    # IF INPUT IS LINKED LIST, CONVERT TO ARRAY FOR SORTING, THEN BINARY SEARCH
    from converter import converter  # IMPORTING CONVERTER METHOD
    from linked_list import EventLinkedList # IMPORTING EventLinkedList
    if isinstance(range, EventLinkedList):  # CHECKING TO SEE IF THE ARRAY IS ACTUALLY A LINKED LIST
        range = converter(range)
    
    iter = 0                   # COUNTER FOR NUMBER OF LOOP ITERATIONS
    for i, val in enumerate(range):  # USING enumerate() TO TRACK INDEX & VALUE
        iter += 1              # INCREMENT ITERATIONS COUNTER
        if val.id == target:            # TARGET NUMBER FOUND IN GIVEN LIST/RRAY
            print(f"After {iter} 'guesses', target number ({target}) found at index {i}.")       # PRINT STATEMENT FOR TRACKING/DEBUGGING
            return i, iter     # RETURN INDEX WHERE TARGET VALUE FOUND

    # TARGET NUMBER NOT FOUND IN GIVEN LIST/ARRAY
    print(f"After {iter} 'guesses', target number ({target}) NOT found in the given range.")
    return -1, iter            # RETURN -1 TO SHOW TARGET NUMBER NOT FOUND

# BINARY SEARCH FOR ARRAY IMPLEMENTATION
'''
BINARY SEARCH ALGORITHM - Complexity = O(logn)
    PARAMS:
        target - INTEGER THE USER WANTS TO SEARCH FOR
        range  - RANGE OF SORTED NUMBERS TO SEARCH THROUGH
    RETURNS:
        middle - INDEX WHERE TARGET IS FOUND
        OR
        -1 IF TARGET IS NOT FOUND
        AND
        iter - NUMBER OF LOOP ITERATIONS
'''
def binary(target, array):
    # IF INPUT IS LINKED LIST, CONVERT TO ARRAY FOR SORTING, THEN BINARY SEARCH
    from converter import converter  # IMPORTING CONVERTER METHOD
    from linked_list import EventLinkedList # IMPORTING EventLinkedList
    if isinstance(array, EventLinkedList):  # CHECKING TO SEE IF THE ARRAY IS ACTUALLY A LINKED LIST
        array = converter(array)
    
    iter = 0                   # COUNTER FOR NUMBER OF LOOP ITERATIONS        
    low = 0                    # LOW INDEX OF RANGE
    high = len(array) - 1      # HIGH INDEX OF RANGE
    while low <= high:         # MAIN WHILE LOOP: SEARCH UNTIL TARGET FOUND OR LIST ENDS
        iter += 1                     # INCREMENT ITERATIONS COUNTER
        middle = (low + high) // 2    # DIVIDING OUR SEARCH RANGE IN HALF
        if array[middle].id == target:   # TARGET NUMBER FOUND IN LIST
            print(f"After {iter} 'guesses', target number ({target}) found at index {middle}.")
            return middle, iter       # RETURN INDEX WHERE VALUE FOUND
        elif array[middle].id < target:         # TARGET VALUE GREATER THAN MIDDLE VALUE
            low = middle + 1          # SETS low TO INDEX JUST ABOVE MIDDLE
        else:                         # TARGET VALUE LESS THAN MIDDLE VALUE
            high = middle - 1         # SETS high TO INDEX JUST BELOW MIDDLE
    print(f"After {iter} 'guesses', target number ({target}) NOT found in the given range.")
    return -1, iter

