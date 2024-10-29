class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = {}

        def move(v, r, c):
            if r < 0 or r >= m or c >= n or v >= grid[r][c]:
                return 0
            key = str(r) + '_' + str(c)
            if key in d:
                return d[key]
            val = grid[r][c]
            res =  1 + max(move(val, r - 1, c + 1), move(val, r, c + 1), move(val, r + 1, c + 1))
            d[key] = res
            return res
        moves = 0
        for row in range(m):
            col = 0
            moves = max(moves, move(0, row, col))
        
        return moves - 1


