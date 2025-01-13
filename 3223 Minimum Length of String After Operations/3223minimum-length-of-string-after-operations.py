class Solution:
    def minimumLength(self, s: str) -> int:
        counts = Counter(s)
        res = len(s)

        for _, v in counts.items():
            if v > 2:
                if v % 2:
                    res = res - v + 1
                else:
                    res = res - v + 2

        return res