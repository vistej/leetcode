class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = {}
        limit = len(nums)/3
        res = []
        for num in nums:
            if not num in check:
                check[num] = 1
            elif check[num] != -1:
                check[num] += 1
            if check[num] > limit:
                res.append(num)
                check[num] = -1
        return res