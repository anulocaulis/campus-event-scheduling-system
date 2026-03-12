# SORTING ALGORITHMS: INSERTION, MERGE, QUICK

# IMPORT random MODULE FOR RANDOMIZED PIVOT SELECTION IN quickSort()
import random

# INSERTION SORT FOR ARRAY IMPLEMENTATION
def insertSort(myArray, key=None):
    # STORE LENGTH OF ARRAY FOR LOOP CONTROL
    n = len(myArray)
    # IF NO KEY FUNCTION PROVIDED, DEFAULT TO Event.sortKey()
    # THIS ALLOWS EVENTS TO BE SORTED BY (date, time, location)
    if key is None: key = lambda e: e.sortKey()
    # LOOP THROUGH ARRAY STARTING AT INDEX 1
    # INDEX 0 IS TRIVIALLY SORTED BECAUSE A SINGLE ELEMENT IS ALWAYS SORTED
    for i in range(1, n):
        # STORE CURRENT VALUE BEING INSERTED INTO THE SORTED PORTION
        curr = myArray[i]
        # j POINTS TO ELEMENT DIRECTLY LEFT OF i
        j = i - 1
        # MOVE LEFTWARD THROUGH THE SORTED SECTION WHILE ELEMENTS ARE GREATER THAN curr
        # THIS SHIFTS LARGER ELEMENTS ONE POSITION TO THE RIGHT
        while j >= 0 and key(myArray[j]) > key(curr):
            # SHIFT ELEMENT RIGHTWARD TO MAKE SPACE
            myArray[j + 1] = myArray[j]
            # MOVE COMPARISON INDEX ONE POSITION LEFT
            j = j - 1
        # INSERT curr INTO ITS CORRECT SORTED POSITION
        myArray[j + 1] = curr
    # RETURN SORTED ARRAY
    return myArray

# MERGE SORT FOR ARRAY IMPLEMENTATION
def mergeSort(myArray, key=None):
    # IF NO KEY FUNCTION PROVIDED, DEFAULT TO Event.sortKey()
    if key is None: key = lambda e: e.sortKey()
    # STORE LENGTH OF ARRAY
    n = len(myArray)
    # BASE CASE: ARRAYS OF SIZE 0 OR 1 ARE ALREADY SORTED
    if n <= 1:
        return myArray
    else:
        # SPLIT ARRAY INTO TWO HALVES
        left = myArray[0:n//2]
        right = myArray[n//2:n]
        # RECURSIVELY SORT BOTH HALVES
        L_sort = mergeSort(left, key=key)
        R_sort = mergeSort(right, key=key)
    # CREATE EMPTY LIST THAT WILL STORE MERGED RESULT
    s = []
    # POINTER FOR LEFT SORTED LIST
    i = 0
    # POINTER FOR RIGHT SORTED LIST
    j = 0
    # MERGE BOTH SORTED HALVES WHILE BOTH HAVE REMAINING ELEMENTS
    while i < len(L_sort) and j < len(R_sort):
        # COMPARE CURRENT ELEMENTS FROM BOTH LISTS
        if key(L_sort[i]) <= key(R_sort[j]):
            # APPEND SMALLER ELEMENT FROM LEFT LIST
            s.append(L_sort[i])
            # MOVE LEFT POINTER FORWARD
            i += 1
        else:
            # APPEND SMALLER ELEMENT FROM RIGHT LIST
            s.append(R_sort[j])
            # MOVE RIGHT POINTER FORWARD
            j += 1
    # IF RIGHT LIST STILL HAS ELEMENTS REMAINING, APPEND THEM
    while j < len(R_sort):
        s.append(R_sort[j])
        j += 1
    # IF LEFT LIST STILL HAS ELEMENTS REMAINING, APPEND THEM
    while i < len(L_sort):
        s.append(L_sort[i])
        i += 1
    # RETURN FULLY MERGED AND SORTED LIST
    return s            

# QUICKSORT FOR ARRAY IMPLEMENTATION
def quickSort(myArray, key=None):
    # IF NO KEY FUNCTION PROVIDED, DEFAULT TO Event.sortKey()
    if key is None: key = lambda e: e.sortKey()
    # STORE LENGTH OF ARRAY
    n = len(myArray)
    # BASE CASE: ARRAYS OF SIZE 0 OR 1 ARE ALREADY SORTED
    if n <= 1:
        return myArray
    else:
        # SELECT RANDOM ELEMENT FROM ARRAY AS PIVOT
        # RANDOMIZED PIVOTS HELP REDUCE WORST-CASE SCENARIOS
        pivot = random.choice(myArray)
        # LIST FOR ELEMENTS SMALLER THAN PIVOT
        less = []
        # LIST FOR ELEMENTS EQUAL TO PIVOT
        equal = []
        # LIST FOR ELEMENTS GREATER THAN PIVOT
        more = []
        # PARTITION ORIGINAL ARRAY INTO THREE GROUPS
        for i in myArray:
            # IF ELEMENT IS LESS THAN PIVOT, ADD TO less
            if key(i) < key(pivot):
                less.append(i)
            # IF ELEMENT EQUALS PIVOT VALUE, ADD TO equal
            elif key(i) == key(pivot):
                equal.append(i)
            # OTHERWISE ELEMENT IS GREATER THAN PIVOT
            else:
                more.append(i)
        # RECURSIVELY SORT BOTH PARTITIONS
        sortLess = quickSort(less, key=key)
        sortMore = quickSort(more, key=key)
    # CONCATENATE SORTED PARTITIONS AND PIVOT VALUES
    s = sortLess + equal + sortMore
    # RETURN FULLY SORTED LIST
    return s
