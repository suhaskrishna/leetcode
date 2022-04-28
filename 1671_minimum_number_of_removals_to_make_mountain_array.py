class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dpi = [1 for _ in range(n)]
        dpd = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dpi[i] = max(dpi[i], dpi[j]+1)
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if nums[j] < nums[i]:
                    dpd[i] = max(dpd[i], dpd[j]+1)
        
        res=0
        for i in range(n):
            if dpi[i] == 1 or dpd[i] == 1:
                continue
            res = max(res, dpi[i]+dpd[i]-1)
        
        return n-res