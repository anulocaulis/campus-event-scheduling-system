# FUNCTION TO CONVERT LINKED LIST INTO AN ARRAY FOR EASIER SORTING

def converter(linkedList):
    """
    CONVERTS LINKED LIST INTO AN ARRAY FOR COMPARATIVELY EASY SORTING
    PARAMS:
        linkedList - LINKED LIST OF EVENT OBJECTS
    RETURNS:
        res - ARRAY BUILT FROM LINKED LIST ELEMENTS
    """
    res = []
    curr = linkedList.head
    while curr:
        res.append(curr.event)
        curr = curr.next
    return res
