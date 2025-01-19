class Solution:
    def smallestNumber(self, pattern: str) -> str:
        v = set()
        b = 1
        e = len(pattern) + 1
        def loo(n, i, v):
            if n < 1 or n > e:
                return None
            if i == e - 1:
                return v
            if pattern[i] == 'I':
                for j in range(n + 1, e + 1):
                    if not j in v:
                        
                        r = loo(j, i + 1, v + [j])
                        if r:
                            return r
            elif pattern[i] == 'D':
                for j in range(n - 1, 0, -1):
                    if not j in v:
                        r = loo(j, i + 1, v + [j])
                        if r:
                            return r
            return None
        for i in range(b, e + 1):
            r = loo(i, 0, [i])
            if r:
                return ''.join([str(c) for c in r])
        
        return ''
