class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        i = 1

        while i < len(nums):
            cr = 1
            while i < len(nums) and nums[i] > nums[i - 1]:
                cr += 1
                i += 1
            
            res = max(res, cr)
            cr = 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                cr = 1
                i += 1
            while i < len(nums) and nums[i] < nums[i - 1]:
                cr += 1
                i += 1
            res = max(res, cr)
        
        return res