"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        st = [root]
        res = []
        while len(st) > 0:
            node = st.pop()
            
            for i in range(len(node.children)-1, -1, -1):
                st.append(node.children[i])
            
            res.append(node.val)
        
        return res