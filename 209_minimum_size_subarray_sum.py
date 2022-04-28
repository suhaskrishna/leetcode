from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        ans = float("inf")
        
        si = 0
        for i, val in enumerate(nums):
            curSum += val
            
            while curSum >= target:
                ans = min(ans, i-si+1)
                curSum -= nums[si]
                si += 1
                
        
        return ans if ans != float("inf") else 0