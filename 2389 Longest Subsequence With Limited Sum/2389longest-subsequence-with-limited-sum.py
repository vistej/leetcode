class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        s = 0
        i = 0
        r = {}
        nums.sort()
        qs = sorted(queries)
        for q in qs:
            if s < q:
                while i < len(nums):
                    s += nums[i]
                    if s > q:
                        s -= nums[i]
                        break
                    else:
                        i += 1

            r[q] = i
        return [r[q] for q in queries]