class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        row = col = idx = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while count <= n*n:
            matrix[row][col] = count
            count += 1
            
            if row+dirs[idx][0] == n or col+dirs[idx][1] == n or matrix[row+dirs[idx][0]][col+dirs[idx][1]] != 0:
                idx = (idx+1) % 4
            
            row += dirs[idx][0]
            col += dirs[idx][1]
        
        return matrix