class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {0: -1}
        p = 0
        r = 0
        vows = 'aeiou'

        for i,c in enumerate(s):
            if c in vows:
                index = vows.index(c)
                p ^= 1<<index

            if p in d:
                r = max(r, i - d[p])
            else:
                d[p] = i
                
        return r