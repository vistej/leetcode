class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = [[0, i] for i in range(n)]
        for a,b in roads:
            d[a][0] += 1
            d[b][0] += 1
        
        d.sort()
        s = 0
        for i in range(n):
            s += (i + 1) * d[i][0]
        

        return s