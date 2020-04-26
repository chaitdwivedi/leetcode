'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left, right = 0, 0
        cur_len, max_len = 0, 0

        while right < len(s):
            if s[right] in seen:
                left = max(seen[s[right]] + 1, left)
            seen[s[right]] = right

            cur_len = right - left + 1
            right = right + 1
            max_len = cur_len if cur_len > max_len else max_len

        return max_len
