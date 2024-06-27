class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        a = [0, 0, 0]
        s = 0
        for j,g in enumerate(garbage):
            s += len(g)
            if "P" in g:
                s += a[0]
                a[0] = 0
            if "G" in g:
                s += a[1]
                a[1] = 0
            if "M" in g:
                s += a[2]
                a[2] = 0
            if j < len(travel):
                for i in range(3):
                    a[i] += travel[j]
        return s

