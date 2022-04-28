# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def getHeight(root):
            if not root:
                return 0
            
            lh = getHeight(root.left)
            rh = getHeight(root.right)
            
            level = max(lh, rh)
            
            if len(ans) == level:
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            
            return level+1
        
        ans = []
        getHeight(root)
        
        return ans