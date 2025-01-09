class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def loop(a, i, s):
            if s == 0:
                res.append(a[:])
                return
            if s < 0:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                a.append(candidates[j])
                loop(a, j + 1, s - candidates[j])
                a.pop()
            
        
        loop([], 0, target)
        return res