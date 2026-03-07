# SORTING ALGORITHMS: INSERTION, MERGE, QUICK

# INSERTION SORT FOR ARRAY IMPLEMENTATION
def insertSort(myArray, key=None):
    n = len(myArray)         # ASSIGN n AS len(myArray) FOR EASE OF USE
  
    # IF EVENT DOESN'T ALREADY HAVE A SORT KEY, THIS GIVES IT ONE
    if key is None: key = lambda e: e.sortKey()

    # ITERATES THROUGH WHOLE LIST STARTING AT IDX 1, SINCE IDX 0 SORTED
    for i in range(1, n):    # I FIRST HAD IT AS n-1, LEAVING LAST ELEM UNSORTED
        curr = myArray[i]    # STORE CURR VALUE AS curr FOR SHIFTING
        j = i - 1            # COMPARE curr TO LIST ELEMS TO LEFT OF IT

        # PREVENTS j FROM GOING OUT OF BOUNDS LEFT
        while j >= 0 and key(myArray[j]) > key(curr): # INSURE ELEM GOES TO RIGHT OF curr
            myArray[j + 1] = myArray[j]  # SHIFT EVERYTHING OVER TO THE RIGHT
            j = j - 1           # MOVING RIGHT TO LEFT INSTEAD OF LEFT TO RIGHT

        myArray[j + 1] = curr   # USE j + 1 SINCE j POINTING TO ELEM < curr

    return myArray

# MERGE SORT FOR ARRAY IMPLEMENTATION
def mergeSort(myArray, key=None):
    # IF EVENT DOESN'T ALREADY HAVE A SORT KEY, THIS GIVES IT ONE
    if key is None: key = lambda e: e.sortKey()
    
    n = len(myArray)                    # ASSIGN n AS len(myArray) FOR EASE
    if n <= 1:
        return myArray                  # BASE CASE len(myArray) <= 1
    else:
        left = myArray[0:n//2]          # left LIST IS FIRST HALF OF myArray
        right = myArray[n//2:n]         # right LIST IS SECOND HALF OF myArray

        L_sort = mergeSort(left)        # RECURSIVE CALL TO SPLIT left FURTHER
        R_sort = mergeSort(right)       # RECURSIVE CALL TO SPLIT right FURTHER

    s = []                              # EMPTY LIST TO STORE FINAL RESULT
    i = 0                               # COUNTER FOR L_sort
    j = 0                               # COUNTER FOR R_sort

    # BOTH LEFT AND RIGHT LISTS STILL HAVE ELEMENTS
    while i < len(L_sort) and j < len(R_sort):
        # COMPARE THE TWO VALUES
        if key(L_sort[i]) <= key(R_sort[j]):      # VAL FROM LEFT < VAL FROM RIGHT
            s.append(L_sort[i])         # APPEND LEFT VAL TO sorted
            i += 1                      # INCREMENT COUNTER FOR LEFT LIST
        else:                           # VAL FROM RIGHT < VAL FROM LEFT
            s.append(R_sort[j])         # APPEND RIGHT VAL TO sorted
            j += 1                      # INCREMENT COUNTER FOR RIGHT LIST

    # LEFT LIST EMPTY, RIGHT LIST HAS REMAINING (SORTED) ELEMENTS
    while j < len(R_sort):              # ITERATE THROUGH REMAINING ELEMENTS
        s.append(R_sort[j])             # APPEND EACH ELEMENT TO sorted
        j += 1                          # INCREMENT j COUNTER

    # RIGHT LIST EMPTY, LEFT LIST HAS REMAINING (SORTED) ELEMENTS
    while i < len(L_sort):              # ITERATE THROUGH REMAINING ELEMENTS
        s.append(L_sort[i])             # APPEND EACH ELEMENT TO sorted
        i += 1                          # INCREMENT i COUNTER

    return s                            # RETURN SORTED LIST

# QUICKSORT FOR ARRAY IMPLEMENTATION
def quickSort(myArray, key =None):
    # IF EVENT DOESN'T ALREADY HAVE A SORT KEY, THIS GIVES IT ONE
    if key is None: key = lambda e: e.sortKey()
    
    n = len(myArray)                  # ASSIGN n AS len(myArray) FOR EASE OF USE
    if n <= 1:                          # BASE CASE RETURNS myArray
        return myArray
    else:
        pivot = myArray[0]               # PICK PIVOT: FIRST ELEMENT IN myArray
        less = []                        # CREATE EMPTY LIST FOR VALS < pivot
        equal = [pivot]                  # CREATE EMPTY LIST FOR VALS = pivot
        more = []                        # CREATE EMPTY LIST FOR VALS > pivot
        for i in range(1, n):            # CAN EXCLUDE PIVOT IN RANGE
            if key(myArray[i]) < key(pivot):       # COMPARE myArray[i] TO pivot
                less.append(myArray[i])  # IF myArray[i] < pivot, APPEND TO less
            elif key(myArray[i]) == key(pivot):
                equal.append(myArray[i]) #IF myArray[i] = pivot, APPEND TO equal
            else:
                more.append(myArray[i])  # IF myArray[i] > pivot, APPEND TO more
        sortLess = quickSort(less) # RECURSIVE CALL TO SORT less
        sortMore = quickSort(more) # RECURSIVE CALL TO SORT more

    s = sortLess + equal + sortMore    # CONCATENATE THREE (3) SUBLISTS TOGETHER
    return s
