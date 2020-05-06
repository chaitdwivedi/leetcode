'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. 

It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def oldcountNodes(self, root: TreeNode) -> int:
        '''Linear Time'''
        if not root:
            return 0 
        
        stack = [root]
        count = 0 
        while stack:
            current = stack.pop()
            count += 1
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
                
        return count
        
    def countNodes(self, root: TreeNode) -> int:
        '''O(logn * logn)'''
        def get_depth(node):
            if not node:
                return 0 
            return 1 + get_depth(node.left)
        
        if not root:
            return 0 
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
    
        if left_depth == right_depth:  # no need to traverse left tree - its full
            return 2 ** left_depth + self.countNodes(root.right)  # left tree = 2^d - 1 + 1 (root)
        else:
            return 2 ** right_depth + self.countNodes(root.left) # no need to traverse right 
