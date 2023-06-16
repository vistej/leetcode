import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        def combs(n, l):
            if l > n:
                return 0
            return (math.factorial(n))//((math.factorial(l)) * (math.factorial(n - l)))

        def countWays(arr):
            if len(arr) <= 2:
                return 1

            la = list(filter(lambda x: x < arr[0], arr))
            ra = list(filter(lambda x: x > arr[0], arr))

            lc = countWays(la)
            rc = countWays(ra)

            return lc * rc * combs(len(arr) - 1, len(la))

        return ((countWays(nums) - 1) % (10**9 + 7))
