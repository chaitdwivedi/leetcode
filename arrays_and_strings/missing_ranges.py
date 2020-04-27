'''
Given a sorted integer array nums, where the range of elements are in the inclusive 
range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        output = []
        nums = [lower-1] + nums + [upper+1]
        current, _next = 0, 1
        while _next < len(nums):
            if nums[_next] - nums[current] > 1:
                if nums[_next] - 1 == nums[current] + 1:
                    output.append(str(nums[_next] - 1))
                else:
                    output.append("{}->{}".format(nums[current]+1, nums[_next]-1))
             
            current += 1
            _next += 1
        return output
