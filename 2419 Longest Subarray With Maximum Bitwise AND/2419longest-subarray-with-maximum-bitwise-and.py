class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        x = 0
        t = 0
        s = False
        for n in nums:
            if n == m:
                t += 1
                
            else:
                x = max(x, t)
                t = 0
        return max(x, t)
                
