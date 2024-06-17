class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            v = pow(i, 2) + pow(j, 2)
            if v == c:
                return True
            if v > c:
                j -= 1
            else:
                i += 1

        return False