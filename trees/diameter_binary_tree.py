'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''Diameter of binary tree is maximum of:
        o Diameter of left subtree 
        o Diameter of right subtree
        o Max path between leaves that passes through root 
          - this is found using height of left subtree + height of right subtree
        '''
        def get_height(root):
            '''return height of a tree'''
            if not root:
                return 0

            return 1 + max(get_height(root.left), get_height(root.right))

        if not root:
            return 0
        
        diameter_left = self.diameterOfBinaryTree(root.left)
        diameter_right = self.diameterOfBinaryTree(root.right)

        height_left = get_height(root.left)
        height_right = get_height(root.right)

        return max(max(diameter_left, diameter_right), (height_left + height_right))


