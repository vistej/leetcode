class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = {}

        for b,a in edges:
            if not a in d:
                d[a] = []
            d[a].append(b)
        
        r = []
        i = 0
        while i < n:
            s = set([])
            if i in d:
                t = []
                k = d[i]
                while k:
                    for v in k:
                        if not v in s:
                            s.add(v)
                            if v in d:
                                t.extend(d[v])
                    k = t
                    t = []
            i += 1
            r.append(sorted(s))
        return r


                
