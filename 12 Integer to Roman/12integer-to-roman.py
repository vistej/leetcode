class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'}

        self.r = ''
        def loo(n, p):
            v = n // p
            l = n % p
            t = n - l
            if t in d:
                self.r += d[t]
            else:
                while v:
                    if v > 5 and 5*p in d:
                        self.r += d[5*p]
                        v -= 5
                    else:
                        self.r += d[p]
                        v -= 1
            return l
        if num > 1000:
            num = loo(num, 1000)
        if num > 100:
            num = loo(num, 100)
        if num > 10:
            num = loo(num, 10)
        if num > 0:
            num = loo(num, 1)
        return self.r

