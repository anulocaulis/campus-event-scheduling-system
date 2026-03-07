import event_creator, sorting, searching
from event_creator import Event

### ARRAY IMPLEMENTATION OF SCHEDULING SYSTERM
class DynamicArray():
  def __init__(self):
    # Length of array
    self.size = 0
    # Maximum capacity of array
    self.capacity = 1
    # Creates array with empty slots.
    self.array = [None] * self.capacity

  # Length method
  def __len__(self):
    """
    Returns the length of the array
    """
    return self.size

### Store events (call event-creator.py)
eventArray = []
### Sort events
# Quick sort 

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
