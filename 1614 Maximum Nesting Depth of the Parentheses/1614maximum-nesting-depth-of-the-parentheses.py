class Solution:
    def maxDepth(self, s: str) -> int:
        k = 0
        ans = 0
        for c in s:
            if c == '(':
                k += 1
                ans = max(ans, k)
            elif c == ')':
                k -= 1
        return ans