class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        heapq.heapify(nums)
        while len(nums) >= 2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >= k and y >= k:
                break
            val = min(x, y) * 2 + max(x, y)
            ops += 1
            heapq.heappush(nums, val)
        
        return ops
