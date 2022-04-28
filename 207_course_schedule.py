from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(graph, src, vis):
            vis[src] = 1
            
            for node in graph[src]:
                if vis[node] == 0:
                    isCycle = dfs(graph, node, vis)
                    if isCycle:
                        return True
                elif vis[node] == 1:
                    return True
            
            vis[src] = 2
            
            return False
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        vis = [0 for _ in range(numCourses)]
        
        for req in prerequisites:
            graph[req[1]].append(req[0])
            indegree[req[1]] += 1
        
        
        for i in range(numCourses):
            if vis[i] == 0:
                isCycle = dfs(graph, i, vis)
                if isCycle:
                    return False
        
        return True
        
        