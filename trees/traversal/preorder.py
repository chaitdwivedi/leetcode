'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive
    def rec_preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, order):
            if not root:
                return

            order.append(root.val)
            helper(root.left, order)
            helper(root.right, order)

        order = []
        helper(root, order)
        return order

    # iterative
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        order = []
        while stack:
            current = stack.pop()
            order.append(current.val)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return order
