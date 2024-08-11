class Solution(object):
    def minDays(self, grid):
        def dfs(m, r, c):
            if not (0 <= r < len(m) and 0 <= c < len(m[0])) or m[r][c] == 0:
                return

            m[r][c] = 0
            adjacents = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for row, col in adjacents:
                dfs(m, row, col)

        gc = [row[::] for row in grid]
        count = 0
        for r in range(len(gc)):
            for c in range(len(gc[0])):
                if gc[r][c] == 1:
                    count += 1
                    dfs(gc, r, c)
        
        if count == 0 or count >= 2: return 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    cg = [row[::] for row in grid]
                    cg[r][c] = 0
                    v = 0
                    for row in range(len(cg)):
                        for col in range(len(cg[0])):
                            if cg[row][col] == 1:
                                v += 1
                                dfs(cg, row, col)
                    if v == 0 or v >= 2: return 1
        
        return 2