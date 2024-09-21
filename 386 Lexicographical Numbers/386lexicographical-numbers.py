class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        r = []
        c = 1

        for _ in range(n):
            r.append(c)
            if c * 10 <= n:
                c *= 10
            else:
                while c % 10 == 9 or c + 1 > n:
                    c //= 10
                c += 1
        
        return r
                        
        
                
