class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 1
        c = 1
        for n in nums:
            s += n
            if s < 1:
                c += abs(s) + 1
                s = 1
        return c