class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rm = [max(row) for row in grid]
        cm = [max(col) for col in zip(*grid)] 

        t = 0
        for r in range(n):
            for c in range(n):
                t += min(rm[r], cm[c]) - grid[r][c]

        return t
