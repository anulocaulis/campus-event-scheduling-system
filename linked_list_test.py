### linked list testing of campus event scheduling system

from linked_list import EventLinkedList
from event_creator import Event
import sample_array
import pytest


@pytest.fixture

def ll():
    """ Provides fresh instance of the EventLinkedList class and cleans up after test. """
    return EventLinkedList()

def test_insert_event(ll):
    ll.insert(0,sample_array.hhour)
    assert ll.get_at(0) == sample_array.hhour
    
def test_insert_error(ll):
    for event in sample_array.friday:
        ll.append(event)
    with pytest.raises(ValueError, match="Index is out of bounds"):
            ll.insert(6, sample_array.stars)

def test_delete_event(ll):
    # Events added into linked list will have length 5
    for event in sample_array.friday:
        ll.append(event)
    ll.delete(sample_array.hhour.id)
    # If length is 4 test passes.
    assert len(ll) == 4

def test_search_by_id(ll):
    for event in sample_array.friday:
       ll.append(event)
    result = ll.search_by_id(sample_array.hhour.id)
    assert result == sample_array.hhour

def test_search_by_id_none(ll):
    for event in sample_array.friday:
        ll.append(event)
    ll.delete(sample_array.hhour.id)
    result = ll.search_by_id(sample_array.hhour.id)
    assert result == None

def test_list_all(ll):
    for event in sample_array.friday:
        ll.append(event)
    result = ll.list_all()
    assert result == sample_array.friday
