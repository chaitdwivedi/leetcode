'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict
class Solution:
    def map_levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''solution using map as extra mem to store level'''
        if not root:
            return []

        queue = deque()

        queue.append((root, 0))

        order = defaultdict(list)
        while queue:
            current, current_level = queue.popleft()
            order[current_level].append(current.val)

            if current.left:
                queue.append((current.left, current_level + 1))
            if current.right:
                queue.append((current.right, current_level + 1))

        return list(order.values())


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''solution without extra map'''
        if not root:
            return []

        queue = deque()
        queue.append(root)
        order = []

        while queue:
            # current lenght of queue will determine number of items in that level
            current_len = len(queue)
            level = []
            # traverse nodes in the same level
            for i in range(current_len):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            order.append(level)

        return order