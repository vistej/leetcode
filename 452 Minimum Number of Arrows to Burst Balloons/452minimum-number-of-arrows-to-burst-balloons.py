class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        counts = 0
        mi, ma = None, None
        for point in points:
            print(ma)
            if not ma or ma < point[0]:
                counts += 1
                mi = point[0]
                ma = point[1]
            else:
                mi = max(mi, point[0])
                ma = min(ma, point[1])


        return counts