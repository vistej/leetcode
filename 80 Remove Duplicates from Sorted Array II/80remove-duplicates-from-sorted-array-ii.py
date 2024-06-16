class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        i = 0
        while True:
            if i < len(nums):
                if nums[i] != l:
                    r = 1
                    l = nums[i]
                    i += 1
                else:
                    if r == 2:
                        del nums[i]
                    else:
                        r += 1
                        i += 1
            else:
                break
        return len(nums)