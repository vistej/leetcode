class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        d = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

        i = 0
        c = 0
        r = 0
        for j,v in enumerate(d):
            c += v

            while c > maxCost:
                c -= d[i]
                i += 1
            
            r = max(r, j - i + 1)



        return r