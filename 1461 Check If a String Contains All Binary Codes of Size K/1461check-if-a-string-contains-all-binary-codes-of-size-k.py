class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        r = set()

        for i in range(len(s) - k + 1):
            p = s[i: i + k]
            r.add(p)
        return len(r) == 2 ** k