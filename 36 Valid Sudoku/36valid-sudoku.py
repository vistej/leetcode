class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [''] * 9
        c = [''] * 9
        b = [''] * 9

        def boxIndex(i, j):
            return 3 * (i // 3) + (j // 3)

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                bi = boxIndex(i, j)
                if v != '.':
                    if v in r[i] or v in c[j] or v in b[bi]:
                        return False
                    r[i] += v
                    c[j] += v
                    b[bi] += v
        return True
   
