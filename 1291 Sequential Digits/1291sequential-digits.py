class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        if high < low:
            return []
        a = list(str(low))
        b = list(str(high))
        la = len(a)
        lb = len(b)

        f = int(a[0])
        l = b[0]
        k = 1
        while int(l) <= f:
            l += b[k]
            k += 1
        l = int(l)
        
        def getCon(v, l):
            if v + l - 1 < 10:
                s = ''
                for i in range(l):
                    s += str(v)
                    v += 1
                return int(s)
            else:
                return 0

        r = []
        for i in range(la, lb + 1):
            for j in range(1, 10):
                n = getCon(j, i)
                if n >= low and n <= high:
                    r.append(n)
        return r
