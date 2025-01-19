class Solution:
    def minSwaps(self, s: str) -> int:
        r = 0

        v = 1

        for i,c in enumerate(s):
            if c == ']':
                if i < v:
                    r += 1
                else:
                    v += 2
        return r