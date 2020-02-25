'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec_maxDepth(self, root: TreeNode) -> int:
        '''bottom-up solution'''
        if not root:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

    def maxDepth(self, root: TreeNode) -> int:
        '''using stack'''
        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]
        while stack:
            root, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if root.left:
                stack.append((root.left, depth + 1))
            if root.right:
                stack.append((root.right, depth + 1))

        return max_depth