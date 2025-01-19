class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        a = []
        e = []
        for i, c in enumerate(s):
            if c == '(':
                a.append(i)
            elif c == ')':
                if len(a):
                    a.pop()
                else:
                    e.append(i)
                
        ex = a + e
        if not len(ex):
            return s
        r = ''
        for i, c in enumerate(s):
            if not i in ex:
                r += c
        return r