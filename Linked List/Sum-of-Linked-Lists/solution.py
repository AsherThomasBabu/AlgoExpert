# You're given two Linked Lists of potentially unequal length. Each Linked List represents a non-negative Integer, where each node in the Linked List is a digit of that integer, and the first node in each Linked List always represents the least significant digit of the integer. Write a function that returns the head of a new Linked List that represents the sum of the integers represented by the two input Linked Lists.

# Each [LinkedList node has an integer [value] as well as a [next] node pointing to the next node in the list or to None/null if It's the tall of the list.

# The value of each LinkedList node is always in the range of 6 - 9

# Note: your function must create and return a new Linked List, and you're not allowed to modify elther of the Input Linked Lists.

# This is an input class. Do not edit.

# -------------Naive Solution | Incomplete | Runs in O(m+n) | Takes the same space too ------------------------

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedList = LinkedList(-1)
    curNode = newLinkedList
    carry = 0
    
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne else 0
        valueTwo = nodeTwo.value if nodeTwo else 0
        
        sumOfValues = valueOne + valueTwo + carry
        
        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        curNode.next = newNode
        curNode = newNode
        
        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None
        
    return newLinkedList.next
    
    
    
    