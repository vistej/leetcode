class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        def loo(s, i):
            r = []
            while i < len(s):
                if s[i] == '(':
                    k, i = loo(s, i + 1)
                    r += reversed(k)
                elif s[i] == ')':
                    i += 1
                    break
                else:
                    r.append(s[i])
                    i += 1
            return r, i
        r, _ = loo(s, 0)
        return ''.join(r)
