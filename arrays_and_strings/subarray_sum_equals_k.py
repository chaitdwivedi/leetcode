'''
Given an array of integers and an integer k, you need to find the total number
of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000]
 and the range of the integer k is [-1e7, 1e7].
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum_ = 0, 0
        # init with 0:1 for case where number itself is equal to k
        hashmap = {0: 1}

        # iterate over array of sums
        # store previous sums in a hashmap
        for num in nums:
            sum_ += num
            if (sum_ - k) in hashmap:
                count += hashmap[sum_ - k]

            hashmap[sum_] = hashmap[sum_] + 1 if sum_ in hashmap else 1

        return count
