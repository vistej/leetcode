class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        val = 0
        res = []
        for i in nums:
            val += i
            res.append(val)
            
        return res