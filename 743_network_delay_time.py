import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for src, dest, wt in times:
            graph[src].append((dest, wt))
        
        maxVal = 0
        
        distance = [float("inf") for _ in range(n+1)]
        distance[k] = 0
        
        queue = [(0, k)]
        
        while queue:
            cost, node = heapq.heappop(queue)
            
            if distance[node] < cost:
                continue
            
            for edge in graph[node]:
                v, w = edge
                
                newCost = cost+w
                
                if distance[v] > newCost:
                    distance[v] = newCost
                    heapq.heappush(queue, (newCost, v))
        
        for i in range(1, n+1):
            if distance[i] == float("inf"):
                return -1
            maxVal = max(maxVal, distance[i])
        
        return maxVal