class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        s = 0
        if sum(nums) < target:
            return 0
        m = len(nums)
        for i,n in enumerate(nums):
            s += n
            while s >= target:
                s -= nums[j]
                m = min(m,i - j + 1)
                j += 1
        
        return m
            