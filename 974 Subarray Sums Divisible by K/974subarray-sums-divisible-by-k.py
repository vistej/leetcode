class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p = {}
        s = 0
        r = 0
        for n in nums:
            s += n
            m = s%k
            if m in p:
                r += p[m]
                p[m] += 1
            else:
                p[m] = 1
        return r + (p[0] if 0 in p else 0)