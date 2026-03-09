from event_creator import Event

"""
Theoretical Complexities of Operations:
  
push: Time Complexity O(1) - Pushes Node into front of the Linked List.
append: Time Complexity O(n) - Inserts Node into end of linked list, will have to traverse through the whole list.
length: Time Complexity O(1) - Returns size at constant time by using a size counter
get_at: Time Complexity O(n) - Traverses through linked list until it retrieves event at given index.
insert: Time Complexity O(n) - Traverses linked list, and inserts node into selected index.
sort: Time Complexity O(nlogn) - average for mergeSort and quickSort
      Time Complexity O(n^2) - worst case for insertSort
search_by_id: Time Complexity O(n) - Search Id of Node by traversing through the linked list until target ID is found.
delete: Time Complexity O(n) - To delete a node you have to traverse through linked list to delete selected node.
list_all: Time Complexity O(n) - To list all nodes, you have to go through the whole linked list.

"""

### linked list implementation of campus event scheduling system
class Node:
  def __init__(self,event):
    """
    INITIALIZES A SINGLE NODE IN THE LINKED LIST
    PARAMS:
      self  - NODE BEING INITIALIZED
      event - EVENT OBJECT STORED IN THE NODE
    RETURNS:
      None
    """
    # Store event data
    self.event = event
    # Pointer to next node, is defaulted to Null
    self.next = None

class EventLinkedList:
  def __init__(self):
    """
    INITIALIZES AN EMPTY LINKED LIST
    PARAMS:
      self - LINKED LIST BEING INITIALIZED
    RETURNS:
      None
    """
    self.head = None
    # size counter 
    self.size = 0

  # Push Method
  def push(self, event):
    """
    PUSHES A NEW EVENT TO THE FRONT OF THE LINKED LIST
    PARAMS:
      self  - LINKED LIST BEING MODIFIED
      event - EVENT OBJECT BEING PUSHED TO FRONT
    RETURNS:
      None - MODIFIES LINKED LIST IN PLACE
    """
    # Creates a new node
    newNode = Node(event)
    # Pointer points to head
    newNode.next = self.head
    # New Node becomes head
    self.head = newNode
    # Increment size 
    self.size +=1

  # Sort Method
  def sort(self, algorithm='mergeSort', key=None):
    """
    SORTS THE LINKED LIST IN PLACE USING INSERTION SORT
    PARAMS:
      self - LINKED LIST BEING SORTED
      algorithm - SORT ALGORITHM TO USE: 'insertSort', 'mergeSort', 'quickSort'
      key  - SORT KEY FUNCTION, DEFAULTS TO sortKey() (DATE > TIME > LOCATION)
    RETURNS:
      None - MODIFIES LINKED LIST IN PLACE
    RAISES:
      ValueError - IF UNKNOWN ALGORITHM NAME GIVEN
    """
    # IF EVENT DOESN'T ALREADY HAVE A SORT KEY, THIS GIVES IT ONE
    if key is None: key = lambda e: e.sortKey()
    
    # CONVERTING EVENTS FROM LINKED LIST TO AN ARRAY
    from converter import converter
    arr = converter(self)

    # SORTING THE ARRAY
    from sorting import insertSort, mergeSort, quickSort
    if algorithm == 'insertSort':
      sorted = insertSort(arr, key=key)
    elif algorithm == 'mergeSort':
      sorted = mergeSort(arr, key=key)
    elif algorithm == 'quickSort':
      sorted = quickSort(arr, key=key)
    else:
      raise ValueError(f"Unknown algorithm '{algorithm}'. Choose 'insertSort', 'mergeSort', or 'quickSort'")
    
    # CONVERT SORTED ARRAY BACK INTO LINKED LIST NODES
    temp = self.head
    for event in sorted:
      temp.event = event
      temp = temp.next

  # Append Method
  def append(self, event):
    """
    ADDS A NEW EVENT TO THE END OF THE LINKED LIST
    PARAMS:
      self  - LINKED LIST BEING APPENDED TO
      event - EVENT OBJECT BEING ADDED
    RETURNS:
      None - MODIFIES LINKED LIST IN PLACE
    """
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
    # Increment size 
    self.size +=1

  # Length of linked list
  def __len__(self):
    """
    RETURNS THE LENGTH OF THE LINKED LIST
    PARAMS:
      self - LINKED LIST WHOSE LENGTH IS BEING MEASURED
    RETURNS:
      size - NUMBER OF NODES IN THE LINKED LIST
    """
    return self.size

  def get_at(self, index):
    """
    GETS EVENT AT GIVEN INDEX
    PARAMS:
      self - LINKED LIST TO PULL EVENT WITH GIVEN INDEX
      INDEX - POSITION WHERE WE WILL GET EVENT

    RETURNS: 
        temp.event - EVENT OBJECT IF FOUND.
    RAISES:
        ValueError - IF INDEX IS OUT OF BOUNDS.
    """
    
    # Set counter to zero
    counter = 0
    # Set temporary head
    temp = self.head
    # Grabs length of Linked List  
    length_ll = len(self)
    # Raise
    if length_ll <= index or index < 0:
      raise ValueError("Index is out of bounds")
    
    else:
      # Traverse linked list until equal to index
      while counter != index:
        counter += 1
        temp = temp.next
    # Return event node
    return temp.event
  
 
  # Insert Method
  def insert(self, index, event):
    """
    INSERTS A NEW EVENT AT A GIVEN INDEX IN THE LINKED LIST
    PARAMS:
      self  - LINKED LIST BEING INSERTED INTO
      index - POSITION WHERE EVENT WILL BE INSERTED
      event - EVENT OBJECT BEING INSERTED
    RETURNS:
      None - MODIFIES LINKED LIST IN PLACE
    RAISES:
      ValueError - IF INDEX IS OUT OF BOUNDS
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
      # Increment size 
      self.size +=1

  # Search by ID method
  def search_by_id(self, target_id):
    """
    SEARCHES FOR AN EVENT BY ITS UNIQUE ID
    PARAMS:
      self      - LINKED LIST BEING SEARCHED
      target_id - ID OF THE EVENT BEING SEARCHED FOR
    RETURNS:
      temp.event - EVENT OBJECT IF FOUND
      None       - IF EVENT NOT FOUND
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
    DELETES AN EVENT FROM THE LINKED LIST BY ITS UNIQUE ID
    PARAMS:
      self      - LINKED LIST BEING MODIFIED
      target_id - ID OF THE EVENT TO BE DELETED
    RETURNS:
      None - IF LIST IS EMPTY, EVENT NOT FOUND, OR AFTER SUCCESSFUL DELETION
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
      # Decrement size 
      self.size -=1  
      return

    # While pointer is not pointing to null
    while temp.next != None:
      # If the event id of the next node is equal to target node
      if temp.next.event.id == target_id:
        # Delete target node by pointing to node after it.
        temp.next = temp.next.next
        # Decrement size
        self.size -=1  
        return

      # Continues to next node.
      temp = temp.next
  
  # List All Method
  def list_all(self):
    """
    RETURNS A LIST OF ALL EVENTS IN THE LINKED LIST
    PARAMS:
      self - LINKED LIST BEING LISTED
    RETURNS:
      output - List of all events in linked list.
    """
    # Empty list
    output = []
    # Set temporary head
    temp = self.head

    # Traverse to end of list
    while temp != None:
      # Append
      output.append(temp.event)
      # Move to next node
      temp = temp.next
    # Print linked list. 
    return output
