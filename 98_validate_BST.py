class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = []
        prev = float("-inf")
        node = root
        
        while len(st) > 0 or node != None:
            while node != None:
                st.append(node)
                node = node.left
            
            node = st.pop()
            if node.val <= prev:
                return False
            
            prev = node.val
            node = node.right
        
        return True