from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = idx = 0
        prev = None
        
        while i < len(nums):
            if nums[i] != prev:
                prev = nums[idx] = nums[i]
                idx += 1
            i += 1
        
        return idx