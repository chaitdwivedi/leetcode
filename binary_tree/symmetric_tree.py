'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(root1, root2):
            # if both are none
            if not root1 and not root2:
                return True

            # if one of the nodes is none
            if not root1 or not root2:
                return False

            # compare values and then compare left vs right and right vs left
            # of the two parts of the tree
            return (
                root1.val == root2.val and
                isMirror(root1.left, root2.right) and
                isMirror(root1.right, root2.left)
            )

        return isMirror(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)
        queue.append(root)

        while queue:
            root1 = queue.popleft()
            root2 = queue.popleft()

            if not root1 and not root2:
                continue

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            queue.append(root1.left)
            queue.append(root2.right)

            queue.append(root1.right)
            queue.append(root2.left)

        return True