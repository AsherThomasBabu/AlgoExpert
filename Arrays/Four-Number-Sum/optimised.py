# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.


def fourSum(nums,target):
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left = j+1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target and sorted([nums[i] , nums[j] , nums[right] , nums[left]]) not in result:
                        result.append(sorted([nums[i] , nums[j] , nums[right] , nums[left]]))
                        left += 1
                        right -= 1
                    elif sum<target:
                        left+=1
                    else:
                        right-=1
        return result