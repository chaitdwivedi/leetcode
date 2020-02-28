'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
2 - abc
3 - def
4 - ghi 
5 - jkl
6 - mno
7 - pqrs
8 - tuv
9 - wxyz
0 - ' '

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
'''
class Solution:
    def __init__(self):
        self.hashmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' '],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        '''simple recursive solution'''
        def mult(array_1, array_2):
            result = []
            for item in array_1:
                result.extend([item+v for v in array_2])
            return result

        def combine(digits):
            if len(digits) == 1:
                return self.hashmap[digits]
            if len(digits) == 2:
                return mult(self.hashmap[digits[0]], self.hashmap[digits[1]])
            return mult(self.hashmap[digits[0]], combine(digits[1:]))

        if not digits:
            return []

        return combine(digits)

    def letterCombinations(self, digits: str) -> List[str]:
        '''Solution with memoization'''
        def mult(array_1, array_2):
            result = []
            for item in array_1:
                result.extend([item+v for v in array_2])
            return result 
        
        def combine(digits):
            if digits in self.hashmap:
                return self.hashmap[digits]
            
            if len(digits) == 2:
                return mult(self.hashmap[digits[0]], self.hashmap[digits[1]])
            
            key = ''.join(sorted(digits))
            self.hashmap[key] = mult(self.hashmap[digits[0]], combine(digits[1:]))
            return self.hashmap[key]
        
        if not digits:
            return []
        
        return combine(digits)
