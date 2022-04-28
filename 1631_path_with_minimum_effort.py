import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        
        dif = [[float("inf") for _ in range(m)] for _ in range(n)]
        
        queue = [(0, 0, 0)]
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            effort, row, col = heapq.heappop(queue)
            
            if dif[row][col] < effort:
                continue
            
            if row == n-1 and col == m-1:
                return effort
            
            for d in dirs:
                x = row+d[0]
                y = col+d[1]
                
                if x >= 0 and y >= 0 and x < n and y < m:
                    newEffort = max(effort, abs(heights[row][col] - heights[x][y]))
                    if newEffort < dif[x][y]:
                        dif[x][y] = newEffort
                        heapq.heappush(queue, (newEffort, x, y))
        
        return dif[n-1][m-1]
            
            
        
        
        
        