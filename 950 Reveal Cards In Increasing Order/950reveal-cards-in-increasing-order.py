from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ar = sorted(deck)
        r = []
        l = len(ar)
        q = deque()
        for i in range(l):
            q.append(i)
            r.append(0)
        for i in range(l):
            r[q.popleft()] = ar[i]
            if len(q):
                q.append(q.popleft())
        return r