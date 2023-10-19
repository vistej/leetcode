class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for i in s:
            if i == '#':
                if len(s1):
                    s1.pop()
            else:
                s1.append(i)
        for i in t:
            if i == '#':
                if len(t1):
                    t1.pop()
            else:
                t1.append(i)
        return s1 == t1