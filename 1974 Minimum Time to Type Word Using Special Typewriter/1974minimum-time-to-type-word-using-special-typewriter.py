class Solution:
    def minTimeToType(self, word: str) -> int:
        c = 0
        l = 'a'
        for i in word:
            d = abs(ord(i) - ord(l))
            d = min(d, abs(d - 26))
            c += d + 1
            l = i
        return c