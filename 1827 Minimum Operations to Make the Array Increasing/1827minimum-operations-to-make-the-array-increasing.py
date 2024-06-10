class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        l = 0
        for n in nums:
            if n > l:
                l = n
            else:
                l += 1
                c += l - n
        return c