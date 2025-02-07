class Solution:
    def rob(self, nums: List[int]) -> int:
        s1 = 0
        s2 = 0

        for i in range(len(nums)):
            temp = s1
            s1 = max(s2 + nums[i], s1)
            s2 = temp
        
        return s1