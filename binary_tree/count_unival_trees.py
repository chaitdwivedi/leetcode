'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def isUnival(root):
            if not root:
                return True

            left, right = isUnival(root.left), isUnival(root.right)

            if (left and right) and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
                self.count += 1
                return True

            return False

        self.count = 0
        isUnival(root)
        return self.count
