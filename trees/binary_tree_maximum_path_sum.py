'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # set initial max to negative to system max size
        self.max_sum = -sys.maxsize

    def maxPathSum(self, root: TreeNode) -> int:
        def get_max(node):
            """Search for max path for given node and update global max

            - Find max of these 4 cases:
            -- node
            -- node + left
            -- node + right
            -- node + left + right

            for left and right calculation use recursion

            - Update global max with this value

            Return max of only first 3 cases - becasue 4th case marks top of the tree
            If both children of node are added - then it can't be connected to caller

            :param node: current node to calculate
            :type node: TreeNode
            :returns: max path that can be continued
            :rype: int
            """
            if not node:
                return 0


            left = get_max(node.left)
            right = get_max(node.right)

            cases = [
                    node.val,                      # when node is the best case
                    node.val + left,               # when left path is chosen
                    node.val + right,              # when right parth is chosen
                    node.val + left + right,       # top of the tree case - this cannot be part of any other path
                ]

            self.max_sum = max(self.max_sum, max(cases))

            return max(cases[0:3])

        get_max(root)
        return self.max_sum


