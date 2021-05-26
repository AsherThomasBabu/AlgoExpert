# Question from leetcode

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# <------- Runs in O(nlogN) ------->

def longestConsecutive(nums):
    if not nums:
        return 0

    nums.sort()

    count = 1
    maxCount = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 1
    return max(count, maxCount)


print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
