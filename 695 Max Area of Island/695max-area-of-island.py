class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def bfs(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or not grid[i][j]:
                return 0
            grid[i][j] = 0
            sides = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            d = 0
            for x, y in sides:
                d += bfs(x, y)
            
            return 1 + d
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    r = bfs(i, j)
                    res = max(r, res)
                
        return res

