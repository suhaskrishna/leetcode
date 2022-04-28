class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(low, high):
            if low > high:
                return -1
            
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return binarySearch(low, mid-1)
            else:
                return binarySearch(mid+1, high)
            
        if target > nums[-1] or target < nums[0]:
            return -1
        
        return binarySearch(0, len(nums)-1)