class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pi = 0
        ls = 0
        rs = sum(nums[1: ])

        while ls != rs and pi < len(nums) - 1:
            ls += nums[pi]
            pi += 1
            rs -= nums[pi]
        
        return pi if ls == rs else -1