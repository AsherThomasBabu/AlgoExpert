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

    down = True

    while row < height and row > 0 and col > 0 and col < width:
        result.append([array[row][col]])

        if down:
            if col == 0 or row == height:
                down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1

        else:
            if row == 0 or col == width:
                down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result