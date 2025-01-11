class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        p1 = 3
        p2 = 2
        res = 0

        for i in range(3, n):
            res = p1 + p2
            p2 = p1
            p1 = res
        
        return res