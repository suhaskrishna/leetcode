# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Iterative solution
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        if not head:
            return None
        
        node = root
        st = [root]
        s = 0
        visited = set()
            
        while st:
            node = st[-1]
            
            while node.right and node.right not in visited:
                visited.add(node.right)
                st.append(node.right)
                node = node.right
            
            node = st.pop()
            s += node.val
            node.val = s
            
            if node.left:
                st.append(node.left)
        
        return head

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Recursive solution
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        
        def helper(node):
            if node:
                helper(node.right)
                self.total += node.val
                node.val = self.total
                helper(node.left)
            return node
        
        return helper(root)