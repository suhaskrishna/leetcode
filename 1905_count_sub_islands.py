from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:                    
                    
        def dfs(row, col):
            grid2[row][col] = 0
            
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for i, j in dirs:
                newRow = row+i
                newCol = col+j
                
                if newRow >= 0 and newRow < self.NUM_ROWS and newCol >= 0 and newCol < self.NUM_COLS and grid2[newRow][newCol] == 1:
                    dfs(newRow, newCol)
        
        self.NUM_ROWS = len(grid1)
        self.NUM_COLS = len(grid1[0])
        
        count = 0
        
        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COLS):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)

        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COLS):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
                    count += 1
        
        return count
        
s = Solution()

print(s.countSubIslands([[0,1,1,1,1,1,1,0,1,1],[1,0,1,1,1,0,1,1,1,1],[1,0,1,1,0,1,1,1,1,1],[1,0,1,1,0,1,1,1,1,1],[1,0,1,1,1,1,1,0,1,1],[1,1,0,0,1,1,1,0,0,1],[1,1,0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,1,1,1],[1,0,0,1,1,0,1,1,1,1]],
[[0,0,1,1,1,1,1,1,1,1],[1,0,0,1,1,1,0,0,1,0],[1,1,1,0,1,1,0,1,1,1],[1,0,0,1,0,0,1,0,1,1],[0,1,1,1,0,1,0,1,1,0],[1,1,1,0,0,0,1,0,1,0],[1,1,1,1,1,1,1,1,1,1],[1,1,1,0,0,0,1,0,1,1],[1,1,1,1,1,1,0,1,1,0]]))
        