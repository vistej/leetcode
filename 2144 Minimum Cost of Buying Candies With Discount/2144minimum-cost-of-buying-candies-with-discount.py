class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i = 1
        r = 0
        while i <= len(cost):
            if not i or i % 3 !=0:
                r += cost[i - 1]
            i += 1
        return r