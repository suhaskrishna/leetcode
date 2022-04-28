class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        visited = [False for i in range(n)]
        
        def dfs(node):            
            if node == destination:
                return True

            for v in graph[node]:
                if not visited[v]:
                    visited[v] = True
                    flag = dfs(v)
                    if flag:
                        return True
            
            return False       
        
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited[source] = True
        return dfs(source)