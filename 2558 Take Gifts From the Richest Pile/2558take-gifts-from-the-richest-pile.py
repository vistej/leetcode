class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
   
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            val = -heapq.heappop(gifts)
            val = -math.floor(math.sqrt(val))
            heapq.heappush(gifts, val)
        
        return -sum(gifts)