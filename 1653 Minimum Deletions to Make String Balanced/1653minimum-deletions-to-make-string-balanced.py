

class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        d = 0
        
        for char in s:
            if char == 'b':
                b += 1
            else:
                d = min(d + 1, b)
                
        return d