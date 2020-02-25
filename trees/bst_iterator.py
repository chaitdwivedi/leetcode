'''
Implement an iterator over a binary search tree (BST). 
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.


Example:
  7
 / \
3  15
   / \
  9   20

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.

You may assume that next() call will always be valid, that is, 
there will be at least a next smallest number in the BST when next() is called.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Easy O(n) space
class BSTIterator_On:

    def __init__(self, root: TreeNode):
        self.sorted = []
        self._inorder(root)
        # or call iterative
        # self._inorder_iterative(root)
        self.current = 0 
    
    # recursive
    def _inorder(self, root):
        if not root:
            return 
        self._inorder(root.left)
        self.sorted.append(root.val)
        self._inorder(root.right)
        
    # iterative 
    def _inorder_iterative(self, root):
        if not root:
            return []
        
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            
            root = stack.pop()
            self.sorted.append(root.val)
            root = root.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.sorted[self.current]
        self.current += 1 
        return val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.current < len(self.sorted)


# using custom stack implemention 
# max stack size is that of the height of the tree
# O(h)
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._fill_stack(root)
   
    def _fill_stack(self, root):
        '''Fill stack all left childs - top item will be smallest'''
        while root:
            self.stack.append(root)
            root = root.left
            
    def next(self):
        root = self.stack.pop()
        val = root.val 
        # fill stack for left branch of right child
        self._fill_stack(root.right)
        return val
        
    
    def hasNext(self):
        if self.stack:
            return True 
        return False

# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
