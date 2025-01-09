class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def loop(a, i):
            if i == len(nums):
                return
            b = a.copy()
            b.append(nums[i])
            res.append(b)
            loop(a, i + 1)
            loop(b, i + 1)
        
        loop([], 0)
    
        return res