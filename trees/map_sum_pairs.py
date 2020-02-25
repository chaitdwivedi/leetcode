'''
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). 
The string represents the key and the integer represents the value. 
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, 
and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
'''
class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.sum_ = 0
        
    def insert(self, key: str, val: int) -> None:
        node = self 
        for char in key:
            trie = node.trie
            if char not in trie:
                trie[char] = MapSum()
            node = trie[char]
        
        node.sum_ = val
        
    def sum(self, prefix: str) -> int:
        output = 0 
        node = self
        for char in prefix:
            trie = node.trie
            node = trie.get(char)
            if not node:
                return 0
            
        stack = [node]
        while stack:
            cur = stack.pop()
            output += cur.sum_
            stack.extend(cur.trie.values())
       
        return output

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
