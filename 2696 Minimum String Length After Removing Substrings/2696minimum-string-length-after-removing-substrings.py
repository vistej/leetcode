class Solution:
    def minLength(self, s: str) -> int:
        d = {'AB': 1, 'CD': 1}

        r = []

        for c in list(s):
            if len(r) and r[-1] + c in d:
                r.pop()
            else:
                r.append(c)
        
        return len(r)
        

