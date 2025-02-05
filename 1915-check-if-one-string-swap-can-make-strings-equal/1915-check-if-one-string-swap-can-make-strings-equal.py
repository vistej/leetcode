class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        limit = 2
        n = len(s1)
        check = None
        
        # since both strings are of same length
        for i in range(n):
            if s1[i] != s2[i]:
                if not check:
                    check = [s1[i], s2[i]]
                else:
                    if s2[i] != check[0] or s1[i] != check[1]:
                        return False
                limit -= 1
            if limit < 0:
                return False

        return (limit in (0, 2))