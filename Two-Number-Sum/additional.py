# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two different integers in the array. you can't add a single integer to itself in order to obtain the target sum.
# You can assume that there will be at most one pair of numbers summing up to the target sum.

def twoNumberSum(array, targetSum):
    array.sort()

    leftInd = 0
    rightInd = len(array) - 1 

    while leftInd < rightInd:
        checkSum = array[leftInd] + array[rightInd]
    
        if checkSum == targetSum:
            return [array[leftInd],array[rightInd]]
        elif checkSum < targetSum:
            leftInd += 1
        elif checkSum > targetSum:
            rightInd -= 1

    return[]