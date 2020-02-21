'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        '''don't preserve tree and save the sum in val
        this solution destroyes original tree'''

        if not root:
            return False

        stack = []
        stack.append(root)

        # add sums until that point
        while len(stack):
            cur = stack.pop()

            if cur.left:
                cur.left.val += cur.val
                stack.append(cur.left)
            if cur.right:
                cur.right.val += cur.val
                stack.append(cur.right)

            if not cur.right and not cur.left and cur.val == sum:
                return True


        return False

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        '''Use tuple in stack to preserve tree'''

        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            cur, sum_ = stack.pop()
            if cur.left:
                stack.append((cur.left, sum_ + cur.left.val))
            if cur.right:
                stack.append((cur.right, sum_ + cur.right.val))

            # check if leaf node
            if not cur.right and not cur.left and sum_ == sum:
                return True

        return False
