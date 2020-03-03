'''
Interval List Intersections
---------------------------

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
'''
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        intervals = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            low_A, high_A = A[i]
            low_B, high_B = B[j]
            low, high = max(low_A, low_B), min(high_A, high_B)

            if low <= high:
                intervals.append([low, high])

            # skip the intevals that won't occur in future
            if high_A < high_B:
                i += 1
            else:
                j += 1

        return intervals
