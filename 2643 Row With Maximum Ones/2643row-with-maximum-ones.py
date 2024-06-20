class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        r = [len(mat), 0]
        for i,m in enumerate(mat):
            c = sum(m)
            if c > r[1]:
                r = [i, c]
            elif c == r[1]:
                r[0] = min(r[0], i)

        return r