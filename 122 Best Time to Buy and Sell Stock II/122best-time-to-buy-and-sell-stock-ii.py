class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        if not prices:
            return p

        b = prices[0]

        for price in prices[1:]:
            if price < b:
                b = price
            else:
                p += price - b
                b = price

        return p
