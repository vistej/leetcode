class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        for n in nums:
            c += (int(n < k))
        return c