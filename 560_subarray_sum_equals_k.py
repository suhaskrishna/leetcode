class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        count[0] = 1
        
        s = 0
        res = 0
        for val in nums:
            s += val
            if s-k in count:
                res += count[s-k]
            count[s] = count.get(s, 0) + 1
            
        return res
        