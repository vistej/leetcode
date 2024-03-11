class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderd = {c: i for i, c in enumerate(order)}
        sd = [((orderd[c] if c in orderd else -i), c) for i, c in enumerate(s)]
        sd = ''.join(i[1] for i in sorted(sd, key=lambda x: x[0]))
        return sd
