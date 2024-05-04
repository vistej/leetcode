class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1

        score = [0]*(n+1)

        for a,b in trust:
            score[a] -= 1
            score[b] += 1

        for i, s in enumerate(score[1:], 1):
            if s == n-1:
                return i

        return -1