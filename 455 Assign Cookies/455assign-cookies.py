class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i = 0
        j = 0
        c = 0
        while i < len(g):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j == len(s):
                return c
            c += 1
            i += 1
            j += 1
        
        return c