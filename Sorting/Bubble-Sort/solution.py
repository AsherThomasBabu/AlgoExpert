# Write a finction that takes in an array of integers and returns a sorted version of that array. Use Bubble sort algorithm to sort the array.

#  Best and worst case, | Runs in O(n^2)\
    
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array