class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row_sum = [0] * len(mat)
        col_sum = [0] * len(mat[0])
        keys = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]
                keys[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            x, y = keys[arr[i]]
            row_sum[x] -= arr[i]
            col_sum[y] -= arr[i]
            if not row_sum[x] or not col_sum[y]:
                return i