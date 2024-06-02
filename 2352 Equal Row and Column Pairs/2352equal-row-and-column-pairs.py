class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rid = 0
        cid = 0
        count = 0
        for rid in range(len(grid)):
            for cid in range(len(grid)):
                ind = 0
                isit = True
                while ind < len(grid[rid]):
                    if grid[rid][ind] != grid[ind][cid]:
                        isit = False
                        break
                    ind += 1
                if isit:
                    count += 1

        return count