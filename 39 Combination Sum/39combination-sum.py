class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def loop(a, i, s):
            if i == len(candidates) or s > target:
                return

            b = a.copy()
            b.append(candidates[i])
            k = s + candidates[i]
            if k == target:
                res.append(b)
            loop(b, i, k)
            loop(a, i + 1, s)
        
        loop([], 0, 0)

        return res
            