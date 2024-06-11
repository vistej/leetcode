class Solution:
    def splitNum(self, num: int) -> int:
        d = sorted(list(str(num)))
        a = ''
        b = ''
        for i in range(0, len(d), 2):
            a += d[i]
            if i + 1 < len(d):
                b += d[i + 1]
        return int(a) + int(b)