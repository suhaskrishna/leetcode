"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        queue = deque([root])
        
        while len(queue) > 0:
            l = len(queue)
            temp = []
            while l > 0:
                node = queue.popleft()
                temp.append(node.val)
                l-= 1
                
                for child in node.children:
                    queue.append(child)
                
            res.append(temp)
        
        return res
        