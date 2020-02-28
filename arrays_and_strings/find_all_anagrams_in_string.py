'''
Find All Anagrams in a String
-----------------------------
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the 
length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def create_map(inp):
            '''Create a map of counts for a given string'''
            map_ = defaultdict(int)
            for char in inp:
                map_[char] += 1
            return map_ 
        
        if not s:
            return []
            
        result = []
        index = 0
        pattern_map, window_map = create_map(p), defaultdict(int)
        
        while index <= len(s) - len(p):
            # create window of length of pattern
            window = s[index:index+len(p)]
            
            # create map if not already created
            if not window_map:
                window_map = create_map(window)
            else:
                # update map with only the new char of window if already created
                window_map[window[-1]] += 1
        
            if window_map == pattern_map:
                result.append(index)
            
            # remove the oldest value - since no longer part of the new window
            window_map[window[0]] -= 1
            
            # remove from map if 0 to help with comparison
            if window_map[window[0]] == 0:
                del window_map[window[0]]
            
            index += 1
            
        return result
        
