class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        k = 2
        res = False
        while k <= n:
            if k == n:
                res = True
                break
            k = k * 2
        return res

        