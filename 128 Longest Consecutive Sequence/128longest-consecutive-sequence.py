class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not len(nums):
            return 0
        d = {v: 1 for v in nums}
        max_count = 1

        for n in nums:
            count = 0
            if n - 1 not in d:
                while n in d:
                    count += 1
                    d[n] = 0
                    n += 1
                max_count = max(count, max_count)
        
        return max_count

