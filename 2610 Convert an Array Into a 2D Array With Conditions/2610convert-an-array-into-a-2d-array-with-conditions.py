class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        a = sorted(nums)
        o = [[]]
        c = None
        i = 0
        for v in a:
            if not c or c != v:
                c = v
                i = 0
                o[0].append(v)
            elif c and c == v:
                i += 1
                if i == len(o):
                    o.append([])
                o[i].append(v)
        return o
