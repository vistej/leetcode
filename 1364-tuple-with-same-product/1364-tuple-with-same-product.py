class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        prod_keep = defaultdict(int)

        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                res += prod_keep[p]
                prod_keep[p] += 1
        return res * 8

