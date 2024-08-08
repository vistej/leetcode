class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:
        m = 1
        d = 'rb'

        def dire(m):
            if m == 'rb': return 'lu'
            else: return 'rb'
        
        def add(r, c):
            if r < rows and c < cols and r >=0 and c >= 0:
                res.append([r, c])
        
        res = [[r, c]]
        while len(res) < rows * cols:
            if d == 'rb':
                for _ in range(m):
                    c += 1
                    add(r, c)
                for _  in range(m):
                    r += 1
                    add(r, c)
            else:
                for _ in range(m):
                    c -= 1
                    add(r, c)
                for _ in range(m):
                    r -= 1
                    add(r, c)
            m += 1
            d = dire(d)
        
        return res

                

         