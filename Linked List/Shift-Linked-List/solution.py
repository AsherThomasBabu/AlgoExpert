# Write a function that takes in the head of a Singly Linked List and an integer [k, shifts the list in place (i.e., doesn't create a brand new list) by k positions, and returns its new head.

# Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate. For example, shifting a Linked List forward by one position would make its tall become the new head of the linked list.

# Whether nodes are moved forward or backward is determined by whether is positive or negative.

# Each LinkedList node has an integer [value] as well as a [next] node pointing to the next node in the list or to None if  It's the tail of the list.

# You can assume that the input Linked List will always have at least one node; in other words, the head will never be None

# This is the class of the input linked list.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
	count = 1
	cur,header = head,head
	while cur.next != None:
		cur = cur.next
		count += 1
	cur.next = head
	k = k % count
	for _ in range(count - k -1):
		header = header.next
	out = header.next
	header.next = None
	
	return out