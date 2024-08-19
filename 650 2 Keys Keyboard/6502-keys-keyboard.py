class Solution:
    def minSteps(self, n):
        s = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                s += i
                n //= i
            i += 1
        if n > 1: 
            s += n
        return s