class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        x = 0
        i = len(nums) - 1
        res = 0

        while i > 0:
            x += nums[i]
            s -= nums[i]
            if s >= x:
                res += 1
            i -= 1

        return res
