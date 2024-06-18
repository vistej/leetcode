class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: 
            return 1
        i = 1
        j = x // 2

        def loo(i, j):
            m = (i + j) // 2
            if m * m == x:
                return m
            elif m * m > x:
                if (m - 1) * (m - 1) <= x:
                    return m - 1
                else:
                    return loo(i, m - 1)
            else:
                if (m + 1) * (m + 1) > x:
                    return m
                else:
                    return loo(m + 1, j)
        
        return loo(i, j)