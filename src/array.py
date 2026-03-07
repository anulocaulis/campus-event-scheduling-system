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
  # Resizing Method
  def resize(self):
    # Doubles capacity of array when capacity is full.
    self.capacity = self.capacity * 2
    # Creates new empty array with updated capacity.
    new_array = [None] * self.capacity
    # Set Counter to zero
    i = 0
    # Only run while inside the list.
    while i < self.size:
      # Transfers old arrays to new resized array
      new_array[i] = self.array[i]
      i += 1
    # Provides new array with old array values.
    self.array = new_array
  def insert(self,event):
    # If at full capacity, simply resize array.
    if self.size == self.capacity:
      self.resize()
    pass
  def search_by_id(self, target_id):
    pass
  def delete(self, target_id):
    pass
  def list_all(self):
    pass
  
    
    

### Store events (call event-creator.py)
eventArray = []
### Sort events
# Quick sort 

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
