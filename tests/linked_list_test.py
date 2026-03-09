from linked_list import EventLinkedList
from event_creator import Event
import sample_array
import pytest


@pytest.fixture

def ll():
    """ Provides fresh instance of the EventLinkedList class and cleans up after test. """
    return EventLinkedList()

def test_insert_event(ll):
    """ Tests if insertion works in linked list. """
    # Creates linked list with events from sample_array
    for event in sample_array.friday:
        ll.append(event)
    # Inserts event at index 2
    ll.insert(2,sample_array.hhour)
    # Checks if event is at index 2
    assert ll.get_at(2) == sample_array.hhour
    
def test_insert_error(ll):
    """ Tests for ValueError for inserting out of bounds. """
    # Creates linked list with events from sample_array
    for event in sample_array.friday:
        ll.append(event)
    # Check if ValueError is Raised when index is out of bounds
    with pytest.raises(ValueError, match="Index is out of bounds"):
            ll.insert(6, sample_array.stars)

def test_delete_event(ll):
    """ Tests for delete method. """
    # Creates linked list with events from sample_array
    for event in sample_array.friday:
        ll.append(event)
    # Use delete method
    ll.delete(sample_array.hhour.id)
    # If length is 4 test passes, since original length was 5
    assert len(ll) == 4

def test_search_by_id(ll):
    """ Tests for search_by_id method. """
    # Creates linked list with events from sample_array
    for event in sample_array.friday:
       ll.append(event)
    # Use search_by_id method 
    result = ll.search_by_id(sample_array.hhour.id)
    # Checks if result is the event of resulting id inputted
    assert result == sample_array.hhour

def test_search_by_id_none(ll):
    """ Tests for search_by_id method when id is not in linked list. """
    # Creates linked list with events from sample_array
    for event in sample_array.friday:
        ll.append(event)
    # Use delete method to remove event
    ll.delete(sample_array.hhour.id)
    # Use search_by_id method 
    result = ll.search_by_id(sample_array.hhour.id)
    # Check if search_by_id returns None
    assert result == None

def test_list_all(ll):
    """ Tests for the list_all method. """
    # Creates linked list with events from sample_array
    for event in sample_array.friday:
        ll.append(event)
    # Use list_all method
    result = ll.list_all()
    # Check if list all is equal to sample array list.
    assert result == sample_array.friday
