class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        ml = 0
        cl = 0
        col = {}
        while j < len(nums):
            v = nums[j]
            if not v in col:
                col[v] = 1
            else:
                col[v] += 1
            if col[v] > k:
                cl += 1
                while i <= j and nums[i] != v:
                    col[nums[i]] -= 1
                    i += 1
                    cl -= 1
                col[v] -= 1
                i += 1
                cl -= 1
                j += 1
            else:
                j += 1
                cl += 1
            if cl > ml:
                ml = cl
        return ml