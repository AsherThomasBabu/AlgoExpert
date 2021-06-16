# Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively. The function should merge the lists in place (le, it shouldn't create a brand new list) and return the head of the merged list; the merged list should be in sorted order.

# Each LinkedList] node has an integer [value as well as a [next] node pointing to the next node in the list or to [None/null It's the tall of the list.

# You can assume that the Input linked lists will always have at least one node; In other words, the heads will never be None

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    l1 = headOne
    l2 = headTwo
    marker = LinkedList(-1)
    start = marker
    
    while l1 and l2:
        if l1.value < l2.value:
            marker.next = l1
            l1 = l1.next
        else:
            marker.next = l2
            l2 = l2.next  
        marker = marker.next
    
    if l1:
        marker.next = l1
    else:
        marker.next = l2
    
    return start.next
    

        
    
    
