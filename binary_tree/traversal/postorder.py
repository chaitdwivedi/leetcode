'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec_postorderTraversal(self, root: TreeNode) -> List[int]:
        '''recursive solution'''
        def helper(root, order):
            if not root:
                return

            helper(root.left, order)
            helper(root.right, order)
            order.append(root.val)

        order = []
        helper(root, order)
        return order

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''iterative solution'''
        if not root:
            return []
        stack = [root]
        order = []

        # do opposite of pre order
        while stack:
            root = stack.pop()
            order.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return reversed(order)