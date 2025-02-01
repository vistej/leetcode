class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        even = (nums[0]%2 == 0)
        for i in range(1, len(nums)):
            c = (nums[i]%2 == 0)
            if c == even:
                return False
            even = c
        
        return True