### ### array testing  of campus event scheduling system

from dynamic_array import DynamicArrayEvent
from event_creator import Event
import sample_array
import pytest


@pytest.fixture

def da():
    """ Provides fresh instance of the DynamicArrayEvent class and cleans up after test. """
    return DynamicArrayEvent()

def test_insert_event(da):
    """ Tests if insertion works in dynamic array. """
    # Creates dynamic array with events from sample_array
    for event in sample_array.friday:
        da.append(event)
    # Inserts event at index 3
    da.insert(3,sample_array.hhour) 
    # Checks if event is at index 3
    assert da.get_at(3) == sample_array.hhour
    
def test_insert_error(da):
    """ Tests for ValueError for inserting out of bounds. """
    # Creates dynamic array with events from sample_array
    for event in sample_array.friday:
        da.append(event)
    # Check if ValueError is Raised when index is out of bounds
    with pytest.raises(ValueError, match="Index is out of bounds"):
            da.insert(6, sample_array.stars)

def test_delete_event(da):
    """ Tests for delete method. """
    # Creates dynamic array with events from sample_array
    for event in sample_array.friday:
        da.append(event)
    # Use delete method
    da.delete(sample_array.hhour.id)
    # If length is 4 test passes, since original length was 5
    assert len(da) == 4

def test_search_by_id(da):
    """ Tests for search_by_id method. """
    # Creates dynamic array with events from sample_array
    for event in sample_array.friday:
       da.append(event)
    # Use search_by_id method 
    result = da.search_by_id(sample_array.hhour.id)
    # Checks if result is the event of resulting id inputted
    assert result == sample_array.hhour

def test_search_by_id_none(da):
    """ Tests for search_by_id method when id is not in linked list. """
    # Creates dynamic array with events from sample_array
    for event in sample_array.friday:
        da.append(event)
    # Use delete method to remove event
    da.delete(sample_array.hhour.id)
    # Use search_by_id method 
    result = da.search_by_id(sample_array.hhour.id)
    # Check if search_by_id returns None
    assert result == None

def test_list_all(da):
    """ Tests for the list_all method. """
    # Creates dynamic with events from sample_array
    for event in sample_array.friday:
        da.append(event)
    # Use list_all method
    result = da.list_all()
    # Check if list all is equal to sample array list.
    assert result == sample_array.friday
