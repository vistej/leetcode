class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        x = 0
        if x == len(nums) - 1:
            if nums[x] == target:
                return [0, 0]
        if nums[0] == target and nums[-1] == target:
            return [0, len(nums) - 1]
        while x < len(nums):
            if nums[x] == target:
                start = x
                end = x
                
                while end <= len(nums) - 1 and nums[end] == target:
                    end += 1

                return [start, end - 1]
            x += 1
        return [-1, -1]


        