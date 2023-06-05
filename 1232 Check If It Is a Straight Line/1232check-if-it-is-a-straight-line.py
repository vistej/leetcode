class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        same = True
        ind = 2
        def eq(c3):
            c1 = coordinates[0]
            c2 = coordinates[1]
            return ((c3[0] - c1[0]) * (c2[1] - c1[1])) == ((c2[0] - c1[0]) * (c3[1] - c1[1]))
        samex = all([bool(x[0] == coordinates[0][0]) for x in coordinates])
        samey = all([bool(x[1] == coordinates[1][1]) for x in coordinates])

        if samex or samey:
            return True

        while same and ind < len(coordinates):
            
            same = eq(coordinates[ind])
            ind += 1
        return same
