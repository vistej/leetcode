class Solution:
    def minimumPushes(self, word: str) -> int:
        l = 8
        v = 1
        d = {}
        for i in range(len(word)):
            c = word[i]
            d[c] = d.get(c, 0) + 1
        
        k = sorted(d.items(), key=lambda x: x[1], reverse=True)
        r = 0
        for a,b in k:
            r += b * v
            l -= 1
            if not l:
                l = 8
                v += 1

        return r