class Solution:
    def minimumSteps(self, s: str) -> int:
        onec = s.count('0')
        s = list(s)
        i,j = 0,1
        r = 0
        while i < onec and j < len(s):
            if s[i] == '1':
                while s[j] == '1':
                    j += 1
                r += j - i
                s[i], s[j] = s[j], s[i]
            i += 1
            j += 1
            
        return r