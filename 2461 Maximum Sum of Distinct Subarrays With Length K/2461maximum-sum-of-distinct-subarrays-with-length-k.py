class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        a = 0
        v = {}
        c = 0
        for i in range(len(nums)):
            c += nums[i]
            v[nums[i]] = v.get(nums[i], 0) + 1
            if i >= k - 1:
                if len(v) == k:
                    a = max(a, c)
                c -= nums[i - k + 1]
                v[nums[i - k + 1]] -= 1
                if not v[nums[i - k + 1]]:
                    del v[nums[i - k + 1]]
        return a