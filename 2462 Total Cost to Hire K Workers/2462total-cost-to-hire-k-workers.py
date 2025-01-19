from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        if candidates * 2 >= N:
            return sum(sorted(costs)[:k])
        
        lh = costs[:candidates]
        rh = costs[-candidates:]
        heapify(lh)
        heapify(rh)

        cost = 0
        l = candidates
        r = N - candidates - 1
        
        for _ in range(k):
            if not rh or (lh and lh[0] <= rh[0]):
                cost += heappop(lh)
                if l <= r:
                    heappush(lh, costs[l])
                    l += 1
            else:
                cost += heappop(rh)
                if l <= r:
                    heappush(rh, costs[r])
                    r -= 1
        
        return cost
