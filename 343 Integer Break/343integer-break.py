class Solution:
    def integerBreak(self, n: int) -> int:
        if (n == 2 or n == 3):
            return (n-1)

        res = 1
        while (n > 4):
            n -= 3
            print(n)
            res *= 3
        return (n * res);

