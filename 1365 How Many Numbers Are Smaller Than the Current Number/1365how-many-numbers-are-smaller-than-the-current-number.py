class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i,n in enumerate(sorted(nums)):
            if n not in d:
                d[n] = i
        return [d[i] for i in nums]