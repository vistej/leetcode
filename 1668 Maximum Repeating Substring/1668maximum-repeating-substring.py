class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence == word:
            return 1
        l = len(word)
        i = 0
        r = 0
        while i < len(sequence) - l + 1:
            c = 0
            j = i
            while j < len(sequence) - l + 1 and sequence[j] == word[0]:
                s = sequence[j: j + l]
                if s == word:
                    c += 1
                    j += l
                    r = max(r, c)
                else:
                    break
            i += 1
        return r