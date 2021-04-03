'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''easy solution using sorting'''
        nums = list(set(nums))
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        nums.sort()

        start = 0
        max_range = 1

        # result = []
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1] + 1:
                current_range = index - start + 1
                if current_range > max_range:
                    max_range = current_range
                    # result = [nums[start], nums[index]]
            else:
                start = index

        return max_range

