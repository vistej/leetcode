class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r = []

        def checkStart(land, i, j):
            return (i - 1 < 0 or land[i - 1][j] == 0) and (j - 1 < 0 or land[i][j - 1] == 0)

        def getEnd(land, i, j):
            while i + 1 < len(land) and land[i + 1][j] == 1:
                i += 1
            while j + 1 < len(land[0]) and land[i][j + 1] == 1:
                j += 1
            return i, j


        i = 0
        j = 0
        while i < len(land) and j < len(land[0]):
            if land[i][j] == 1 and checkStart(land, i, j):
                x, y = getEnd(land, i , j)
                r.append([i, j, x, y])
            j += 1
            if j == len(land[0]):
                j = 0
                i += 1

        return r