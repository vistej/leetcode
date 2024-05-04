class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10**9+7
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        for dl in range(1, n+1):
            for tl in range(1, target+1):
                for i in range(1, min(k, tl)+1):
                    dp[dl][tl] += dp[dl-1][tl-i]
                dp[dl][tl] %= modulo
        return dp[n][target]