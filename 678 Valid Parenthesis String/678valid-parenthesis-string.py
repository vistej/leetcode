class Solution:
    def checkdat(self, a, e):
        la = len(a)
        le = len(e)
        print(a, e)
        i = 0
        j = 0
        while i < la and j < le:
            while j < le and e[j] < a[i]:
                j += 1
            if j == le:
                return False
            print(i, j)
            j += 1
            i += 1
        
        return i == la

    def checkValidString(self, s: str) -> bool:
        e = []
        a = []
        for i, c in enumerate(s):
            if c == '(':
                a.append(i)
            elif c == '*':
                e.append(i)
            elif c == ')':
                if len(a):
                    a.pop()
                elif len(e):
                    e.pop()
                else:
                    return False
        if not len(a):
            return True
        elif not len(e):
            return False

        return self.checkdat(a, e)

            