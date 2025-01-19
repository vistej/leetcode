class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = {x for x in nums if x }
        return len(res)
        