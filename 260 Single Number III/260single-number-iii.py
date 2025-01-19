class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}

        for n in nums:
            if n in d:
                del d[n]
            else:
                d[n] = 1
        return d.keys()