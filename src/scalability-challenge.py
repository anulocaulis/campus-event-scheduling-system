### Tests Array vs Linked List implementation at n = 1,000,000 events
# imports
from randEvent import Event, genEvents
from dynamic_array import DynamicArrayEvent
from linked_list import EventLinkedList
from searching import binary
import random
import time

def generate_scalability_data():
    """
    GENERATES ONE MILLION RANDOM EVENTS AND LOADS THEM INTO BOTH A DYNAMIC ARRAY AND LINKED LIST
    RETURNS:
        arr - DynamicArrayEvent CONTAINING ONE MILLION EVENTS
        ll - EventLinkedList CONTAINING ONE MILLION EVENTS
        gen_time - TIME TAKEN TO GENERATE AND LOAD EVENTS INTO BOTH STRUCTURES
    """    
    # create a million events
    n = 1000000
    events = genEvents(n)
    # load into linked list and dynamic array
    start = time.perf_counter()
    arr = DynamicArrayEvent()
    ll = EventLinkedList()
    for event in events:
        arr.append(event)
        ll.append(event)
    end = time.perf_counter()
    gen_time = end - start
    return arr, ll, gen_time

def merge_sort_large_array(arr):
    """
    SORTS THE LARGE DYNAMIC ARRAY USING MERGE SORT AND MEASURES TIME TAKEN
    PARAMS:
        arr - DynamicArrayEvent CONTAINING ONE MILLION EVENTS
    RETURNS:
        time - TIME TAKEN TO SORT THE ARRAY
    """
    start = time.perf_counter()
    arr.sort()
    end = time.perf_counter()
    return end - start
    
def merge_sort_large_linked_list(ll):
    """
    SORTS THE LARGE LINKED LIST USING MERGE SORT AND MEASURES TIME TAKEN
    PARAMS:
        ll - EventLinkedList CONTAINING ONE MILLION EVENTS
    RETURNS:
        time - TIME TAKEN TO SORT THE LINKED LIST
    """
    start = time.perf_counter()
    ll.sort()
    end = time.perf_counter()
    return end - start

def get_random_event_from_structures(arr):
    """
    GETS A RANDOM EVENT ID FROM THE DYNAMIC ARRAY FOR USE IN BINARY SEARCH TESTING
    PARAMS:
        arr - DynamicArrayEvent CONTAINING ONE MILLION EVENTS
    RETURNS:
        target_id - ID OF A RANDOMLY SELECTED EVENT FROM THE ARRAY
    """
    n = arr.size
    random_index = random.randint(0,n-1)
    target_id = arr.get_at(random_index).id
    return target_id

def binary_search_large_linked_list(id, ll):
    """
    SEARCHES FOR A RANDOM EVENT IN THE LARGE LINKED LIST USING BINARY SEARCH AND MEASURES TIME TAKEN
    PARAMS:
        ll - EventLinkedList CONTAINING ONE MILLION EVENTS
        id - ID OF THE EVENT TO SEARCH FOR
    RETURNS:
        time - TIME TAKEN TO PERFORM THE BINARY SEARCH
    """
    start = time.perf_counter()
    ll.binary(id, ll)
    end = time.perf_counter()
    return end - start

def binary_search_large_array(id, arr):
    """
    SEARCHES FOR A RANDOM EVENT IN THE LARGE DYNAMIC ARRAY USING BINARY SEARCH AND MEASURES TIME TAKEN
    PARAMS:
        arr - DynamicArrayEvent CONTAINING ONE MILLION EVENTS
        id - ID OF THE EVENT TO SEARCH FOR 
    RETURNS:
        time - TIME TAKEN TO PERFORM THE BINARY SEARCH
    """
    start = time.perf_counter()
    arr.binary(id,arr)
    end = time.perf_counter()
    return end - start



if __name__ == "__main__":
    print(" Generating one million random events ...")
    arr, ll, gen_time = generate_scalability_data()
    print("Event generation complete.")
    print("Attempting Merge Sort on array ...")
    merge_array = merge_sort_large_array(arr)
    print("Merge sort for array complete.")
    print("Attempting Merge Sort on linked list ...")
    merge_ll = merge_sort_large_linked_list(ll)
    print("Merge sort for linked list complete.")
    print("Generating random target event ID for binary search ...")
    target_id = get_random_event_from_structures(arr)
    print(f"Random target event ID selected: {target_id}")
    print("Attempting Binary Search Sort on linked list ...")
    bin_ll = binary_search_large_linked_list(ll, target_id)
    print("Binary Search Sort on linked list complete.")
    print("Attempting Binary Search Sort on array ...")
    bin_array = binary_search_large_array(arr, target_id)
    print("Binary Search Sort on array complete.")

    print("Time required by function:")
    print(f"Event generation time: {gen_time:.6f} seconds")
    print(f"Mergesort time for dynamic array: {merge_array:.6f} seconds")
    print(f"Mergesort time for linked list: {merge_ll:.6f} seconds")
    print(f"Binary search time for dynamic array: {bin_array:.6f} seconds")
    print(f"Binary search time for linked list: {bin_ll:.6f} seconds")