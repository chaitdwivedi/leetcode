'''
Given a 01 matrix M, find the longest line of consecutive one in the matrix. 
The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
'''
from collections import defaultdict
class dfs_Solution:
    '''DFS solution using memoization'''
    def longestLine(self, M: List[List[int]]) -> int:

        def get_path(M, i, j, cache, direction):

            if i < 0 or j < 0 or i >= len(M) or j >= len(M[0]):
                return 0
           
            key = '%s_%d_%d' % (direction, i, j) 
            if key in cache:
                return cache[key]
                
            
            left, right = i-1, i+1 
            up, down = j+1, j-1
            path = -1
            # left
            if direction == 'left' and left >= 0 and M[left][j] == 1:
                path = 1 + get_path(M, left, j, cache, direction)
            
            # right
            if direction == 'right' and right < len(M) and M[right][j] == 1:
                path = 1 + get_path(M, right, j, cache, direction)
            
            # up
            if direction == 'up' and up < len(M[0]) and M[i][up] == 1:
                path = 1 + get_path(M, i, up, cache, direction)
            
            # down
            if direction == 'down' and down >= 0 and M[i][down] == 1:
                path = 1 + get_path(M, i, down, cache, direction)
            
            # left-up
            if direction == 'left-up' and left >= 0 and up < len(M[0]) and M[left][up] == 1:
                path = 1 + get_path(M, left, up, cache, direction)
            
            # right-up
            if direction == 'right-up' and right < len(M) and up < len(M[0]) and M[right][up] == 1:
                path = 1 + get_path(M, right, up, cache, direction)
            
            # left-down
            if direction == 'left-down' and left >= 0 and down >= 0 and M[left][down] == 1:
                path = 1 + get_path(M, left, down, cache, direction)
            
            # right-down 
            if direction == 'right-down' and right < len(M) and down >= 0 and M[right][down] == 1:
                path  = 1 + get_path(M, right, down, cache, direction)
           
            max_val = max(path, 1)
            cache[key] = max_val
            return max_val   
    
            
        cache = {}
        longest_path = 0 
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    for dir_ in ['left', 'right', 'up', 'down', 'left-up', 'left-down', 'right-down', 'right-up']:
                        path = get_path(M, i, j, cache, dir_)
                        longest_path = max(longest_path, path)
        
        return longest_path
   

class iterative_Solution:
    '''Simple iterative solution'''
    def longestLine(self, M: List[List[int]]) -> int:
        def get_count(array):
            '''Return maximum consequtive 1s in a array'''
            max_count, count = 0, 0
            for i in array:
                if i == 1:
                    count += 1 
                    max_count = max(max_count, count)
                else:
                    count = 0
            return max_count 
        
        def get_longest(M, mode):
            longest = 0 
            if mode == 'row':
                for row in M:
                    longest = max(get_count(row), longest)
            
            if mode == 'column':
                for j in range(len(M[0])):
                    count = 0 
                    col = [row[j] for row in M]
                    longest = max(get_count(col), longest)
            
            if mode == 'diagonal':
                diags = defaultdict(list)
                for i in range(len(M)):
                    for j in range(len(M[0])):
                        diags[j-i].append(M[i][j])
    
                for diag in diags.values():
                    longest = max(get_count(diag), longest)
            
            if mode == 'anti-diagonal':
                diags = defaultdict(list)
                for i in range(len(M)):
                    for j in range(len(M[0])):
                        diags[j+i].append(M[i][j])
    
                for diag in diags.values():
                    longest = max(get_count(diag), longest)
                
            return longest
                
        if not M:
            return 0 
        
        longest_path = 0
        modes = ['row', 'column', 'diagonal', 'anti-diagonal']
        for mode in modes:
            longest_path = max(longest_path, get_longest(M, mode))
        
        return longest_path
    
    
class Solution:
    '''Dynamic Programming'''
    def longestLine(self, M: List[List[int]]) -> int:   
        if not M:
            return 0 
        
        longest_path = 0
        dp = {}
        modes = ['row', 'column', 'diagonal', 'anti-diagonal']
        for mode in modes:
            dp[mode] = [[0] * len(x) for x in M]
            
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    dp['row'][i][j] = dp['row'][i][j-1] + 1 if j - 1 >= 0 else 1 
                    dp['column'][i][j] = dp['column'][i-1][j] + 1 if i - 1 >= 0 else 1
                    dp['diagonal'][i][j] = dp['diagonal'][i-1][j-1] + 1 if i - 1 >= 0 and j-1>=0 else 1
                    dp['anti-diagonal'][i][j] = dp['anti-diagonal'][i-1][j+1] + 1 if i-1>=0 and j+1<len(M[0]) else 1
                    
                longest_path = max(
                    longest_path, 
                    dp['row'][i][j], 
                    dp['column'][i][j], 
                    dp['diagonal'][i][j], 
                    dp['anti-diagonal'][i][j]
                )
         
        return longest_path
        
