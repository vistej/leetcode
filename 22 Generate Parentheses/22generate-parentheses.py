class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []

        def loo(s, x, y):
            if not x and not y:
                r.append(s)
            else:
                if x:
                    loo(s + '(', x - 1, y)
                if y > x:
                    loo(s + ')', x, y - 1)
        loo('', n, n)

        return r
            