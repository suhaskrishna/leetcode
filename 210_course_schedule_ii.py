from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        graph = [[] for _ in range(numCourses)]
        vis = [0 for _ in range(numCourses)]
        res = []
        
        for req in prerequisites:
            cur, pre = req
            graph[pre].append(cur)
        
        def dfs(src):
            vis[src] = 1
            
            for node in graph[src]:
                if vis[node] == 0:
                    isCycle = dfs(node)
                    
                    if isCycle:
                        return True
                elif vis[node] == 1:
                    return True
            
            vis[src] = 2
            res.append(src)
            return False
        
        for i in range(numCourses):
            if vis[i] == 0:
                isCycle = dfs(i)
                
                if isCycle:
                    return []
        
        return res[::-1]