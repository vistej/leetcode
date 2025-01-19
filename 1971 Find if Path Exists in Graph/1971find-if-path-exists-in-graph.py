class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ch = {}
        ch[source] = 1
        oc = {}
        oc[destination] = 1
        r = []
        i = 0
        while i < len(edges):
            edge = edges[i]
            if edge[0] in ch or edge[1] in ch:
                if destination in edge:
                    return True
                ch[edge[0]] = 1
                ch[edge[1]] = 1
            elif edge[0] in oc or edge[1] in oc:
                oc[edge[0]] = 1
                oc[edge[1]] = 1
            else:
                r.append(edge)
            i += 1
            if i == len(edges):
                if len(r) == len(edges):
                    return False
                else:
                    edges = r
                    r = []
                    i = 0
            
        for o in oc:
            if o in ch:
                return True
        return False