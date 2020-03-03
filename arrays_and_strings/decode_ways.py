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
    def numDecodings(self, s: str) -> int:
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
