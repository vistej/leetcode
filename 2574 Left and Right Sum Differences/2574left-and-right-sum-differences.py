class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rs = sum(nums)
        ls = 0
        r = []
        for n in nums:
            rs -= n
            r.append(abs(ls - rs))
            ls += n
        
        return r