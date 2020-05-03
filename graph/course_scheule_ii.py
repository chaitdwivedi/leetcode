'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
from collections import defaultdict 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build dependency graph
        graph = defaultdict(list)
        for deps in prerequisites:
            graph[deps[0]].append(deps[1])
        
        visited = [False] * numCourses
        resolved = [False] * numCourses
        resolution_order = []
        
        for i in range(numCourses):
            stack = [i]
            while stack:
                top = stack[-1]
                if graph[top] and not visited[top]:
                    for deps in graph[top]:
                        if visited[deps] and not resolved[deps]:
                            return []
                        stack.append(deps)
                    visited[top] = True
                else:
                    # to handle duplicates
                    if not resolved[top]:
                        resolved[top] = True 
                        resolution_order.append(top)
                    stack.pop()
        
        return resolution_order
        
