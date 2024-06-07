class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0, 1, 1]
        if n < len(l):
            return l[n]
        i = len(l)
        while i <= n:
            v = sum(l)
            l = l[1:] + [v]
            i += 1
        return l[-1]