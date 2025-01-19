class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        os = 0
        es = 0

        for p in position:
            if p%2 == 0:
                es += 1
            else:
                os += 1
        return min(os, es)
