class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums) - 1

        def loo(i, j):
            m = (i + j) // 2
            if nums[m] == target:
                return m
        
            elif nums[m] > target:
                if m - 1 < 0 or nums[m - 1] < target:
                    return m
                return loo(i, m - 1)
            else:
                if m + 1 >= len(nums) or nums[m + 1] >= target:
                    return m + 1
                return loo(m + 1, j)
        
        return loo(i, j)