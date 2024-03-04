class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        left = []
        score = 0
        tokens = sorted(tokens)
        si = 0
        ai = len(tokens) - 1
        while si <= ai:
            if power >= tokens[si]:
                power = power - tokens[si]
                score = score + 1
                si = si + 1
            elif score > 0 and si < ai:
                power = power + tokens[ai]
                score = score - 1
                ai = ai - 1
            else:
                break
        return score


        