'''
3Sum 
----
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        def two_sum(nums, cur_index, target):
            res = []
            diff = set()
            seen = set()
            for index, num in enumerate(nums):
                if num not in seen:
                    if index > cur_index:
                        req = target - num 
                        if req in diff:
                            seen.add(num)
                            res.append([nums[cur_index], req, num])
                        else:
                            diff.add(num)
            return res 
        
        def two_sum_sorted(nums, cur_index, target):
            left = cur_index + 1 
            right = len(nums) - 1
            result = []
            
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    result.append([nums[cur_index], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                            
                    left += 1
                    right -= 1 
                elif total < target:
                    left += 1 
                else:
                    right -= 1
            
            return result
                        
        nums.sort()
        result = []
        i = 0 
        while i < len(nums):
            twosum = two_sum_sorted(nums=nums, cur_index=i, target=0-nums[i])
            result.extend(twosum)
            # skip all dups
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
                    
        return result
