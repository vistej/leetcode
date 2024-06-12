class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = {}
        for n in nums:
            if n not in r:
                r[n] = 0
            r[n] += 1
        
        for i in range(len(nums)):
            if 0 in r and r[0]:
                nums[i] = 0
                r[0] -= 1
            elif 1 in r and r[1]:
                nums[i] = 1
                r[1] -= 1
            elif 2 in r:
                nums[i] = 2
                r[2] -= 1