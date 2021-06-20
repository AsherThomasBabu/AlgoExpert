# Write a function that takes in a non-enpty array of integers and returns the maximum sum that can be obtained by summing up all of the integers in a non-empty subarray of the input arary. A subarray must only contain adjacent numbers (numbers next to each other in the input array).

def kadanesAlgorithm(array):
    sumSoFar = 0
    maxSoFar = 0
    for i in range(len(array)):
        sumSoFar = max(sumSoFar+array[i],array[i])
        maxSoFar = max(maxSoFar,sumSoFar)
    return maxSoFar if maxSoFar else -1