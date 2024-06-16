class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        b = {}
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if (pattern[i] in d and d[pattern[i]] != s[i]) or (
                s[i] in b and b[s[i]] != pattern[i]
            ):
                return False
            d[pattern[i]] = s[i]
            b[s[i]] = pattern[i]
        return True