class Solution:
    def fillCups(self, amount: List[int]) -> int:
        r = 0
        amount.sort()
        
        while amount[1] and amount[2]:
            r += 1
            amount[1] -= 1
            amount[2] -= 1
            amount.sort()
        
        r += amount[2]
            
        return r