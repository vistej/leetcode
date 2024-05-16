class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cs = 0
        ps = {0 : 1}
        
        for num in nums:
            cs += num
            diff = cs - k
            res += ps.get(diff, 0)
            ps[cs] = 1 + ps.get(cs, 0)
        
        return res