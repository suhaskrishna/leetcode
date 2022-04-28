# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            count = 0
            if not root:
                return 0
            
            if root.val >= low and root.val <= high:
                count += root.val
            
            return count + helper(root.left) + helper(root.right)
        
        return helper(root)