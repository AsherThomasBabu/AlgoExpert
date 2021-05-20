# Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

# Note that the absolute difference of two Integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 Is 1.

# You can assume that there will only be one pair of numbers with the smallest difference.

# arrayOne = [-1, 5, 10, 20, 28, 3] 
# arrayTwo = [26, 134, 135, 15, 17]

# [28,26]

def smallestDifference(arrayOne, arrayTwo):
    difference = arrayTwo[0]-arrayOne[0]
    arr = []

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            if abs(arrayOne[i]-arrayTwo[j]) <= abs(difference):
                difference = abs(arrayOne[i]-arrayTwo[j])
                arr = [arrayOne[i],arrayTwo[j]]
    return arr

arrayOne = [-1, 5, 10, 20, 28, 3] 
arrayTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrayOne, arrayTwo))