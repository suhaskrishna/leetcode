from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        result = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 4
                    
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        result -= 2
                    
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        result -= 2
        
        return result