# TESTING FOR CONFLICT DETECTION ALGORITHMS
# USING PYTEST TO VALIDATE NAIVE, OPTIMIZED, AND UNIFIED CONFLICT FUNCTIONS
from conflict import conflict, conflict_naive, conflict_optimized
from sorting import insertSort, mergeSort, quickSort
from dynamic_array import DynamicArrayEvent
from event_creator import Event
import sample_array
import pytest


# FIXTURES: SET UP PRECONFIGURED DYNAMIC ARRAY EVENTS
@pytest.fixture
def noConflicts():
    '''
    DYNAMIC ARRAY EVENT LOADED WITH friday EVENTS. 
    ALL HAVE DISTINCT TIMES AND LOCATIONS (NO CONFLICTS)
    RETURNS:
        dyn_arr - DynamicArrayEvent INSTANCE
    '''
    dyn_arr = DynamicArrayEvent()
    for event in sample_array.friday:
        dyn_arr.append(event)
    return dyn_arr

@pytest.fixture
def withConflicts():
    '''
    DYNAMIC ARRAY EVENT WITH 2 EVENTS SHARING SAME DATE/TIME/LOCATION (CONFLICT)
    RETURNS:
        dyn_arr - DynamicArrayEvent INSTANCE WITH 1 CONFLICTING EVENT
    '''
    dyn_arr = DynamicArrayEvent()
    for event in sample_array.friday:
        dyn_arr.append(event)
    # MANUALLY INSERT/INJECT CONFLICTING EVENT
    conflict_event = Event("Yoga Class", "2026-03-06", "09:00", "C4C", id=99)
    dyn_arr.append(conflict_event)
    return dyn_arr

@pytest.fixture
def multipleConflicts():
    '''
    DYNAMIC ARRAY EVENT WITH MULTIPLE CONFLICTS (TWO PAIRS)
    RETURNS:
        dyn_arr - DynamicArrayEvent instance
    '''
    dyn_arr = DynamicArrayEvent()
    for event in sample_array.friday:
        dyn_arr.append(event)
    # PURPOSELY CONFLICT WITH brunch
    dyn_arr.append(Event("Yoga Class",    "2026-03-06", "09:00", "C4C",    id=98))
    # PURPOSELY CONFLICT WITH stars
    dyn_arr.append(Event("Meteor Watch",  "2026-03-06", "22:00", "Flagstaff", id=97))
    return dyn_arr

@pytest.fixture
def emptySchedule():
    '''
    RETURNS AN EMPTY DYNAMIC ARRAY (SHOULD HAVE ZERO CONFLICTS)
    '''
    return DynamicArrayEvent()


#================================================================================
# NAIVE CONFLICT DETECTION
def test_noConflicts_naive(noConflicts):
    # TEST IF NAIVE CONFLICT DETECTION RETURNS EMPTY LIST WHEN NO CONFLICTS
    result = conflict_naive(noConflicts)
    assert result == []

def test_oneConflict_naive(withConflicts):
    # TEST IF NAIVE CONFLICT DETECTION FINDS EXACTLY 1 CONFLICT PAIR
    result = conflict_naive(withConflicts)
    assert len(result) == 1

def test_multConflicts_naive(multipleConflicts):
    # TEST IF NAIVE CONFLICT DETECTION FINDS MULTIPLE CONFLICT PAIRS
    result = conflict_naive(multipleConflicts)
    assert len(result) == 2

def test_correctEvents_naive(withConflicts):
    # TEST IF NAIVE DETECTION RETURNS CORRECT EVENTS IN CONFLICT PAIR
    result = conflict_naive(withConflicts)
    ids_in_conflict = {e.id for pair in result for e in pair}
    # BRUNCH (id=0) AND INJECTED EVENT (id=99) SHOULD CONFLICT
    assert 0 in ids_in_conflict
    assert 99 in ids_in_conflict



# OPTIMIZED CONFLICT DETECTION (ALL 3 SORTING ALGORITHMS)
@pytest.mark.parametrize("sort_func", [insertSort, mergeSort, quickSort])
def test_noConflicts_optimized(noConflicts, sort_func):
    # TEST IF OPTIMIZED DETECTION RETURNS EMPTY LIST WHEN NO CONFLICTS
    result = conflict_optimized(noConflicts, sort_func)
    assert result == []

@pytest.mark.parametrize("sort_func", [insertSort, mergeSort, quickSort])
def test_oneConflict_optimized(withConflicts, sort_func):
    # TEST IF OPTIMIZED DETECTION FINDS ONE CONFLICT PAIR
    result = conflict_optimized(withConflicts, sort_func)
    assert len(result) == 1

@pytest.mark.parametrize("sort_func", [insertSort, mergeSort, quickSort])
def test_multiConflicts_optimized(multipleConflicts, sort_func):
    # TEST IF OPTIMIZED DETECTION FINDS MULTIPLE CONFLICT PAIRS
    result = conflict_optimized(multipleConflicts, sort_func)
    assert len(result) == 2

@pytest.mark.parametrize("sort_func", [insertSort, mergeSort, quickSort])
def test_correctEvents_optimized(withConflicts, sort_func):
    # TEST IF OPTIMIZED DETECTION RETURNS CORRECT EVENTS IN CONFLICT PAIR
    result = conflict_optimized(withConflicts, sort_func)
    ids_in_conflict = {e.id for pair in result for e in pair}
    assert 0 in ids_in_conflict
    assert 99 in ids_in_conflict



# UNIFIED conflict() DISPATCHER
# TESTS THAT IT SELECTS CORRECT DETECTION METHOD
def test_noSortFunc_useNaive(withConflicts):
    # TEST IF conflict() WITH NO sort_func DEFAULTS TO NAIVE DETECTION
    result = conflict(withConflicts)
    assert len(result) == 1

def test_withSortFunc_useOptimized(withConflicts):
    # TEST IF conflict() WITH sort_func USES OPTIMIZED PATH
    result = conflict(withConflicts, sort_func=mergeSort)
    assert len(result) == 1

def test_agreeTest(withConflicts):
    # TEST IF BOTH PATHS FIND SAME NUMBER OF CONFLICTS
    naive_result     = conflict(withConflicts)
    optimized_result = conflict(withConflicts, sort_func=mergeSort)
    assert len(naive_result) == len(optimized_result)

def test_emptyScheduleTest(emptySchedule):
    # TEST IF conflict() ON EMPTY SCHEDULE RETURNS NO CONFLICTS 
    assert conflict(emptySchedule) == []
    assert conflict(emptySchedule, sort_func=mergeSort) == []
