class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(1, rows):
            for c in range(cols):
                top_left = matrix[r - 1][c - 1] if c - 1 >= 0 else float ('inf')
                top_above = matrix[r - 1][c]
                top_right = matrix[r - 1][c + 1] if c + 1 < cols else float('inf')

                matrix[r][c] = matrix[r][c] + min(top_left, top_above, top_right)
        return min(matrix[-1])