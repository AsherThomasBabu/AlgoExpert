# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Input: mat =    [[1,2,3],
#                 [4,5,6],
#                 [7,8,9]]

# Output: [1,2,4,7,5,3,6,8,9]

def findDiagonalOrder(array):
    height = len(array) - 1
    width = len(array[0]) - 1

    result = []

    row = 0
    col = 0
    
    # TODO
    # Need to do this part, using the constant index sum method (sum of indices of all elements on the diagonal are constant)