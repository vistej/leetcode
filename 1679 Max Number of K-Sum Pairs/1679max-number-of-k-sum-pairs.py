class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        c = 0
        for n in nums:
            l = k - n
            if l in d and d[l]:
                d[l] -= 1
                c += 1
            else:
                d[n] = d.get(n, 0) + 1
        return c