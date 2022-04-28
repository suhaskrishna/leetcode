class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        
        def findParent(u):
            if u == parent[u]:
                return u
            
            return findParent(parent[u])
        
        def merge(p1, p2):
            if size[p1]>=size[p2] :
                parent[p2]=p1
                size[p1]+=size[p2]
            else:
                parent[p1]=p2
                size[p2]+=size[p1]
        
        for edge in edges:
            u=edge[0]-1
            v=edge[1]-1
            
            p1=findParent(u)
            p2=findParent(v)
            
            if(p1!=p2):
                merge(p1,p2)
            else:
                return edge

        return []