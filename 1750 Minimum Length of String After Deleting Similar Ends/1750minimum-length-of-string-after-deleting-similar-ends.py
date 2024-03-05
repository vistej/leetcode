class Solution:
    def minimumLength(self, s: str) -> int:
        si = 0
        ei = len(s) - 1

        while ei > si and s[si] == s[ei]:
            si = si + 1
            ei = ei - 1
            while si + 1 < ei and s[si] == s[si - 1]:
                si = si + 1
            while ei - 1 > si and s[ei] == s[ei + 1]:
                ei = ei - 1
        res = ei - si + 1
        return res

        