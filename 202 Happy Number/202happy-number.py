class Solution:
    def isHappy(self, n: int) -> bool:
        c = {}
        while n not in c:
            c[n] = 1
            if n == 1:
                return True
            n = sum([pow(int(i), 2) for i in str(n)])
        return False
