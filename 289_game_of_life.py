class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numRow = len(board)
        numCol = len(board[0])
        
        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for i in range(numRow):
            for j in range(numCol):
                count = 0
                for d in dirs:
                    u = i + d[0]
                    v = j + d[1]
                    
                    if u >= 0 and u < numRow and v >= 0 and v < numCol and abs(board[u][v]) == 1:
                        count += 1
                
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2
        
        for i in range(numRow):
            for j in range(numCol):
                if board[i][j] >= 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
                        
        