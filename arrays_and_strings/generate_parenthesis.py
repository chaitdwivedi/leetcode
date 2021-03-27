'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

class Solution:
    '''
    The idea is simple:
    * For every step in process we have 2 choices: 
            * either we can open a bracket 
            * or we can close a bracket 
    * Depending on the current status we can determine if we open or close or both - `get_choices`
            * if number of opened brackets are less that n - we can stil open more brackets 
            * if number of closed brackets are less than n - we can still close brackets 
                    * However, we can only close after we've opened 
    * Using template backtracking algorithm to iterate of all valid choices recursively 
    * Keeping track of opened and closed bracket with help of `update` function 
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        def get_choices(opened, closed):
            choices = []
            if opened < n:
                choices.append("(")
           
            if closed < n and closed < opened:
                choices.append(")")
            
            return choices
        
        def update(opened, closed, bracket, op):
            val = 1 if op == "+" else -1
            if bracket == "(":
                opened = opened + val
    
            if bracket == ")":
                closed = closed + val 
        
            return opened, closed
                
        
        def backtrack(opened, closed, pattern):
       
            if len(pattern) == 2 * n:
                result.append("".join(pattern))
                return 
            
            choices = get_choices(opened, closed)
            for bracket in choices:
                pattern.append(bracket)
                opened, closed = update(opened, closed, bracket, "+")
                backtrack(opened, closed, pattern)
                popped_bracket = pattern.pop()
                opened, closed = update(opened, closed, popped_bracket, "-")
            
            
        result = []
        backtrack(opened=1, closed=0, pattern=["("])
        return result 
