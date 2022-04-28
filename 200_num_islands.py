from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            
            grid[i][j] = '0'
            
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                
                if x >= 0 and y >= 0 and x<m and y < n and grid[x][y] == '1':
                    dfs(grid, x, y)
                    
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res