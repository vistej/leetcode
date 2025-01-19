class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        m = 0
        c = 0
        d = {'a':1, 'e':1, 'i':1, 'o':1, 'u': 1}
        for i in range(len(s)):
            if s[i] in d:
                c += 1
            if i >= k - 1:
                m = max(m, c)
                if s[i - k + 1] in d:
                    c -= 1
        return m