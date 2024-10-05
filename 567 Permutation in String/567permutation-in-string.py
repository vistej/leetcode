class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sa = {}
        for i in s1:
            sa[i] = sa.get(i, 0) + 1
        sb = {}
        l = len(s1)
        for i in range(len(s2)):
            sb[s2[i]] = sb.get(s2[i], 0) + 1

            if i >= l - 1:
                if sa == sb:
                    return True
                sb[s2[i - l + 1]] -= 1
                if not sb[s2[i - l + 1]]:
                    del sb[s2[i - l + 1]]
        return False