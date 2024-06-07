class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = deque()

        fc = 0
        r = len(grid)
        if not r:
            return -1
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    d.append((i, j))
                elif grid[i][j] == 1:
                    fc += 1
        
        m = 0

        while fc > 0 and len(d):
            m += 1

            for _ in range(len(d)):
                x, y = d.popleft()

                
                for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    xx, yy = x + dx, y + dy

                    if xx < 0 or xx == r or yy < 0 or yy == c:
                        continue
                    if grid[xx][yy] == 0 or  grid[xx][yy] == 2:
                        continue

                    fc -= 1

                    grid[xx][yy] = 2

                    d.append((xx, yy))
            
        return m if not fc else -1
            

