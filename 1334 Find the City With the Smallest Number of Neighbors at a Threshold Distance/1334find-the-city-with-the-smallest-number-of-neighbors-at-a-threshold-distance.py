from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], danceThreshold: int) -> int:
        d = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            d[i][i] = 0
        
        for u, v, w in edges:
            d[u][v] = w
            d[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
        
        mr = float('inf')
        b = -1
        
        for i in range(n):
            r = 0
            for j in range(n):
                if d[i][j] <= danceThreshold:
                    r += 1
            
            if r <= mr:
                mr = r
                b = i
        
        return b