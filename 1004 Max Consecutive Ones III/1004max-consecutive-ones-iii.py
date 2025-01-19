class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j = 0, 0

        res = 0

        while j < len(nums):
            if not nums[j]:
                k -= 1
            
            if k < 0:
                while k < 0:
                    if not nums[i]:
                        k += 1
                    i += 1
            res = max(res, j - i + 1)

            j += 1
        
        return res
            