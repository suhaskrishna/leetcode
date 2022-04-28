class Solution:
    def checkEqualTree(self, root) -> bool:
        if root is None:
            return False
        
        leftSum = self.calculateSum(root.left)
        rightSum = self.calculateSum(root.right)
        
        if leftSum+root.val == rightSum or rightSum+root.val == leftSum:
            return True
        
        return False
        
    def calculateSum(self, root):
        count = 0
        if root is None:
            return count
        
        count = root.val + self.calculateSum(root.left) + self.calculateSum(root.right)
        return count