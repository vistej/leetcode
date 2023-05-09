class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ar = [sum(x) for x in accounts]
        return max(ar)