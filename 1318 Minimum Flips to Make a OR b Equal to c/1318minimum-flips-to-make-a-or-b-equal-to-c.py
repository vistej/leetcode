class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
            a1 = format(a, 'b')
            b1 = format(b, 'b')
            c1 = format(c, 'b')
            maxl = max(len(a1), len(b1), len(c1))
            a1 = a1.rjust(maxl, '0')
            b1 = b1.rjust(maxl, '0')
            c1 = c1.rjust(maxl, '0')
            cnt = 0
            for i in range(len(a1)):
                if int(a1[i]) | int(b1[i]) != int(c1[i]):
                    if c1[i] == '1':
                        cnt += 1
                    else:
                        if a1[i] == '1':
                            cnt += 1
                        if b1[i] == '1':
                            cnt += 1
            return cnt