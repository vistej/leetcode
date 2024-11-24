class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mv = abs(matrix[0][0])

        s = 0
        count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                v = matrix[i][j]
                if v < 0:
                    count += 1
                v = abs(v)
                s += v
                mv = min(mv, v)

        
        return s - mv * 2 if count % 2 else s