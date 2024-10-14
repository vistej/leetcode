
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)

        r = 0
        
        for _ in range(k):
            v = -heapq.heappop(heap)
            r += v
            heapq.heappush(heap, -math.ceil(v/3))
        
        return r