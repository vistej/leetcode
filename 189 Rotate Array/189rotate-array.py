class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        p = len(nums) - k

        r = nums[p:] + nums[:p]
        for i,v in enumerate(r):
            nums[i] = v
        