class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        
        def findParent(u):
            if u == parent[u]:
                return u
            parent[u] = findParent(parent[u])
            return parent[u]
        
        def merge(u, v):
            if size[u] >= size[v]:
                parent[v] = u
                size[u] += size[v]
            else:
                parent[u] = v
                size[v] += size[u]
        
        for i in range(n):
            for j, val in enumerate(isConnected[i]):
                if i == j or val == 0:
                    continue
                
                p1 = findParent(i)
                p2 = findParent(j)
                
                if p1 != p2:
                    merge(p1, p2)
        
        res = 0
        for i, val in enumerate(parent):
            if i == val:
                res += 1
                
        return res
                
                