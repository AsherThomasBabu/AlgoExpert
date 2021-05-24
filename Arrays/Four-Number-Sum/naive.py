# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.


def fourNumberSum(array, targetSum):
    result = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1,len(array)):
                for l in range(k+1,len(array)):
                    sum = array[i] + array[j] + array[k] + array[l]
                    if sum == targetSum and sorted([array[i] , array[j] , array[k] , array[l]]) not in result:
                        result.append(sorted([array[i] , array[j] , array[k] , array[l]]))
    return result