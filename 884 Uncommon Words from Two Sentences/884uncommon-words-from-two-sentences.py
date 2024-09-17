class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        for w in s1.split(' '):
            d[w] = not w in d
        for w in s2.split(' '):
            d[w] = not w in d
        
        r = []
        for k,v in d.items():
            if v:
                r.append(k)
        
        return r