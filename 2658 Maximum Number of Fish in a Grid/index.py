class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        def dfs(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or not grid[i][j]:
                return 0
            
            visited.add((i, j))

            sides = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            ans = 0

            for x,y in sides:
                if (i + x, j + y) not in visited:
                    ans += dfs(i + x, j + y)
            
            return grid[i][j] + ans
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j]:
                    res = max(res, dfs(i, j))
        
        return res
