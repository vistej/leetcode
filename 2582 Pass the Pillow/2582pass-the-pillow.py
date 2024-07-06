class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k = time // (n - 1)
        return (time % (n - 1) + 1) if k % 2 == 0 else (n - time % (n - 1))