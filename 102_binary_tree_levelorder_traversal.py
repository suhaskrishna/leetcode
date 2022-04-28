# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    #using BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = queue.Queue()
        q.put(root)
        
        while q.qsize() > 0:
            size = q.qsize()
            res.append([])
            
            while size > 0:
                node = q.get()
                
                res[-1].append(node.val)
                
                if node.left:
                    q.put(node.left)
                
                if node.right:
                    q.put(node.right)
                    
                size -= 1
                
        return res

    #Using DFS
    def levelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def helper(root, level):
            if not root:
                return
            
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)
            
            helper(root.left, level+1)
            helper(root.right, level+1)
        
        helper(root, 0)
        return res
        