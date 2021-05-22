# Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.
# In other words, the value at output[1] is equal to the product of every number in the Input array other than input[1]
# Note that you're expected to solve this problem without using division.

# Sample Input
# array = [5, 1, 4, 2]
# Sample Output
# [8, 40, 10, 20]

def arrayOfProducts(array):
    leftRunning = 1
    rightRunning = 1

    products = [1]*len(array)

    for i in range(len(array)):
        products[i] = leftRunning
        leftRunning *= array[i]

    for i in reversed(range(len(array))):
        products[i] *= rightRunning
        rightRunning *= array[i]

    return products

