class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = [1] * len(nums)
        x = 1
        for i in range(len(nums)):
            prod_arr[i] *= x
            x *= nums[i]
        x = 1
        for i in range(len(nums) - 1, -1, -1):
            prod_arr[i] *= x
            x *= nums[i]
        
        return prod_arr

