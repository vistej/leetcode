class Solution:
    def makeFancyString(self, s: str) -> str:
        x = ''
        res = ''
        count = 0
        for c in list(s):
            if c != x:
                x = c
                count = 1
            else:
                count += 1
            if count < 3:
                res += c
            
        return res