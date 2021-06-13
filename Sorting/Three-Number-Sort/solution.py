# You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain Integers that are in the second array, and the second array represents a desired order for the integers in the first array. For example, a second array of [x, y, z] represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] In the first array.

# Write a function that sorts the first array according to the desired order in the second array.
# The function should perform this in place (l.e., It should mutate the input array), and it shouldn't use any auxiliary space (l.e., It should run with constant space: 0(1) space).

# Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all three Integers found in the second array-It might only contain one or two.

def threeNumberSort(array, order):
    count = 0
    for i in order:
        for j in range(len(array)):
            if array[j] == i:
                array[j],array[count] = array[count],array[j]
                count += 1
    return array


print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1],[0, 1, -1]))