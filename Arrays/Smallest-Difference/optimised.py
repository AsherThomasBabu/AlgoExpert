# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

# Note that the absolute difference of two Integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 Is 1.

# You can assume that there will only be one pair of numbers with the smallest difference.

# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]

# [28,26]

def smallestDifference(arrayOne, arrayTwo):
    arrayTwo.sort()
    arrayOne.sort()

    p1,p2,smallestDifference = 0,0,float('inf')

    result = []

    if arrayOne[p1] - arrayTwo[p2] == 0:
        return[arrayOne[p1] , arrayTwo[p2]]
    
    while p1<len(arrayOne) and p2 < len(arrayTwo):
        first = arrayOne[p1]
        second = arrayTwo[p2]

        currentDifference = abs(first - second)

        if first < second:
            p1 += 1
        elif second < first:
            p2 += 1
        else:
            return [first,second]

    
        if smallestDifference > currentDifference:
            smallestDifference = currentDifference
            result = [first,second]

    return result

