'''
Given a non-empty array containing only positive integers, find if the array can be 
partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def rec_call(index, nums, sum_, target):
            '''Perform a recursive call using current index and the choice made
            For every number in list - choice could be either taken or not taken - 
            represented by either:taken: sum + nums[index] or not taken: sum

            Exit conditions: if sum matches the target sum 
            or if it exceed target sum - meaning - the other half can never be equal to the target
            or we run out of the items in list
            '''
            if sum_ == target:
                return True 
            
            if sum_ > target or index >= len(nums):
                return False
            
            # return rec solution of either making a choice or not making a choice
            return (rec_call(index+1, nums, sum_ + nums[index], target) or rec_call(index+1, nums, sum_, target))
        
        def dp_call(index, nums, sum_, target, dp_map):
            '''Optimize recursive call by using status map or dp map
            status determined by index and sum 
            '''
            current_state = str(index) + " " + str(sum_)
            
            if current_state in dp_map:
                return dp_map[current_state]
            
            if sum_ == target:
                return True 
            
            if sum_ > target or index >= len(nums):
                return False
            
            dp_map[current_state] = (dp_call(index+1, nums, sum_ + nums[index], target, dp_map) or dp_call(index+1, nums, sum_, target, dp_map))
            # return rec solution of either making a choice or not making a choice
            return dp_map[current_state] 
            
        
        sum_ = sum(nums)
        # cannot partition if sum is odd
        if sum_ % 2 != 0:
            return False
       
        # check if a subset is equal to half of total - meaning other half will be same
        target = sum_ / 2 
        return dp_call(index=0, nums=nums, sum_=0, target=target, dp_map={})
