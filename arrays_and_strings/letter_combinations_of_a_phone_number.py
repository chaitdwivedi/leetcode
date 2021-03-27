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


####################
#
# Alternate Solution 
#
####################


def combine(arr1, arr2):
    combined = []
    for item1 in arr1:
        for item2 in arr2:
            combined.append(f"{item1}{item2}")
    return combined
    
class Solution:
    def __init__(self):
        self.phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        if digits in self.phone:
            return self.phone[digits]
    
        combined = combine(self.phone[digits[0]], self.letterCombinations(digits[1:]))
        self.phone[digits] = combined
        return combined


####################
#
# Backtrack Solution 
#
####################

class Solution:
    def __init__(self):
        self.phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        
        def backtrack(index, combination=[]):
            if len(combination) == len(digits):
                combination = "".join(combination)
                results.append(combination)
                return 
            
            for letter in self.phone[digits[index]]:
                combination.append(letter)
                backtrack(index + 1, combination)
                combination.pop()
            
            
        if not digits:
                return []
            
        results = []    
        backtrack(index=0, combination=[])
        return results 
        
