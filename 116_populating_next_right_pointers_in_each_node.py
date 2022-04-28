"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        q = deque([root])
        
        while len(q) > 0:
            l = len(q)
            
            while l > 0:
                node = q.popleft()
                l -= 1
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                if l > 0:
                    node.next = q[0]
                else:
                    node.next = None
                    
        return root
                
                
            
        