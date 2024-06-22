class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        p = [0] * (len(nums) + 1)
        p[0] = 1
        s = 0
        r = 0
        
        for num in nums:
            s += num
            if s >= k:
                r += p[s - k]
            p[s] += 1
        
        return r