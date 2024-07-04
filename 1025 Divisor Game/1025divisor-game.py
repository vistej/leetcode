class Solution:
    def divisorGame(self, n: int) -> bool:
        a = False
        k = 0
        while k < n - 1:
            k = k + 1
            if not n % k:
                n -= k
                k = 0
                a = not a
        return a
            
