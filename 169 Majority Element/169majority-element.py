class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        for n in nums:
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n] += 1
            if cnt[n] > len(nums)//2:
                return n