'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
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
    def rec_inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, order):
            if not root:
                return

            helper(root.left, order)
            order.append(root.val)
            helper(root.right, order)

        order = []
        helper(root, order)
        return order

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        order = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            order.append(root.val)
            root = root.right

        return order