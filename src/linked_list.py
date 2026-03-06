from event_creator import Event

### linked list implementation of campus event scheduling system
class Node:
  def __init__(self,event):
    self.event = event
    self.next = None
    

class EventLinkedList:
  def __init__(self):
  self.head = None

def push(self):
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
  length = self.length()
  
  if length <= index or index < 0:
    raise ValueError("Index is out of bounds")
  
  else:
    while counter != index -1:
      counter += 1 
      temp = temp.next
      
    newNode.next = temp.next
    temp.next = newNode

def search_by_id(self, target_id):
  counter = 0 
  temp = self.head
  length = self.length()
  
  if length <= index or index < 0:
    raise ValueError("Index is out of bounds")

  else: 
    while counter != index -1 :
      counter +=1 
      temp = temp.next
    
    return temp.event
  

def delete(self, target_id):
  pass

def list_all(self):
  pass



### Store events (call event-creator.py)

### Sort events
# Quick sort

# Merge sort

# Insertion sort

### Search events
# Linear search

# Binary search
