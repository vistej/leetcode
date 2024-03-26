class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        l = len(nums)
        i = 0
        prev = None
        while i < l:
            n = nums[i]
            if n > 0 and n < l and n - 1 != i and n != prev:
                temp = nums[i]
                nums[i] = nums[n - 1]
                nums[n - 1] = temp
                prev = n
            else:
                i += 1
        for j in range(1, l + 1):
            if nums[j - 1] != j:
                return j
        return l+1

