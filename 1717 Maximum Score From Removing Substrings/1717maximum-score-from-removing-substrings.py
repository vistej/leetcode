class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'ab', 'ba'
        if y > x:
            b, a, y, x = a, b, x, y

        r = 0
        
        for e in [a, b]:
            m = []
            i = 0
            while i < len(s):
                m.append(s[i])
                
                n = len(m)
                prefix = m[n-2] + m[n-1]
                if prefix == e:
                    r += x
                    m.pop()
                    m.pop()
                i += 1
            x = y
            
            s = ''.join(m)
        return r