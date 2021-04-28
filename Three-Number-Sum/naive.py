# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an empty array.

def threeNumberSum(array, targetSum):
    targetArray = []
    for i in array:
        for j in array:
            for k in array:
                if i!=j and j!=k and i!=k and i+j+k == targetSum:
                    temp = [i,j,k]
                    temp.sort()
                    if temp not in targetArray:
                        targetArray.append(temp)
                        
    targetArray.sort()
    return targetArray