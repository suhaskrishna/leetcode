class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        
        def helper(s, si, ei, memo):
            if si == ei:
                memo[si][ei] = 1
                return 1
            
            if si > ei:
                return 0
            
            if memo[si][ei] != -1:
                return memo[si][ei]
            
            if s[si] == s[ei]:
                memo[si][ei] = 2+ helper(s, si+1, ei-1, memo)
            else:
                memo[si][ei] = max(helper(s, si+1, ei, memo), helper(s, si, ei-1, memo))
            
            return memo[si][ei]
        
        return helper(s, 0, n-1, memo)