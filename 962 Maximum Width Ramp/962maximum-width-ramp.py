class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        r = []
        n = len(nums)
        a = 0

        for i in range(n):
            if not r or nums[r[-1]] > nums[i]:
                r.append(i)
            
        for i in range(len(nums) - 1, 0, -1):
            while r and nums[r[-1]] <= nums[i]:
                a = max(a, i - r[-1])
                r.pop()
        
        return a

            
