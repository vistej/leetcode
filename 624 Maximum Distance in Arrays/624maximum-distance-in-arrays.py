class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ma = []
        mb = []
        for i,a in enumerate(arrays):
            ma.append((a[0], i))
            mb.append((a[-1], i))
        ma.sort()
        mb.sort(reverse=True)
        if ma[0][1] != mb[0][1]:
            return mb[0][0] - ma[0][0]
        else:
            return max((mb[1][0] - ma[0][0]), (mb[0][0] - ma[1][0]))