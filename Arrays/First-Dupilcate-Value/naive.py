# Given an array of integers between and n inclusive, where is the length of the array, write a function that returns the first
# Integer that appears more than once (when the array is read from left to right).
# In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum Index.
# If no integer appears more than once, your function should return -1
# Note that you're allowed to mutate the input array.

# Sample input = [2, 1, 5, 2, 3, 3, 4]
# Output = 2

def firstDuplicateValue(array):
    temp = len(array)
    for i in range(len(array)):
        for j in range(i,len(array)):
            if i!=j and array[i] == array[j]:
                temp = min(temp,j)
    if temp == len(array):
        return -1
    else:
        return array[temp]
        
print(firstDuplicateValue([2,3,4,5]))
