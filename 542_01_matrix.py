from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        que = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i, j))
                    ans[i][j] = 0
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        level = 0
        while len(que) > 0:
            size = len(que)
            
            while size > 0:
                size -= 1
                i, j = que.popleft()
                
                for x, y in dirs:
                    r = i+x
                    c = j+y
                    
                    if r >= 0 and c >= 0 and r < m and c < n and ans[r][c] == -1:
                        que.append((r, c))
                        ans[r][c] = level+1
                
            level += 1
            
        return ans
            