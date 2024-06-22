class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        i = c = 0
        j = 1
        while i < j and j < len(nums):
            if nums[j][0] <= nums[i][1]:
                nums[i][1] = max(nums[j][1], nums[i][1])
            else:
                c += nums[i][1] - nums[i][0] + 1
                i = j
            j += 1
        c += nums[i][1] - nums[i][0] + 1

        return c