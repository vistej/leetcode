class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = {}
        for w in words:
            i = 1
            while i <= len(w):
                s = w[:i]
                d[s] = d.get(s, 0) + 1
                i += 1
        
        r = []
        for w in words:
            i = 1
            c = 0
            while i <= len(w):
                c += d[w[:i]]
                i += 1
            r.append(c)
        
        return r