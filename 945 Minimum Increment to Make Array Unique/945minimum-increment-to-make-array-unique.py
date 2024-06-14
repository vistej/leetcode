class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        c = 0
        nums.sort()
        k = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > k + 1:
                k = nums[i]
            else:
                c += k + 1 - nums[i]
                k += 1
        return c
