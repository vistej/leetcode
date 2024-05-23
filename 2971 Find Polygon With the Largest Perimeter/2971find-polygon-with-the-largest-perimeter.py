class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        ps = [0] * len(nums)
        s = 0

        for i, n in enumerate(nums):
            ps[i] = s
            s += n

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < ps[i]:
                return ps[i] + nums[i]

        return -1
