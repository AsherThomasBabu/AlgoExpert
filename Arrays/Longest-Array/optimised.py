# Question from leetcode

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# <------- Runs in O(N) ------->

def longestConsecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    long_streak = 0
    for num in num_set:
        if num-1 not in num_set:
            curr_num = num
            curr_streak = 1
            while curr_num+1 in num_set:
                curr_num += 1
                curr_streak += 1
            long_streak = max(long_streak, curr_streak)
    return long_streak


print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
