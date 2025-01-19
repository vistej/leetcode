class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        last_index = None
        res = 0

        while j < len(nums):
            if not nums[j]:
                if last_index != None:
                    i = last_index + 1
                last_index = j
            
            res = max(res, j - i)
            j += 1
        
        return res



