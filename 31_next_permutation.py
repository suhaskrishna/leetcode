class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def reverse(nums, i):
            j = len(nums)-1
            
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
    
        n = len(nums)
        i = n-2
        
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            swap(nums, i, j)
        
        reverse(nums, i+1)