class Solution:
    def maxScore(self, s: str) -> int:
        if '1' not in s or '0' not in s:
            return len(s) - 1
        score = s.count('1')
        res = 0

        for c in s:
            if c == '0':
                score += 1
            else:
                score -= 1
            res = max(res, score)
        
        return res
        