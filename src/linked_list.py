from event_creator import Event

### linked list implementation of campus event scheduling system
class Node:
  def __init__(self,event):
    self.event = event
    self.next = None
    

class EventLinkedList:
  def __init__(self):
  self.head = None

  def push(self, event):
    newNode = Node(event)
    newNode.next = self.head
    self.head = newNode

# Length of linked list
  def length(self):
    size = 0 
    temp = self.head 
    while temp != None:
      size += 1 
      temp = temp.next 
    return size
 

# Insert to linked list
  def insert(self, index, event):
    if index == 0:
      self.push(event)
      return
      
    counter = 0
    temp = self.head
  
    newNode = Node(event)
    length_ll = self.length()
    
    if length_ll < index or index < 0:
      raise ValueError("Index is out of bounds")
    
    else:
      while counter != index -1:
        counter += 1 
        temp = temp.next
        
      newNode.next = temp.next
      temp.next = newNode
  
  def search_by_id(self, target_id):
    temp = self.head 
  
    while temp != None:
      if temp.event.id == target_id:
        return temp.event
      temp = temp.next
    # If no target_id is found after traversing linked list return None
    return None
    
  
  def delete(self, target_id):
    temp = self.head
  
    if temp.event.id == target_id:
      self.head = self.head.next
      return
  
    while temp.next != None:
      if temp.next.event.id == target_id:
        temp.next = temp.next.next
      temp = temp.next
  
  def list_all(self):
  
    output = ""
    temp = self.head
  
    while temp != None:
      output += str(temp.event) + "->"
      temp = temp.next
    print(output)
    


### Store events (call event-creator.py)

### Sort events
# Quick sort

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
