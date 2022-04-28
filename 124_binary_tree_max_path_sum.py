# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxGain(root):
            if root is None:
                return 0
            
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)
            
            curGain = root.val + leftGain + rightGain
            
            self.maxSum = max(self.maxSum, curGain)
            
            return root.val + max(leftGain, rightGain)
            
        
        self.maxSum = float("-inf")
        maxGain(root)
        return self.maxSum