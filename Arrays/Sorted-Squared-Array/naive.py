# Write a function that takes in a non-empty array of Integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

def sortedSquaredArray(array):
    # Write your code here.
    new = []
    for i in range (0, len(array)):
        temp= array[i]*array[i]
        new.append(temp)
    new.sort()
    return new
