# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an empty array.

def threeNumberSum(array, targetSum):
    array.sort()
    targetArray = []
    for i in range(len(array)-2):
        leftInd = i+1
        rightInd = len(array)-1
        while leftInd < rightInd:
            if array[i]+array[leftInd]+array[rightInd] == targetSum:
                targetArray.append([array[i],array[leftInd],array[rightInd]])
                leftInd += 1
                rightInd -= 1
            elif array[i]+array[leftInd]+array[rightInd] < targetSum:
                leftInd += 1
            elif array[i]+array[leftInd]+array[rightInd] > targetSum:
                rightInd -= 1
    return targetArray

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

threeNumberSum(array,targetSum)