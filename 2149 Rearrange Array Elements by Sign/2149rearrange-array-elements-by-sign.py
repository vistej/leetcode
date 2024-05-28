class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = 0
        n = 0
        ip = True
        r = []
        while len(r) < len(nums):
            if ip:
                while p < len(nums) and nums[p] < 0:
                    p += 1
                if p < len(nums):
                    r.append(nums[p])
                    p += 1
                ip = False
            else:
                while n < len(nums) and nums[n] > 0:
                    n += 1
                if n < len(nums):
                    r.append(nums[n])
                    n += 1
                ip = True
        return r
            
        