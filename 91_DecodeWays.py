class Solution:
    def numDecodingsMemo(self, s, index, memo):
        if index in memo:
            return memo[index]
        
        if index == len(s):
            return 1
        
        if s[index] == '0':
            return 0
        
        if index == len(s)-1:
            return 1
        
        ans = self.numDecodingsMemo(s, index+1, memo)
        if int(s[index:index+2]) <= 26:
            ans += self.numDecodingsMemo(s, index+2, memo)
        
        memo[index] = ans
        
        return ans
    
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.numDecodingsMemo(s, 0, memo)