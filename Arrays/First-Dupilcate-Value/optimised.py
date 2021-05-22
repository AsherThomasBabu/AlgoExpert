# Given an array of integers between and n inclusive, where is the length of the array, write a function that returns the first
# Integer that appears more than once (when the array is read from left to right).
# In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum Index.
# If no integer appears more than once, your function should return -1
# Note that you're allowed to mutate the input array.

# Sample input = [2, 1, 5, 2, 3, 3, 4]
# Output = 2

def firstDuplicateValue(array):
    for value in array:
        absVal = abs(value)
        if array[absVal - 1] < 0:
            return absVal
        array[absVal - 1] *= -1
    return -1
    
        
print(firstDuplicateValue([2,3,4,2]))
