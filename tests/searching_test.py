# TESTING FOR THE SEARCHING ALGORITHMS

from searching import linear, binary
from sorting import quickSort
from linked_list import EventLinkedList
import sample_array
import pytest


# FIXTURES
@pytest.fixture
def sortedFriday():
    # RETURNS COPY OF friday LIST SORTED BY id (FOR BINARY SEARCH)
    return quickSort(list(sample_array.friday), key=lambda e: e.id)

@pytest.fixture
def unsortedFriday():
    # RETURNS COPY OF friday LIST AS-IS (INSERTED IN id ORDER)
    return list(sample_array.friday)

@pytest.fixture
def sortedLinkedList():
    # RETURNS LINKED LIST WITH friday EVENTS SORTED BY id
    ll = EventLinkedList()
    for event in quickSort(list(sample_array.friday), key=lambda e: e.id):
        ll.append(event)
    return ll

@pytest.fixture
def unsortedLinkedList():
    # RETURNS LINKED LIST WITH friday EVENTS IN DEFAULT ORDER
    ll = EventLinkedList()
    for event in sample_array.friday:
        ll.append(event)
    return ll



# LINEAR SEARCH — ARRAY
def findEventTest_lin_arr(unsortedFriday):
    # TEST IF LINEAR SEARCH RETURNS CORRECT INDEX FOR KNOWN EVENT id
    target = sample_array.hhour.id
    index, iters = linear(target, unsortedFriday)
    assert index == unsortedFriday.index(sample_array.hhour)

def notFoundTest_lin_arr(unsortedFriday):
    # TEST IF RETURNS -1 WHEN TARGET id NOT FOUND
    index, iters = linear(999999999, unsortedFriday)
    assert index == -1

def iterationTest_lin_arr(unsortedFriday):
    # TEST IF LINEAR SEARCH ITERATIONS SHOULD BE BETWEEN 1 AND N
    target = sample_array.stars.id  # WORST CASE: LAST ELEMENT
    index, iters = linear(target, unsortedFriday)
    assert 1 <= iters <= len(unsortedFriday)

def firstElemTest_lin_arr(unsortedFriday):
    # TEST IF LINEAR FINDS FIRST ELEMENT IN ONE ITERATION (AS IS EXPECTED)
    target = unsortedFriday[0].id
    index, iters = linear(target, unsortedFriday)
    assert index == 0
    assert iters == 1



# LINEAR SEARCH — LINKED LIST INPUT
def converterTest_lin_ll(unsortedLinkedList):
    # TEST IF LINEAR WORKS WHEN PASSED A LINKED LIST (CONVERSION)
    target = sample_array.hhour.id
    index, iters = linear(target, unsortedLinkedList)
    assert index != -1

def notFoundTest_lin_ll(unsortedLinkedList):
    # TEST IF LINEAR RETURNS -1 ON LINKED LIST WHEN TARGET NOT FOUND
    index, iters = linear(999999999, unsortedLinkedList)
    assert index == -1



# BINARY SEARCH — ARRAY
def findEventTest_bin_arr(sortedFriday):
    # TEST IF BINARY RETURNS CORRECT INDEX FOR KNOWN EVENT id
    target = sample_array.hhour.id
    index, iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert sortedFriday[index].id == target

def notFoundTest_bin_arr(sortedFriday):
    # TEST IF BINARY RETURNS -1 IF TARGET id NOT FOUND IN LIST
    index, iters = binary(999999999, sortedFriday, key=lambda e: e.id)
    assert index == -1

def iterationsTest_bin_arr(sortedFriday):
    # BINARY SHOULD HAVE FEWER ITERATIONS THAN LINEAR SEARCH
    target = sortedFriday[-1].id  # WORST CASE (FOR LINEAR): LAST ELEMENT
    _, linear_iters = __import__('searching').linear(target, sortedFriday)
    _, binary_iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert binary_iters <= linear_iters

def firstElemTest_bin_arr(sortedFriday):
    # TEST IF BINARY FINDS FIRST ELEMENT IN SORTED LIST
    target = sortedFriday[0].id
    index, iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert sortedFriday[index].id == target

def lastElemTest_bin_arr(sortedFriday):
    # TEST IF BINARY FINDS LAST ELEMENT IN SORTED LIST
    target = sortedFriday[-1].id
    index, iters = binary(target, sortedFriday, key=lambda e: e.id)
    assert sortedFriday[index].id == target

def customTest_bin_arr(sortedFriday):
    # TEST IF BINARY WORKS CORRECTLY WITH A CUSTOM KEY
    date_sorted = quickSort(list(sample_array.friday), key=lambda e: e.date)
    target_date = "2026-03-06"
    index, iters = binary(target_date, date_sorted, key=lambda e: e.date)
    # ANY MATCH ACCEPTABLE SINCE ALL EVENTS SHARE SAME DATE
    assert index != -1
    assert date_sorted[index].date == target_date



# BINARY SEARCH — LINKED LIST INPUT
def converterTest_bin_ll(sortedLinkedList):
    # TEST IF BINARY WORKS WHEN PASSED LINKED LIST (CONVERSION)
    target = sample_array.hhour.id
    index, iters = binary(target, sortedLinkedList, key=lambda e: e.id)
    assert index != -1

def notFoundTest_bin_ll(sortedLinkedList):
    # TEST IF BINARY RETURNS -1 ON LINKED LIST WHEN TARGET NOT FOUND
    index, iters = binary(999999999, sortedLinkedList, key=lambda e: e.id)
    assert index == -1
