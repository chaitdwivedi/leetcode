'''
Decode Ways
-----------
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
class Solution:
    def numDecodings_rec(self, s: str) -> int:
        '''Plain recursive solution - time limit exceeds'''
        def helper(s, pointer):
            if pointer >= len(s):
                return 1

            decodepointer_1 = pointer + 1
            decodepointer_2 = pointer + 2
            result = 0

            # At every point you can either have a single digit or double digit decoding
            # if single digit move the pointer by 1
            # if double digit move the pointer by 2
            if decodepointer_1 <= len(s):
                single = int(s[pointer:decodepointer_1])
                if single >= 1:
                    result += helper(s, pointer + 1)

            if decodepointer_2 <= len(s):
                double = int(s[pointer:decodepointer_2])
                if double >= 10 and double <= 26:
                    result += helper(s, pointer + 2)

            return result

        return helper(s, 0)

    def numDecodings_cached(self, s: str) -> int:
        '''Recursive solution with cached calls using dp array'''
        def helper(s, pointer, dp):
            if pointer >= len(s):
                return 1

            # reduce work by using dp array
            if dp[pointer]:
                return dp[pointer]

            decodepointer_1 = pointer + 1
            decodepointer_2 = pointer + 2
            result = 0

            if decodepointer_1 <= len(s):
                single = int(s[pointer:decodepointer_1])
                if single >= 1:
                    result += helper(s, pointer + 1, dp)

            if decodepointer_2 <= len(s):
                double = int(s[pointer:decodepointer_2])
                if double >= 10 and double <= 26:
                    result += helper(s, pointer + 2, dp)

            dp[pointer] = result
            return result

        dp = [None] * len(s)
        return helper(s, 0, dp)

    def numDecodings(self, s: str) -> int:
        '''Best single pass solution'''
        output = [0] * (len(s)+1)
        output[0] = 1
        output[1] = 1 if int(s[0]) > 0 else 0
        i = 2
        while i <= len(s):
            single = s[i-1:i]
            double = s[i-2:i]

            if int(single) >= 1:
                output[i] += output[i-1]

            if int(double) >= 10 and int(double) <= 26:
                output[i] += output[i-2]
            i += 1

        return output[-1]

