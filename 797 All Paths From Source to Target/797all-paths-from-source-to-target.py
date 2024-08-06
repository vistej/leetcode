class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        r = []
        def loo(i):
            r = []
            for k in graph[i]:
                p = loo(k)
                if p:
                    for pi in p:
                        r.append([k] + pi)
                elif k == len(graph) - 1:
                    r.append([k])
            return r
        d = loo(0)
        r = [[0] + k for k in d]
        return r
