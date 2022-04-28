#Using array

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inOrderBST = []
        self.iterIdx = -1
        self.buildInOrder(root)
        
    def buildInOrder(self, root):
        if root == None:
            return 
        
        self.buildInOrder(root.left)
        self.inOrderBST.append(root.val)
        self.buildInOrder(root.right)
        
    def next(self) -> int:
        self.iterIdx += 1
        return self.inOrderBST[self.iterIdx]

    def hasNext(self) -> bool:
        if self.iterIdx+1 >= len(self.inOrderBST):
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


#Using recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftMost_inorder(root)
    
    def _leftMost_inorder(self, root):
        while root != None:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        node = self.stack.pop()
        
        if node.right != None:
            self._leftMost_inorder(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()