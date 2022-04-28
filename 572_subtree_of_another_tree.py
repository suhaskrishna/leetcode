# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            
            if root1 is None or root2 is None:
                return False
            
            return root1.val == root2.val and isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
        
        def dfs(root, subRoot):
            if not root:
                return False
            
            if root.val == subRoot.val:
                if(isSame(root, subRoot)):
                    return True
                
            leftMatch = dfs(root.left, subRoot)
            rightMatch = dfs(root.right, subRoot)

            return leftMatch or rightMatch
            
        return dfs(root, subRoot)