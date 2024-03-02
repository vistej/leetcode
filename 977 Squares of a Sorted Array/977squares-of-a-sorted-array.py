class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ci = 0
        for i in range(len(nums) - 1):
            ci = ci + 1
            if abs(nums[i]) < abs(nums[i + 1]):
                ci = ci - 1
                break;
        res = [nums[ci] * nums[ci]]
        i = ci - 1
        j = ci + 1

        for k in range(len(nums) - 1):
            if i >= 0:
                if j == len(nums) or abs(nums[i]) <= abs(nums[j]):
                    res.append(nums[i] * nums[i])
                    i = i - 1
            if j < len(nums):
                if i < 0 or abs(nums[i]) > abs(nums[j]):
                    res.append(nums[j] * nums[j])
                    j = j + 1
        return res