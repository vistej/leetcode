class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums) + 2):
            d[i] = ''
        for num in nums:
            del d[num]
        return list(d.keys())[0]