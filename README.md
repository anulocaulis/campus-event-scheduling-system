# campus-event-scheduling-system
Group project #1 for Data Structures and Algorithms -- DTSC 5501 -- Dr. Alfonso Bastias


### explain roles

- Mike Beitner:
- Chris Taylor: Created event_creator, sorting/search algorithms, and compare performance of sorting algorithms
- Luis: Created the methods for the Linked List and the Dynamic Array. Added the theoretical time complexities for these data structures.

### explain project design

#### Event Creator
For our campus event scheduling system project, we first decided to use an event class event_creator.py in order to handle all the event data. This event creator function helps create our 
campus events with the option to randomize the ID for each event. 

### Storage Structure
We created two data structures to hold our campus events in for later use such as searching and sorting. 
- Dynamic Array: For our dynamic array, since it is a resizable array, we will double the capacity of our dynamic array anytime it fills its capacity. This allows us to have a mutable array, allowing us to use methods to append, insert, search by id, and delete, to modify the campus events

- Linked List. Our Linked List is a singly linked list. This means it will have nodes that contain our events, and each node will connect to another until it reaches the end of the linked list when the final node is connected to None. The linked list is also mutable, allowing us to to use methods such as push, append, insert, search by id, and delete to modify the campus events.

### explain results


