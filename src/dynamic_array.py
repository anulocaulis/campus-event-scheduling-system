import sorting, searching
from event_creator import Event

### ARRAY IMPLEMENTATION OF SCHEDULING SYSTERM
class DynamicArrayEvent():

  # Initialize method
  def __init__(self):
    """
    INITIALIZES EMPTY DYNAMIC ARRAY
    PARAMS:
      self - DYNAMIC ARRAY BEING INITIALIZED
    RETURNS:
      None
    """
    # Length of array
    self.size = 0
    # Maximum capacity of array
    self.capacity = 1
    # Creates array with empty slots.
    self.array = [None] * self.capacity

  # Length method
  def __len__(self):
    """
    RETURNS THE LENGTH OF ARRAY
    PARAMS:
      self - ARRAY WHOSE LENGTH BEING MEASURED
    RETURNS:
      self.size - SIZE/LENGTH OF self ARRAY
    """
    return self.size
    
  # Resizing Method
  def resize(self):
    """
    DOUBLES THE CAPACITY OF THE ARRAY WHEN FULL
    PARAMS:
      self - ARRAY BEING RESIZED
    RETURNS:
      None - MODIFIES ARRAY IN PLACE
    """
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
    """
    ADDS A NEW EVENT TO THE END OF THE ARRAY
    PARAMS:
      self  - ARRAY BEING APPENDED TO
      event - EVENT OBJECT BEING ADDED
    RETURNS:
      None - MODIFIES ARRAY IN PLACE
    """
    # If at capacity resize the array.
    if self.size == self.capacity:
      self.resize()
    # Set last index of array equal to event value
    self.array[self.size] = event
    # Increase size counter
    self.size += 1
    
  # Insert Method
  def insert(self, index, event):
    """
    INSERTS A NEW EVENT AT A GIVEN INDEX
    PARAMS:
      self  - ARRAY BEING INSERTED INTO
      index - POSITION WHERE EVENT WILL BE INSERTED
      event - EVENT OBJECT BEING INSERTED
    RETURNS:
      None - MODIFIES ARRAY IN PLACE
    RAISES:
      ValueError - IF INDEX IS OUT OF BOUNDS
    """
    # If at full capacity, simply resize array.
    if self.size == self.capacity:
      self.resize()
    # Raise
    if index > self.size or index < 0:
      raise ValueError("This index is out of bounds.")
    # SHIFT ELEMENTS TO RIGHT 1 SPACE
    i = self.size
    while i > index:
      self.array[i] = self.array[i - 1]
      i -= 1
    # ADD NEW EVENT AT INDEX
    self.array[index] = event
    # INCREMENT SIZE UP BY 1
    self.size += 1

  # Search element by ID
  def search_by_id(self, target_id):
    """
    SEARCHES FOR AN EVENT BY ITS UNIQUE ID
    PARAMS:
      self      - ARRAY BEING SEARCHED
      target_id - ID OF THE EVENT BEING SEARCHED FOR
    RETURNS:
      self.array[i] - EVENT OBJECT IF FOUND
      None          - IF EVENT NOT FOUND
    """
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

  # Delete method
  def delete(self, target_id):
    """
    DELETES AN EVENT FROM THE ARRAY BY ITS UNIQUE ID
    PARAMS:
      self      - ARRAY BEING MODIFIED
      target_id - ID OF THE EVENT TO BE DELETED
    RETURNS:
      None - IF EVENT NOT FOUND OR AFTER SUCCESSFUL DELETION
    """
    # GET INDEX OF TARGET
    i = 0
    while i < self.size:
        if self.array[i].id == target_id:
            break
        i += 1
    # IF ID NOT FOUND RETURN NONE
    if i == self.size:
        return None
    # SHIFT ALL ELEMENTS OF ARRAY TO THE LEFT TO FILL IN THE GAP
    while i < self.size - 1:
        self.array[i] = self.array[i + 1]
        i += 1        
    # CLEAR THE LAST SPOT OF THE ARRAY/LIST AND DECREMENT SIZE
    self.array[self.size - 1] = None
    self.size -= 1 

  # Lists all events in dynamic array.
  def list_all(self):
    """
    RETURNS A LIST OF ALL EVENTS CURRENTLY IN THE ARRAY
    PARAMS:
      self - ARRAY BEING LISTED
    RETURNS:
      eventArray - PYTHON LIST CONTAINING ALL EVENT OBJECTS
    """
    # Create empty list to display events
    eventArray = []
    # set counter to zero
    i = 0
    # Run while inside the array
    while i < self.size:
      # Add event into empty list
      eventArray.append(self.array[i])
      i += 1
    # Return list. 
    return eventArray
      
  
    """
    Theoretical Complexities of Operations:

    
    append: Time Complexity O(1) amortized, O(n) worst case scenario
    
    Append is constant when dynamic array isn't at full capacity as 
    adding an event to the end of a list will always have the same runtime 
    unless it reaches its worst case when the dynamic array is at full capacity.

    
    resize: Time Complexity O(n)

    
    length: Time Complexity O(1)   

    
    insert: Time Complexity O(n)    

    
    search_by_id: Time Complexity O(n)

    
    delete: Time Complexity O(n)    

    
    list_all: Time Complexity O(n)
    
    
    """

    

### Store events (call event-creator.py)
eventArray = []
### Sort events
# Quick sort 

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
