from event_creator import Event

### linked list implementation of campus event scheduling system
class Node:
  def __init__(self,event):
    # Store event data
    self.event = event
    # Pointer to next node, is defaulted to Null
    self.next = None

class EventLinkedList:
  def __init__(self):
    # Creates empty linked list 
    self.head = None

  # Push Method
  def push(self, event):
    """
    Pushes event to the front of linked list.
    """
    # Creates a new node
    newNode = Node(event)
    # Pointer points to head
    newNode.next = self.head
    # New Node becomes head
    self.head = newNode

  # Sort Method
  def sort(self, key=None):
    # IF EVENT DOESN'T ALREADY HAVE A SORT KEY, THIS GIVES IT ONE
    if key is None: key = lambda e: e.sortKey()
    
    # CONVERTING EVENTS FROM LINKED LIST TO AN ARRAY
    from converter import converter
    arr = converter(self)

    # SORTING THE ARRAY
    from sorting import insertSort
    sort_arr = insertSort(arr, key=key)

    # CONVERT SORTED ARRAY BACK INTO LINKED LIST NODES
    temp = self.head
    for event in sort_arr:
      temp.event = event
      temp = temp.next

  # Append Method
  def append(self, event):
    # Creates a new node
    newNode = Node(event)
    # Names new node head if linked list is empty
    if self.head is None:
      self.head = newNode
    else:
      # Creates temporary head
      temp = self.head
      # Traverses until end of list and connects pointer of last node to newNode.
      while temp.next:
        temp = temp.next
      temp.next = newNode

  # Length of linked list
  def __len__(self):
    """
    returns the length of the linked list.
    """
    # Size counter set to zero
    size = 0 
    # Temporary head
    temp = self.head
    # Traverse Linked List
    while temp != None:
      # Iterate size counter until it reaches end
      size += 1 
      # Move to next node
      temp = temp.next 
    # Return size counter
    return size
 
  # Insert Method
  def insert(self, index, event):
    """
    Inserts event into linked list by index.
    """
    # If index is zero push first element to connect to next node
    if index == 0:
      self.push(event)
      return

    # Set counter to zero
    counter = 0
    # Set temporary head
    temp = self.head

    # Create New Node
    newNode = Node(event)
    # Grab length of linked list
    length_ll = len(self)
    # Raise value error if index is out of bounds
    if length_ll < index or index < 0:
      raise ValueError("Index is out of bounds")
    
    else:
      # Traverse before the target index 
      while counter != index -1:
        # Increment counter
        counter += 1 
        # Move to next node
        temp = temp.next
      # new node is pointing to target node
      newNode.next = temp.next
      # Left node is pointing to new node
      temp.next = newNode

  # Search by ID method
  def search_by_id(self, target_id):
    """
    Searches event ID in linked list and returns that event
    """
    # Set temporary head
    temp = self.head 

    # Traverse to end of list.
    while temp != None:
      # Check if node id is equal to target id 
      if temp.event.id == target_id:
        # Return event
        return temp.event
      # Move to next node 
      temp = temp.next
    # If no target_id is found after traversing linked list return None
    return None
    
  # Delete method 
  def delete(self, target_id):
    """
    Deletes event by using event ID
    """
    # Set temporary head
    temp = self.head
    # Print message when linked list is empty.
    if temp is None:
      print("Cannot delete empty list")
      return
    # Check if head node is equal to target id 
    if temp.event.id == target_id:
      # Remove head by moving head to next node
      self.head = self.head.next
      return

    # While pointer is not pointing to null
    while temp.next != None:
      # If the event id of the next node is equal to target node
      if temp.next.event.id == target_id:
        # Delete target node by pointing to node after it.
        temp.next = temp.next.next
        # End while loop
        return
      # Continues to next node.
      temp = temp.next
  
  # List All Method
  def list_all(self):
    """
    Displays all events in linked list
    """
    # Empty string
    output = ""
    # Set temporary head
    temp = self.head

    # Traverse to end of list
    while temp != None:
      # Add event string and pointer ->
      output += str(temp.event) + "->"
      # Move to next node
      temp = temp.next
    # Print linked list. 
    return output

  """
  Theoretical Complexities of Operations:
  
  push: Time Complexity O(1)
  Pushes Node into front of the Linked List.
  
  append: Time Complexity O(n)
  Inserts Node into end of linked list, will have to traverse through the whole node.
  
  length: Time Complexity O(n)
  Traverses the whole array to retrieve length of linked list.
  
  insert: Time Complexity(n)
  Traverses linked list, and inserts node into selected index.
  
  search_by_id: Time Complexity(n)
  Search Id of Node by traversing through the linked list until target ID is found.
  
  delete: Time Complexity(n)
  To delete a node you have to traverse through linked list to delete selected node.
  
  list_all: Time Complexity(n)
  To list all nodes, you have to go through the whole linked list.
  
  
  """


### Store events (call event-creator.py)


### Sort events
# Quick sort

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
