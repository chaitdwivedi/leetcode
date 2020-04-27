'''
Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # starting from right most
        # if you are at last position that means you can reach
        last_good_position = len(nums) - 1
        index = len(nums) - 1

        while index >= 0 :
            max_jump = index + nums[index]
            # if max jump is more than last_good_position
            # update last good position to current index
            if max_jump >= last_good_position:
                last_good_position = index
            index -= 1

        # if last_good_postion is first index 
        # that means jump is possible
        return last_good_position == 0
