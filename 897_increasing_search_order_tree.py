# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Inorder traversal with relinking
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)
            
        ans = TreeNode(0)
        self.cur = ans
        inorder(root)
        return ans.right

#Inorder traveral with yield
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return None
            
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
            
        ans = cur = TreeNode(0)
        
        for val in inorder(root):
            cur.right = TreeNode(val)
            cur = cur.right
            
        return ans.right