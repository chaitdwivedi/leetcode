'''
Minimum Window Substring
-----------------------
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def get_count_map(inp_str):
            '''Read in a string and build a count map'''
            count_map = {}
            for char in inp_str:
                count_map[char] = count_map[char] + 1 if char in count_map else 1
            return count_map


        def hasT(win_map, t_map):
            '''Check if the given window map has the t sring'''
            for char in t_map:
                if char not in win_map:
                    return False
                elif win_map[char] < t_map[char]:
                    return False
            return True

        def get_min_str(a, b):
            '''Return minimum string of a, b'''
            return a if len(a) < len(b) else b

        if not s or not t:
            return ''

        # build char count map for 't'
        t_map = get_count_map(t)

        left, right = 0, 0
        found = False
        min_str = s
        win_map = {s[0] : 1}
        while right < len(s):
            window = s[left:right+1]
            if hasT(win_map, t_map):
                found = True
                min_str = get_min_str(min_str, window)
                # reduce count of left char from window map
                win_map[s[left]] = win_map[s[left]] - 1
                left += 1
            else:
                right += 1
                if right < len(s):
                    # add count of right char in window map
                    win_map[s[right]] = win_map[s[right]] + 1 if s[right] in win_map else 1

        return min_str if found else ''
