class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = [[1]]

        def loo(r, i):
            if i > numRows:
                return r
            a = [1]
            p = r[-1]
            if len(p) > 1:
                for j in range(len(p) - 1):
                    a.append(p[j] + p[j + 1])

            a.append(1)
            r.append(a)
            return loo(r, i + 1)
    
        return loo(r, 2)