class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        pro = 0
        for i in prices:
            if i < mini:
                mini = i
                maxi = i
            if i > maxi:
                maxi = i
                pro = max(pro, maxi - mini)
        return pro