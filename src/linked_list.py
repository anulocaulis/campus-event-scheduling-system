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

  def push(self, event):
    # Creates a new node
    newNode = Node(event)
    # Pointer points to head
    newNode.next = self.head
    # New Node becomes head
    self.head = newNode

# Length of linked list
  def length(self):
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
 

# Insert to linked list
  def insert(self, index, event):
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
    length_ll = self.length()
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
  
  def search_by_id(self, target_id):
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
    
  
  def delete(self, target_id):
    # Set temporary head
    temp = self.head
    
    # Check if head node is equal to target id 
    if temp.event.id == target_id:
      # Remove head by moving head to next node
      self.head = self.head.next
      return
  
    while temp.next != None:
      if temp.next.event.id == target_id:
        temp.next = temp.next.next
        return
      temp = temp.next
  
  def list_all(self):
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
    print(output)
    


### Store events (call event-creator.py)

### Sort events
# Quick sort

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
