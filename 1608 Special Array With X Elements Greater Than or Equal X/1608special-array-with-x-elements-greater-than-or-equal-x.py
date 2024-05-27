class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) + 1):
            if i <= len(nums) and (i == len(nums) or nums[i] < i):
                return i if (i == 0 or nums[i - 1] >= i) else -1

        return -1