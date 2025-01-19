class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = k - 1
        a = cardPoints[:k]
        s = sum(a)
        r = s
        p = -1
        l = len(cardPoints)
        while i > -1:
            s -= cardPoints[i]
            s += cardPoints[p + l]
            i -= 1
            p -= 1
            r = max(r, s)
        return r