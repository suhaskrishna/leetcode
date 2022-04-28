# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Expensive initialization
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def inorder(node):
            if node:
                return inorder(node.left) + [node.val] + inorder(node.right)
            
            return []
        self.array = inorder(root)
        self.n = len(self.array)
        self.curPtr = -1

    def hasNext(self) -> bool:
        return self.curPtr < self.n-1


    def next(self) -> int:
        self.curPtr += 1
        return self.array[self.curPtr]

    def hasPrev(self) -> bool:
        return self.curPtr > 0

    def prev(self) -> int:
        self.curPtr -= 1
        return self.array[self.curPtr]

# Efficient initialization
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.array = []
        self.stack = []
        self.last = root
        
        self.n = len(self.array)
        
        self.curPtr = -1

    def hasNext(self) -> bool:
        return self.stack or self.last or self.curPtr < len(self.array)-1


    def next(self) -> int:
        self.curPtr += 1
        
        if self.curPtr == len(self.array):
            while self.last:
                self.stack.append(self.last)
                self.last = self.last.left
            
            cur = self.stack.pop()
            self.last = cur.right
        
            self.array.append(cur.val)
        
        return self.array[self.curPtr]

    def hasPrev(self) -> bool:
        return self.curPtr > 0

    def prev(self) -> int:
        self.curPtr -= 1
        return self.array[self.curPtr]
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()