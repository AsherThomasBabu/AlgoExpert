# Write a function that takes in a non-empty array of Integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

def sortedSquaredArray(array):
    sortedArray = [0 for i in range(len(array))]
    leftInd = 0
    rightInd = len(array)-1
    arrayLen = len(array) -1

    for i in range(arrayLen + 1):
        leftVal = abs(array[leftInd])
        rightVal = abs(array[rightInd])

        if leftVal > rightVal:
            sortedArray[arrayLen-i] = leftVal**2
            leftInd += 1
        else:
            sortedArray[arrayLen-i] = rightVal**2
            rightInd -= 1
    return sortedArray
