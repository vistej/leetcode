class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    r += 4
                    if i + 1 < len(grid) and grid[i + 1][j]:
                        r -= 2
                    if j + 1 < len(grid[0]) and grid[i][j + 1]:
                        r -= 2
        return r