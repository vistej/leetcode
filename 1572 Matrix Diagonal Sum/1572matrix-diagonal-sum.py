class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        i = 0
        j = 0
        k = l - 1
        r = 0
        while i < l:
            r += mat[i][j]
            r += mat[i][k]
            i += 1
            j += 1
            k -= 1
        if l % 2:
            m = l // 2
            r -= mat[m][m]
        return r
