class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for g in grid:
            i = 0
            j = len(g) - 1

            while i <= j:
                m = (i + j) // 2
                if g[m] < 0:
                    j = m - 1
                else:
                    i = m + 1
            c += len(g) - i
        return c

                    
