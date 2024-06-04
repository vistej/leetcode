class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        a = defaultdict(list)

        for i,e in enumerate(equations):
            a[e[0]].append([e[1], values[i]])
            a[e[1]].append([e[0], 1 / values[i]])

        def loo(x, y, a):
            if not x in a or not y in a:
                return -1
            
            q = deque()
            v = set()

            q.append([x, 1])
            v.add(x)

            while q:
                n, w = q.popleft()

                if n == y:
                    return w
                
                for ne,we in a[n]:
                    if not ne in v:
                        q.append([ne, we * w])
                        v.add(ne)
            return -1
        
        
        r = []

        for q in queries:
            r.append(loo(q[0], q[1], a))
        
        return r
