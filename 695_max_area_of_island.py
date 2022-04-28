from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            grid[i][j] = 0
            count = 1
            
            for d in dirs:
                x = i+d[0]
                y = j+d[1]
                
                if x >= 0 and y >= 0 and x<m and y<n and grid[x][y] == 1:
                    count += dfs(grid, x, y)
            
            return count
        
        m = len(grid)
        n = len(grid[0])
        
        maxArea = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(grid, i, j)
                    maxArea = max(maxArea, area)
                    
        return maxArea

#Solution 2
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.exploreGrid(i, j, grid))
        
        return maxArea
    
    def exploreGrid(self, i, j, grid):
        count = 0
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            count = 1 + self.exploreGrid(i, j+1, grid) + self.exploreGrid(i+1, j, grid) + self.exploreGrid(i, j-1, grid) + self.exploreGrid(i-1, j, grid)
        
        return count
        