class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        r = 0
        gs = 0
        m = 0
        for i in range(len(grumpy)):
            if not grumpy[i]:
                r += customers[i]
            else:
                gs += customers[i]
            if i >= minutes - 1:
                m = max(gs, m)
                j = i - minutes + 1
                if grumpy[j]:
                    gs -= customers[j]
        
        return r + m