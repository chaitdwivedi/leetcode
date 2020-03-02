'''
Find First and Last Postion of Element in Sorted Array
-----------------------------------------------------
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bsearch(nums, target, mode='left'):
            index = -1
            start, end  = 0, len(nums) - 1
            while start <= end:
                mid = start + int((end - start)/2)
                if nums[mid] == target:
                    index = mid

                    if mode == 'left':
                        end = mid - 1
                    else:
                        start = mid + 1

                elif target < nums[mid]:
                    end = mid -1

                elif target > nums[mid]:
                    start = mid + 1
            return index

        return [bsearch(nums, target, 'left'), bsearch(nums, target, 'right')]
