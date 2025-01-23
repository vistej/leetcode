class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rsum = [0] * len(grid)
        csum = [0] * len(grid[0])

        points = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rsum[i] += grid[i][j]
                    csum[j] += grid[i][j]
                    points[i] = j
        
        res = sum(rsum)
        for i in range(len(rsum)):
            if rsum[i] == 1 and csum[points[i]] == 1:
                res -= 1
        
        return res