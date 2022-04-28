from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        
        for val in nums:
            if val != 0:
                nums[idx] = val
                idx += 1
        
        while idx < len(nums):
            nums[idx] = 0
            idx += 1