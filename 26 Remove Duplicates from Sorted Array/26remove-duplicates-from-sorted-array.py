class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = list(set(nums))
        a.sort()
        for i in range(len(nums)):
            nums[i] = a[i] if i < len(a) else '_'
        
        return len(a)