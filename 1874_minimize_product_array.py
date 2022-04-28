#Using plain sorting
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        
        return sum([n1*n2 for n1, n2 in zip(nums1, nums2)])

#Using sorting and priority queue
import heapq

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        queue = [n * -1 for n in nums2]
        
        heapq.heapify(queue)
        
        res = 0
        for val in nums1:
            res += val * heapq.heappop(queue) * -1
        
        return res

#Using count sort
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = [0 for _ in range(101)]
        count2 = [0 for _ in range(101)]
        
        for val in nums1:
            count1[val] += 1
        
        for val in nums2:
            count2[val] += 1
        
        i = 0
        j = 100
        
        ans = 0
        while i <= 100 and j >= 0:
            while i <= 100 and count1[i] == 0:
                i += 1
            
            while j >= -1 and count2[j] == 0:
                j -= 1
            
            if i <= 100 and j >= 0:
                ans += (i*j)
            
                count1[i] -= 1
                count2[j] -= 1
        
        return ans
            