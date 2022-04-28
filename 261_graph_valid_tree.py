class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        
        def findParent(u):
            if u == parent[u]:
                return u
            parent[u] = findParent(parent[u])
            return parent[u]
        
        def merge(p1, p2):
            if size[p1] >= size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]
        
        for u, v in edges:
            p1 = findParent(u)
            p2 = findParent(v)
            
            if p1 == p2:
                return False
            else:
                merge(p1, p2)
        
        res = 0
        for i, val in enumerate(parent):
            if i == val:
                res += 1
        
        return True if res == 1 else False
        
        
        
        