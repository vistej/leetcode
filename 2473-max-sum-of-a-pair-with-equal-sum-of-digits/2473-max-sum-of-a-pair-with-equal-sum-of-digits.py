class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        def digitSum(n):
            r = 0
            while n:
                r += n % 10
                n = n // 10
            return r

        res = -1

        dsum = defaultdict(list)

        for n in nums:
            nsum = digitSum(n)
            if len(dsum[nsum]):
                res = max(res, n - dsum[nsum][0])
            heapq.heappush(dsum[nsum], -n)
        
        return res