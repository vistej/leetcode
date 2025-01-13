class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cm = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            cm = max(nums[i], cm + nums[i])
            res = max(res, cm)
        
        return res