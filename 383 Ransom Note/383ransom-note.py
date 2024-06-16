class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for r in ransomNote:
            d[r] = d.get(r, 0) + 1
        l = len(d)
        for m in magazine:
            if m in d:
                d[m] -= 1
                if not d[m]:
                    l -= 1
        return not bool(l) 