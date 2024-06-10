class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sa = 0
        sb = sum(nums)
        r = []
        for n in nums:
            r.append(n)
            sa += n
            sb -= n
            if sa > sb:
                break
        return r