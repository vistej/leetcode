class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        prod_keep = defaultdict(list)

        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                if prod_keep[p]:
                    for tup in prod_keep[p]:
                        if nums[i] not in tup and nums[j] not in tup:
                            res += 8
                prod_keep[p].append((nums[i], nums[j]))
        return res

