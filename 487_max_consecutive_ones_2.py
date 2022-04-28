from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        si = 0
        lzi = -1
        max1 = 0
        
        for i, val in enumerate(nums):
            if nums[i] == 0:
                if lzi == -1:
                    lzi = i
                else:
                    max1 = max(max1, i-si)
                    si = min(i, lzi+1)
                    lzi = i
        
        max1 = max(max1, len(nums)-si)
        
        return max1