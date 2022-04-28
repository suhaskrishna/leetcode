from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(src, vis, res):
            vis[src] = 1
            
            for node in graph[src]:
                if vis[node] == 0:
                    if(dfs(node, vis, res)):
                        return True
                elif vis[node] == 1:
                    return True
            
            vis[src] = 2
            return False
                    
        n = len(graph)
        vis = [0] * n
        
        res = []
        for i in range(n):
            if vis[i] == 0:
                hasCycle = dfs(i, vis, res)
                
                if not hasCycle:
                    res.append(i)
            elif vis[i] == 2:
                res.append(i)
        
        return res