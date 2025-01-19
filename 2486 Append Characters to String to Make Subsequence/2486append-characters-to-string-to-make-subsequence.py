class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i < len(t):
            while j < len(s) and s[j] != t[i]:
                j += 1
            if j == len(s):
                return len(t) - i
            j += 1
            i += 1
        return 0