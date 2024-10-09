class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r = 0
        k = 0
        for c in list(s):
            if c == '(':
                r += 1
            else:
                if r:
                    r -= 1
                else:
                    k += 1
        
        return abs(r) + k
            