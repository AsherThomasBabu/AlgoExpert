# Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively. The function should merge the lists in place (le, it shouldn't create a brand new list) and return the head of the merged list; the merged list should be in sorted order.

# Each LinkedList] node has an integer [value as well as a [next] node pointing to the next node in the list or to [None/null It's the tall of the list.

# You can assume that the Input linked lists will always have at least one node; In other words, the heads will never be None

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    recursiveMerger(headOne,headTwo,None)
    return headOne if headOne.value < headTwo.value else headTwo

def recursiveMerger(p1,p2, p1Prev):
    if p1 is None:
        p1Prev.next = p2
        return
    if p2 is None:
        return
    
    if p1.value < p2.value:
        recursiveMerger(p1.next,p2,p1)
    else:
        if p1Prev is not None:
            p1Prev.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerger(p1,newP2,p2)
