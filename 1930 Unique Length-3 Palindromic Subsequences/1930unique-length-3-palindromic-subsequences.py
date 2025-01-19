class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        checked = set()

        for i in range(len(s) - 2):
            if s[i] in checked:
                continue
            checked.add(s[i])
            for j in range(len(s) - 1, i + 1, -1):
                if s[j] == s[i]:
                    res += len(set(s[i + 1: j]))
                    break
        return res

        