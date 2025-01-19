class Solution:
    def numWaterBottles(self, n: int, e: int) -> int:
        d = n

        while n >= e:
            k = (n // e)
            d += k
            n = k + (n % e)
        return d