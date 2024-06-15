class Solution:
    def countBits(self, n: int) -> List[int]:
        r = {}
        a = []
        for i in range(n + 1):
            c = 0
            while i:
                if i in r:
                    c += r[i]
                    break
                c += i % 2
                i = i // 2
            a.append(c)
            r[i] = c
        return a