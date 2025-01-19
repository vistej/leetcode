class Solution:
    def partitionString(self, s: str) -> int:
        v = {}
        c = 0
        for i in s:
            if i in v:
                c += 1
                v = {i: 1}
            else:
                v[i] = 1
        return c + 1