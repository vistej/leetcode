class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(n, p):
            if p[n] != n:
                p[n] = find(p[n], p)
            return p[n]

        def union(n, y, p):
            p[find(n, p)] = find(y, p)

        seta = list(range(n + 1))
        setb = list(range(n + 1))
        c = 0
        edges.sort(key=lambda n: n[0], reverse=True)

        for e in edges:
            if e[0] == 3:
                if find(e[1], seta) == find(e[2], seta) and find(e[1], setb) == find(e[2], setb):
                    c += 1
                    continue

                union(e[1], e[2], seta)
                union(e[1], e[2], setb)
            elif e[0] == 1:
                if find(e[1], seta) == find(e[2], seta):
                    c += 1

                union(e[1], e[2], seta)
            else:
                if find(e[1], setb) == find(e[2], setb):
                    c += 1

                union(e[1], e[2], setb)

        for i in range(1, n + 1):
            find(i, seta)
            find(i, setb)

        for i in range(2, n + 1):
            if seta[i] != seta[1] or setb[i] != setb[1]:
                return -1

        return c