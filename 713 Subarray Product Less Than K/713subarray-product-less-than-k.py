class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        i = 0
        j = 0
        p = 1
        l = len(nums)
        while j < l:
            p *= nums[j]
            while i < l and p >= k:
                p = p // nums[i]
                i += 1
            res += j - i + 1
            j += 1
            
                
        return res