'''
Number of Islands 
-----------------

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            '''Perform dfs on graph'''
            grid[i][j] = '0'
            
            up = j - 1 
            down = j + 1 
            right = i + 1 
            left = i - 1
            
            if left >= 0 and grid[left][j] == '1':
                dfs(grid, left, j)
            
            if right < len(grid) and grid[right][j] == '1':
                dfs(grid, right, j)
            
            if up >= 0 and grid[i][up] == '1':
                dfs(grid, i, up)
            
            if down < len(grid[0]) and grid[i][down] == '1':
                dfs(grid, i, down)
    
        if not grid:
            return 0
        
        count = 0  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        
        return count
