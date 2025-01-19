class Solution:
    def notGood(self, c1, c2):
        return c1.lower() == c2.lower() and c1 != c2
    def makeGood(self, s: str) -> str:
        r = []
        for c in s:
            if len(r):
                if self.notGood(r[-1], c):
                    r.pop()
                    continue
            r.append(c)
        return ''.join(r)
        