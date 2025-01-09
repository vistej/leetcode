class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0


        def dfs(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or not grid[i][j]:
                return
            visited.add((i, j))
            if grid[i][j] == '0':
                return
            sides = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1) ]
            for x,y in sides:
                if (x, y) not in visited:
                    dfs(x,y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        
        return count
            