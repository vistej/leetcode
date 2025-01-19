class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        r = 0
        for m in list(zip(*grid)):
            r += max(m)
        return r