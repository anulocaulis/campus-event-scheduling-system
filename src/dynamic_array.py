import event_creator, sorting, searching
from event_creator import Event

### ARRAY IMPLEMENTATION OF SCHEDULING SYSTERM
class DynamicArrayEvent():
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
    # Only run while inside the array.
    while i < self.size:
      # Transfers old arrays to new resized array
      new_array[i] = self.array[i]
      i += 1
    # Provides new array with old array values.
    self.array = new_array
  
  # Append method
  def append(self, event):
    # If at capacity resize the array.
    if self.size == self.capacity:
      self.resize()
    # Set last index of array equal to event value
    self.array[self.size] = event
    # Increase size counter
    self.size += 1
    
  # Insert Method
  def insert(self,index, event):
    # If at full capacity, simply resize array.
    if self.size == self.capacity:
      self.resize()
    elif index > self.size or index < 0:
      raise ValueError("This index is out of bounds.")
    pass

  
  def search_by_id(self, target_id):
    # Set counter to zero
    i = 0
    # Only run while inside the array
    while i < self.size:
      # Returns event iteration if it matches target id
      if self.array[i].id == target_id:
        return self.array[i]
      i += 1
    # Return None if target id not in array.
    return None
    
  def delete(self, target_id):
    pass
    
  def list_all(self):
    i = 0
    while i < self.size:
      print(self.array[i])
      i += 1
  
    
    

### Store events (call event-creator.py)
eventArray = []
### Sort events
# Quick sort 

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
