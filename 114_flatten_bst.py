# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        
        if root.left == None and root.right == None:
            return root
        
        leftFlatten = self.flatten(root.left)
        rightFlatten = self.flatten(root.right)
        
        if leftFlatten != None:
            temp = leftFlatten
            while temp.right != None:
                temp = temp.right
            temp.right = rightFlatten
            root.left = None
            root.right = leftFlatten
        else:
            root.right = rightFlatten
        
        return root