class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r = []
        d = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            a = min(matrix[i])
            b = matrix[i].index(a)
            c = max(d[b])
            if a == c:
                r.append(a)
        
        return r
