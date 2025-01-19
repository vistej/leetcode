class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        while k > 0:
            minimum = heapq.heappop(heap)
            heapq.heappush(heap,-minimum)
            k -= 1
        return sum(heap)