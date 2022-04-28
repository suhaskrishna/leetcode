from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        curOnes = 0
        
        for i, val in enumerate(nums):
            if val == 1:
                curOnes += 1
                maxOnes = max(maxOnes, curOnes)
            else:
                curOnes = 0
        
        return maxOnes