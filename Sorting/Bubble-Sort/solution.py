# Write a finction that takes in an array of integers and returns a sorted version of that array. Use Bubble sort algorithm to sort the array.

def bubbleSort(array):
    for i in range(len(array)-1-i):
        for j in range(i,len(array)):
            if array[j] >= array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array