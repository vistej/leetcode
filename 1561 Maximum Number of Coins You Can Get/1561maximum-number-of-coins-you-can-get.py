class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        cg = len(piles) // 3
        piles.sort(reverse=True)
        i = 1
        r = 0
        while cg:
            r += piles[i]
            i += 2
            cg -= 1
        return r
