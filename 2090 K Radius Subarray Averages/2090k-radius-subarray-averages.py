import math
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        cnt = k*2 + 1
        sum_r = sum(nums[: cnt - 1]) + nums[-1]

        res = []

        for i in range(len(nums)):
            if i < k or len(nums) - i - 1 < k:
                res.append(-1)
            else:
                print(sum_r, nums[i + k], nums[i - k - 1])
                sum_r += (nums[i + k] - nums[i - k - 1])
                res.append(math.floor(sum_r / cnt))

        return res
