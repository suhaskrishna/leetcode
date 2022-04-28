# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def helper(root):
            if not root:
                res.append('#')
                return
            
            res.append(str(root.val))
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        def helper(l):
            if len(l) == 0:
                return None
            
            val = l.pop(0)
            
            if val == '#':
                return None
            
            root = TreeNode(val)
            root.left = helper(l)
            root.right = helper(l)
            
            return root
        
        return helper(l)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))