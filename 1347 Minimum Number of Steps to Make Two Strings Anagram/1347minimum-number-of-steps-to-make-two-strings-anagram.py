class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sa = {}
        ta = {}
        for i in s:
            sa[i] = (sa[i] + 1 if i in sa else 1)
        for i in t:
            ta[i] = (ta[i] + 1 if i in ta else 1)

        c = 0
        print(sa, ta)
        for k in sa.keys():
            if k in ta:
                if sa[k] > ta[k]:
                    c += sa[k] - ta[k]
            else:
                c += sa[k]
        return c