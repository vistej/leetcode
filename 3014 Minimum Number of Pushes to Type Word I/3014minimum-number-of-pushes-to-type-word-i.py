class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        c = 0
        i = 1
        while l:
            if l > 8:
                l -= 8
                c += 8 * i
                i += 1
            else:
                c += l * i
                l = 0
        return c

