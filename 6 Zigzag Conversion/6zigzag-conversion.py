class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        d = False
        r = [''] * numRows
        i = 0
        j = 0
        while i < len(s):
            if j == 0:
                d = True
            if j == numRows - 1:
                d = False
            r[j] += s[i]
            i += 1
            j += 1 if d else (-1)
        
        return ''.join(r)