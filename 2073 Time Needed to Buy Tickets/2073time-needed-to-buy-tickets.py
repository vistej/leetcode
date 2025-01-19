class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        for i, v in enumerate(tickets):
            if i < k:
                t += min(v, tickets[k])
            elif i > k:
                t += min(v, tickets[k] - 1)
        return t