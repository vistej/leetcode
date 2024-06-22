class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = c = 0
        for n in nums:
            s += n
            if not s:
                c += 1
        return c