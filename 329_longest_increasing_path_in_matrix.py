from collections import deque
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        indegree = [[0 for _ in range(n)] for _ in range(m)]
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(m):
            for j in range(n):
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    
                    if x >= 0 and y >= 0 and x < m and y < n and matrix[x][y] > matrix[i][j]:
                        indegree[x][y] += 1
        
        
        que = deque()
        level = 0
        
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    que.append((i, j))
        
        
        while len(que) > 0:
            size = len(que)
            
            while size > 0:
                size -= 1
                
                i, j = que.popleft()
                
                for d in dirs:
                    x = i+d[0]
                    y = j+d[1]
                    
                    if x >= 0 and y >= 0 and x < m and y < n and matrix[x][y] > matrix[i][j]:
                        indegree[x][y] -= 1
                        if indegree[x][y] == 0:
                            que.append((x, y))
            level += 1
        
        return level
                    