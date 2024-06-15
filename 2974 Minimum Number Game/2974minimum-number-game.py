class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            t = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = t

        return nums