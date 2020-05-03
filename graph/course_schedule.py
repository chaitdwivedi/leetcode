'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
'''
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        # build dependency graph 
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        
        visited = [False] * numCourses
        resolved = [False] * numCourses
        
        # perform dfs for each node 
        for i in range(numCourses):
            stack = [i]
            while stack:
                top = stack[-1]
                if graph[top] and not visited[top]:
                    for deps in graph[top]:
                        if visited[deps] and not resolved[deps]:
                            return False
                        if not visited[deps]:
                            stack.append(deps)
                    visited[top] = True
                else:
                    resolved[top] = True 
                    stack.pop()
        
        return True
                    
