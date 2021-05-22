# Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n = m) and returns a one-dimensional
# array of all the array's elements in spiral order.
# Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until
# every element has been visited.

# """
# Q. Traverse the mxn Array in spiral order and return the resultant array.
# Case 1:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Case 2:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Case 3:
# [
#   [7],
#   [9],
#   [6]
# ]
# Output: [7,9,6]
# """

def spiralTraverse(array):
    result = []
    startCol, endCol = 0, len(array[0]) - 1
    startRow, endRow = 0, len(array) - 1

    spiral(array, startCol, endCol, startRow, endRow, result)
    
    return result


def spiral(array, startCol, endCol, startRow, endRow, result):
    if startCol > endCol or startRow > endRow:
        return

    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
        if startRow == endRow:
            break
        result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        if startCol == endCol:
            break
        result.append(array[row][startCol])

    spiral(array, startCol+1, endCol-1, startRow+1, endRow -1, result)


print(spiralTraverse([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))
