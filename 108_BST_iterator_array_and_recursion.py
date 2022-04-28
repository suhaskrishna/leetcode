# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build(self, nums, si, ei):
        if si > ei:
            return None
        
        if si == ei:
            return TreeNode(nums[si])
        
        mid = (si+ei)//2
        
        root = TreeNode(nums[mid])
        
        root.left = self.build(nums, si, mid-1)
        root.right = self.build(nums, mid+1, ei)
        
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
         return self.build(nums, 0, len(nums)-1)