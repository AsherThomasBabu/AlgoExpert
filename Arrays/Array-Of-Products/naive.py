# Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.
# In other words, the value at output[1] is equal to the product of every number in the Input array other than input[1]
# Note that you're expected to solve this problem without using division.

# Sample Input
# array = [5, 1, 4, 2]
# Sample Output
# [8, 40, 10, 20]

def arrayOfProducts(array):
    result = []
    for i in range(len(array) ):
        tempProduct = 1
        for j in range(len(array)):
            if i != j:
                tempProduct *= array[j]
        result.append(tempProduct)

    return result
                
