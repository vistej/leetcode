class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cons = 1
        i = 1
        res = []
        while i <= len(nums):
            if i >= k:
                if cons >= k:
                    res.append(nums[i - 1])
                else:
                    res.append(-1)
            if i < len(nums) and nums[i] == nums[i - 1] + 1:
                cons += 1
            else:
                cons = 1
            i += 1
        
        return res
            


                                
