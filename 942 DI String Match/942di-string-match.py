class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i = 0
        d = len(s)
        r = []
        for c in s:
            if c == 'I':
                r.append(i)
                i += 1
            else:
                r.append(d)
                d -= 1
        if s[-1] == 'I':
            r.append(i)
        else:
            r.append(d)
        return r