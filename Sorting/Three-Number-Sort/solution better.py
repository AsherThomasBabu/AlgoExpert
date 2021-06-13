# You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain Integers that are in the second array, and the second array represents a desired order for the integers in the first array. For example, a second array of [x, y, z] represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] In the first array.

# Write a function that sorts the first array according to the desired order in the second array.
# The function should perform this in place (l.e., It should mutate the input array), and it shouldn't use any auxiliary space (l.e., It should run with constant space: 0(1) space).

# Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all three Integers found in the second array-It might only contain one or two.

# Keeping track of the indices where the values are supposed to be stored. Runs the loop only once


def threeNumberSort(array, order):
    f,s,t = 0,0,len(array)-1
    one, two, three = order
    
    while s <= t:
        if array[s] == one:
            swap(array,s,f)
            f += 1
            s += 1
        elif array[s] == two:
            s += 1
        else:
            swap(array,s,t)
            t -= 1
    return array

def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]
print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1],[0, 1, -1]))