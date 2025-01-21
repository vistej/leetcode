class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        p = sum(grid[0])

        i = 0
        q = 0
        res = float('inf')
        while i < len(grid[0]):
            p -= grid[0][i]
            q += grid[1][i - 1] if i > 0 else 0
            second = max(p, q)
            res = min(second, res)
            i += 1


        return res
        