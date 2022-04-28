# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal maxDiameter
            if not root:
                return 0
            
            lh = helper(root.left)
            rh = helper(root.right)
            
            maxDiameter = max(maxDiameter, lh+rh)
            return max(lh, rh) + 1
            
        maxDiameter = 0
        helper(root)
        return maxDiameter
        
        