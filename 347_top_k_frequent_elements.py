import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        queue = []
        dic = defaultdict(int)
        for val in nums:
            dic[val] += 1
        
        for key in dic:
            heapq.heappush(queue, (dic[key], key))
            if len(queue) > k:
                heapq.heappop(queue)
        
        
        return [val[1] for val in queue]