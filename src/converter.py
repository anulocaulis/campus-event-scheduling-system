# FUNCTION TO CONVERT LINKED LIST INTO AN ARRAY FOR EASIER SORTING
def converter(linkedList):
    res = []
    curr = linkedList.head
    while curr:
        res.append(curr.event)
        curr = curr.next
    return res
