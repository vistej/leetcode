class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n] * m

        ans = 0

        for i in range(m):
            dp[i][0] = matrix[i][0]
            ans += matrix[i][0]
        
        for i in range(1, n):
            dp[0][i] = matrix[0][i]
            ans += matrix[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                ans += matrix[i][j]


        return ans
