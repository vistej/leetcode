class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        b = sorted(boxTypes, key=lambda x: -x[1])
        c = 0
        i = 0
        while truckSize and i < len(b):
            if truckSize > b[i][0]:
                truckSize -= b[i][0]
                c += b[i][0] * b[i][1]
            else:
                c += truckSize * b[i][1]
                truckSize = 0
            i += 1
        

        return c