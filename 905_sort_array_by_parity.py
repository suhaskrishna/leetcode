from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evenIdx = 0
        oddIdx = n-1
        
        while evenIdx < n and oddIdx > -1 and evenIdx < oddIdx:
            while evenIdx < n and nums[evenIdx] % 2 == 0:
                evenIdx += 1
            
            while oddIdx > -1 and nums[oddIdx] % 2 == 1:
                oddIdx -= 1
            
            if evenIdx < n and oddIdx > -1 and evenIdx < oddIdx:
                nums[evenIdx], nums[oddIdx] = nums[oddIdx], nums[evenIdx]
                evenIdx += 1
                oddIdx -= 1
        
        return nums
        