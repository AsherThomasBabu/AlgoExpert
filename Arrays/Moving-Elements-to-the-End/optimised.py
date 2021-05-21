# """
# Move Element To End
# You are given an array of integers and an integer.
# Write a function that moves all instances of that integer in the array to the end of the array.
# The function should perform this in place and does not need to maintain the order of the other integers.
# Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2
# Sample output: [1, 3, 4, 2, 2, 2, 2, 2]  or  [4, 3, 1, 2, 2, 2, 2, 2]
# """


def moveElementToEnd(arr,n):
    pointL = 0
    pointR = len(arr)-1

    while pointR > pointL:
        while pointR > pointL and arr[pointR] == n:
            pointR -= 1
        if arr[pointL] == n:
            swapPositions(arr,pointL,pointR)
        pointL += 1
    return arr

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))