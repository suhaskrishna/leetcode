# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:            

    #If the result order doesn't matter
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, level):
            if not root:
                return
            
            if level not in res:
                res[level] = [root.val]
            else:
                res[level].append(root.val)
            
            helper(root.left, level-1)
            helper(root.right, level+1)
            
        res = {}
        helper(root, 0)
        
        ans = []
        for key in sorted(res):
            ans.append(res[key])
        
        return ans