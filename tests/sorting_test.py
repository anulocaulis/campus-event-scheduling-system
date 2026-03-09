# TESTING FOR THE SORTING ALGORITHMS

from sorting import insertSort, mergeSort, quickSort
from event_creator import Event
import sample_array
import pytest

# FIXTURES
@pytest.fixture
def unsortedEvents():
    # RETURNS UNSORTED COPY OF friday LIST FOR EACH TEST
    return [
        sample_array.stars,   # 22:00
        sample_array.hhour,   # 16:30
        sample_array.brunch,  # 09:00
        sample_array.play,    # 18:30
        sample_array.lunch,   # 11:30
    ]

@pytest.fixture
def sortedOrder():
    # EXPECTED / CORRECT ORDER: DATE > TIME > LOCATION
    return [
        sample_array.brunch,  # 09:00
        sample_array.lunch,   # 11:30
        sample_array.hhour,   # 16:30
        sample_array.play,    # 18:30
        sample_array.stars,   # 22:00
    ]

@pytest.fixture
def singleEvent():
    # LIST WITH ONE EVENT. SHOULD BE SORTED WITHOUT ISSUE
    return [sample_array.brunch]

@pytest.fixture
def alreadySorted():
    # ALREADY SORTED. SORTING ALGS SHOULD NOT BREAK SORTED ORDER
    return list(sample_array.friday)  # friday ALREADY DEFINED IN SORTED ORDER


# INSERTION SORT TESTS
def basicTest_insertSort(unsortedEvents, sortedOrder):
    # TESTING IF insertSort CORRECTLY ORDERS EVENTS BY DATE > TIME > LOCATION
    result = insertSort(unsortedEvents)
    assert result == sortedOrder

def singleTest_insertSort(singleEvent):
    # TESTING IF insertSort HANDLES LIST WITH SINGLE EVENT
    result = insertSort(singleEvent)
    assert len(result) == 1
    assert result[0] == sample_array.brunch

def sortedTest_insertSort(alreadySorted, sortedOrder):
    # TESTING IF insertSort BREAKS/CORRUPTS A SORTED LIST
    result = insertSort(alreadySorted)
    assert result == sortedOrder

def customTest_insertSort(unsortedEvents):
    # TESTING IF insertSort CAN SORT BY CUSTOM KEY (SORTING BY TITLE ALPHABETICALLY)
    result = insertSort(unsortedEvents, key=lambda e: e.title)
    titles = [e.title for e in result]
    assert titles == sorted(titles)

def integrityTest_insertSort(unsortedEvents):
    # TESTING IF insertSort KEEPS DATA INTEGRITY (NO DELETED OR DUPLICATED EVENTS)
    result = insertSort(unsortedEvents)
    assert len(result) == len(unsortedEvents)
    assert set(e.id for e in result) == set(e.id for e in unsortedEvents)


# MERGE SORT TESTS
def basicTest_mergeSort(unsortedEvents, sortedOrder):
    # TESTING IF mergeSort CORRECTLY ORDERS EVENTS BY DATE > TIME > LOCATION
    result = mergeSort(unsortedEvents)
    assert result == sortedOrder

def singleTest_mergeSort(singleEvent):
    # TESTING IF mergeSort HANDLES LIST WITH SINGLE EVENT
    result = mergeSort(singleEvent)
    assert len(result) == 1
    assert result[0] == sample_array.brunch

def sortedTest_mergeSort(alreadySorted, sortedOrder):
    # TESTING IF mergeSort BREAKS/CORRUPTS A SORTED LIST
    result = mergeSort(alreadySorted)
    assert result == sortedOrder

def customTest_mergeSort(unsortedEvents):
    # TESTING IF mergeSort CAN SORT BY CUSTOM KEY (SORTING BY TITLE ALPHABETICALLY)
    result = mergeSort(unsortedEvents, key=lambda e: e.title)
    titles = [e.title for e in result]
    assert titles == sorted(titles)

def integrityTest_mergeSort(unsortedEvents):
    # TESTING IF mergeSort KEEPS DATA INTEGRITY (NO DELETED OR DUPLICATED EVENTS)
    result = mergeSort(unsortedEvents)
    assert len(result) == len(unsortedEvents)
    assert set(e.id for e in result) == set(e.id for e in unsortedEvents)



# QUICK SORT TESTS
def basicTest_quickSort(unsortedEvents, sortedOrder):
    # TESTING IF quickSort CORRECTLY ORDERS EVENTS BY DATE > TIME > LOCATION
    result = quickSort(unsortedEvents)
    assert result == sortedOrder

def singleTest_quickSort(singleEvent):
    # TESTING IF quickSort HANDLES LIST WITH SINGLE EVENT
    result = quickSort(singleEvent)
    assert len(result) == 1
    assert result[0] == sample_array.brunch

def sortedTest_quickSort(alreadySorted, sortedOrder):
    # TESTING IF quickSort BREAKS/CORRUPTS A SORTED LIST
    result = quickSort(alreadySorted)
    assert result == sortedOrder

def customTest_quickSort(unsortedEvents):
    # TESTING IF quickSort CAN SORT BY CUSTOM KEY (SORTING BY TITLE ALPHABETICALLY)
    result = quickSort(unsortedEvents, key=lambda e: e.title)
    titles = [e.title for e in result]
    assert titles == sorted(titles)

def integrityTest_quickSort(unsortedEvents):
    # TESTING IF quickSort KEEPS DATA INTEGRITY (NO DELETED OR DUPLICATED EVENTS)
    result = quickSort(unsortedEvents)
    assert len(result) == len(unsortedEvents)
    assert set(e.id for e in result) == set(e.id for e in unsortedEvents)



# CROSS-ALGORITHM CONSISTENCY TEST
# ENSURING ALL 3 ALGORITHMS CREATE SAME OUTPUT FOR SAME INPUT; LIST SHOULD BE SAME
def agreeTest(unsortedEvents):
    import copy
    result_insert = insertSort(copy.copy(unsortedEvents))
    result_merge  = mergeSort(copy.copy(unsortedEvents))
    result_quick  = quickSort(copy.copy(unsortedEvents))
    assert result_insert == result_merge
    assert result_merge  == result_quick
