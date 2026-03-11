# TESTING FOR THE SEARCHING ALGORITHMS
# USING PYTEST TO VALIDATE LINEAR AND BINARY SEARCH ON ARRAYS AND LINKED LISTS
from searching import linear, binary
from sorting import quickSort
from linked_list import EventLinkedList
import sample_array
import pytest


# FIXTURES: SET UP PRECONFIGURED EVENT LISTS AND LINKED LISTS
@pytest.fixture
def sortedFriday():
    '''
    RETURNS COPY OF 'friday' LIST SORTED BY id
    USED FOR BINARY SEARCH SINCE BINARY REQUIRES SORTED INPUT
    '''
    return quickSort(list(sample_array.friday), key=lambda e: e.id)

@pytest.fixture
def unsortedFriday():
    '''
    RETURNS COPY OF 'friday' LIST IN ORIGINAL INSERTION ORDER
    USED FOR LINEAR SEARCH TESTING
    '''
    return list(sample_array.friday)

@pytest.fixture
def sortedLinkedList():
    '''
    RETURNS LINKED LIST VERSION OF 'friday' EVENTS SORTED BY id
    TO TEST SEARCH FUNCTIONS' ABILITY TO HANDLE LINKED LIST INPUT
    '''
    ll = EventLinkedList()
    for event in quickSort(list(sample_array.friday), key=lambda e: e.id):
        ll.append(event)
    return ll

@pytest.fixture
def unsortedLinkedList():
    '''
    RETURNS LINKED LIST VERSION OF 'friday' EVENTS IN DEFAULT ORDER
    USED TO TEST LINEAR SEARCH ON LINKED LIST INPUT
    '''
    ll = EventLinkedList()
    for event in sample_array.friday:
        ll.append(event)
    return ll



# LINEAR SEARCH — ARRAY INPUT TESTS
def test_findEvent_lin_arr(unsortedFriday):
    # TEST IF LINEAR SEARCH RETURNS CORRECT INDEX FOR KNOWN EVENT id
    target = sample_array.hhour.id
    index, iters = linear(target, unsortedFriday)
    assert index == unsortedFriday.index(sample_array.hhour)

def test_notFound_lin_arr(unsortedFriday):
    # TEST IF RETURNS -1 WHEN TARGET id NOT FOUND
    index, iters = linear(999999999, unsortedFriday)
    assert index == -1

def test_iteration_lin_arr(unsortedFriday):
    # TEST IF LINEAR SEARCH ITERATIONS SHOULD BE BETWEEN 1 AND N
    target = sample_array.stars.id  # WORST CASE: LAST ELEMENT
    index, iters = linear(target, unsortedFriday)
    assert 1 <= iters <= len(unsortedFriday)

def test_firstElem_lin_arr(unsortedFriday):
    # TEST IF LINEAR FINDS FIRST ELEMENT IN ONE ITERATION (AS IS EXPECTED)
    target = unsortedFriday[0].id
    index, iters = linear(target, unsortedFriday)
    assert index == 0
    assert iters == 1



# LINEAR SEARCH — LINKED LIST INPUT TESTS
# ENSURES LINKED LISTS ARE PROPERLY CONVERTED TO ARRAYS
def test_converter_lin_ll(unsortedLinkedList):
    # TEST IF LINEAR WORKS WHEN PASSED A LINKED LIST (CONVERSION)
    target = sample_array.hhour.id
    index, iters = linear(target, unsortedLinkedList)
    assert index != -1

def test_notFound_lin_ll(unsortedLinkedList):
    # TEST IF LINEAR RETURNS -1 ON LINKED LIST WHEN TARGET NOT FOUND
    index, iters = linear(999999999, unsortedLinkedList)
    assert index == -1



# BINARY SEARCH — ARRAY INPUT TESTS
def test_findEvent_bin_arr(sortedFriday):
    # TEST IF BINARY RETURNS CORRECT INDEX FOR KNOWN EVENT id
    target = sample_array.hhour.id
    index, iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert sortedFriday[index].id == target

def test_notFound_bin_arr(sortedFriday):
    # TEST IF BINARY RETURNS -1 IF TARGET id NOT FOUND IN LIST
    index, iters = binary(999999999, sortedFriday, key=lambda e: e.id)
    assert index == -1

def test_iterations_bin_arr(sortedFriday):
    # BINARY SHOULD HAVE FEWER ITERATIONS THAN LINEAR SEARCH
    target = sortedFriday[-1].id  # WORST CASE (FOR LINEAR): LAST ELEMENT
    _, linear_iters = __import__('searching').linear(target, sortedFriday)
    _, binary_iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert binary_iters <= linear_iters

def test_firstElem_bin_arr(sortedFriday):
    # TEST IF BINARY FINDS FIRST ELEMENT IN SORTED LIST
    target = sortedFriday[0].id
    index, iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert sortedFriday[index].id == target

def test_lastElem_bin_arr(sortedFriday):
    # TEST IF BINARY FINDS LAST ELEMENT IN SORTED LIST
    target = sortedFriday[-1].id
    index, iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert sortedFriday[index].id == target

def test_custom_bin_arr(sortedFriday):
    # TEST IF BINARY WORKS CORRECTLY WITH A CUSTOM KEY
    date_sorted = quickSort(list(sample_array.friday), key=lambda e: e.date)
    target_date = "2026-03-06"
    index, iters = binary(target_date, date_sorted, key=lambda e: e.date)
    # ANY MATCH ACCEPTABLE SINCE ALL EVENTS SHARE SAME DATE
    assert index != -1
    assert date_sorted[index].date == target_date



# BINARY SEARCH — LINKED LIST INPUT TESTS
# ENSURES LINKED LISTS ASRE PROPERLY CONVERTED TO ARRAYS
def test_converter_bin_ll(sortedLinkedList):
    # TEST IF BINARY WORKS WHEN PASSED LINKED LIST (CONVERSION)
    target = sample_array.hhour.id
    index, iters = binary(target, sortedLinkedList, key=lambda e: e.id)
    assert index != -1

def test_notFound_bin_ll(sortedLinkedList):
    # TEST IF BINARY RETURNS -1 ON LINKED LIST WHEN TARGET NOT FOUND
    index, iters = binary(999999999, sortedLinkedList, key=lambda e: e.id)
    assert index == -1
