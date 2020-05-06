'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def build_graph(equations, values):
            '''Create edge a -> b:val and edge b -> a:1/val'''
            graph = defaultdict(list)
            for index in range(len(equations)):
                src, dest = equations[index]
                value = values[index]

                graph[src].append((dest, value))
                graph[dest].append((src, 1/value))
                
            return graph  
       
        def get_val(graph, src, dest):
            if src not in graph or dest not in graph: 
                return -1.0
            
            if src == dest:
                return 1.0 
           
            visited = set()
            q = deque()
            q.append((src, 1.0))
            while q:
                current, current_val = q.popleft()
                if current == dest:
                    return current_val 
                if current not in visited:
                    visited.add(current) 
                    for conn, conn_val in graph[current]:
                        q.append((conn, current_val * conn_val))
         
            return -1.0

        graph = build_graph(equations, values)        
        return [get_val(graph, src, dest) for src, dest in queries]
            
