'''
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]


Constraints:

1 <= n <= 14
'''
class Solution:
    '''
    Algorithm

    Handle base cases of 0, 1, 2 using example
    For 3 onwards we need to handle 2 cases
    1: where 0 cannot be placed outside of number
    where 0 can be placed outside of number
    For instance, 010 is invalid as a 3 digit number,
    but valid for "inner" sequence in a 5 digit number
    We can handle this by using "with_zero" flag.
    Once we have result from recursion
    we can simply "wrap" result in the 2 digit pre-determinde combination
    '''
    def findStrobogrammatic(self, n: int) -> List[str]:

        odd = ["0", "1", "8"]
        even = ["11", "69", "88", "96", "00"]
        even_wo_zero = ["11", "69", "88", "96"]

        def generate(n, with_zero=False):
            if n == 0:
                return []

            if n == 1:
                return odd

            if n == 2:
                return even if with_zero else even_wo_zero

            outers = even if with_zero else even_wo_zero
            inners = generate(n - 2, with_zero=True)

            result = []
            for outer in outers:
                for inner in inners:
                    number = outer[:1] + inner + outer[1:]
                    result.append(number)
            return result

        return generate(n)
