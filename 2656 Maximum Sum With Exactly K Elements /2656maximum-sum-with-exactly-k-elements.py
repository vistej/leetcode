class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        a = max(nums)
        r = 0
        for _ in range(k):
            r += a
            a += 1
        return r