class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        r = 0
        nums.sort(reverse=True)
        def check(a, b, c):
            if a + b > c and b + c > a and c + a > b:
                return a + b + c
            return 0

        for i in range(len(nums) - 2):
            r = check(nums[i], nums[i + 1], nums[i + 2])
            if r:
                return r
        
        return 0
