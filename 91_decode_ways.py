class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        for idx in range(len(s), -1, -1):
            if idx == len(s):
                dp[idx] = 1
                continue

            if s[idx] == "0":
                dp[idx] = 0
                continue

            ans = dp[idx+1]

            if idx+1 < len(s):
                if int(s[idx:idx+2]) <= 26:
                    ans += dp[idx+2]

            dp[idx] = ans
            
        return dp[0]
        