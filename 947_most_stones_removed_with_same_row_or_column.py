class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:        
        visited = set()
        row = defaultdict(set)
        col = defaultdict(set)
        
        numIsland = 0
        
        for i, j in stones:
            row[i].add(j)
            col[j].add(i)
            
        def dfs(i, j):
            visited.add((i, j))
            
            for c in row[i]:
                if (i, c) not in visited:
                    dfs(i, c)
            
            for r in col[j]:
                if (r, j) not in visited:
                    dfs(r, j)
            
        for i, j in stones:
            if (i, j) not in visited:
                dfs(i, j)
                numIsland += 1
        
        return len(stones) - numIsland