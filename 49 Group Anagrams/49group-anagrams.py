class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = {}

        for st in strs:
            l = ''.join(sorted([i for i in st]))
            if l not in c:
                c[l] = []
            c[l].append(st)
            
        return c.values()