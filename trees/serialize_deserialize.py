'''
Serialization is the process of converting a data structure or object into a sequence 
of bits so that it can be stored in a file or memory buffer, or transmitted across a 
network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this 
string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Note: Do not use class member/global/static variables to store states. 
Your serialize and deserialize algorithms should be stateless.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        stack = [root]
        serial = ''
        while stack:
            root = stack.pop()
            if not root:
                serial += 'None,'
            else:
                serial += str(root.val) + ','
                stack.append(root.right)
                stack.append(root.left)    
        
        return serial
    
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def get_root(data_list):
            """Recursively build the tree using preorder values"""
            if data_list[0] == 'None':
                data_list.popleft()
                return 
            
            root = TreeNode(data_list.popleft())
            root.left = get_root(data_list)
            root.right = get_root(data_list)
            
            return root
        
        if not data:
            return 
        
        data_list = deque(data.split(','))
        return get_root(data_list)
        
            
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
