class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = 1
        a = 0
        i = 0

        while m <= n:
            if i < len(nums) and nums[i] <= m:
                m += nums[i]
                i += 1
            else:
                m += m
                a += 1

        return a
