from typing import List
def removeElement(nums: List[int], val: int) -> int:
    idx = 0
    i = 0
    n = len(nums)
    
    while i<n:
        if nums[i] != val:
            nums[idx] = nums[i]
            idx += 1
        i += 1
    
    return idx
        
print(removeElement([3, 2, 2, 3], 3))