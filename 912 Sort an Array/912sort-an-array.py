import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        r = []
        while nums:
            r.append(heapq.heappop(nums))
        return r
        