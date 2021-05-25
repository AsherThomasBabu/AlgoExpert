# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# <---- Runs in O(n) ---->

def subarraySort(array):
    if len(array) < 2:
        return [-1,-1]
    res = [-1,-1]

    minUnsorted = array[0]
    for i in range(len(array)):
        if array[i] < minUnsorted:
            res[1] = i
        else:
            minUnsorted = array[i]


    maxUnsorted = array[-1]
    for i in reversed(range(len(array))):
        if maxUnsorted < array[i]:
            res[0] = i
        else:
            maxUnsorted = array[i]

    return res