class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        inx = 2
        res = [1, 1]
        if rowIndex == 1:
            return res
        while inx <= rowIndex:
            c = [1]
            i = 0
            while i < len(res) - 1:
                c.append(res[i] + res[i + 1])
                i += 1
            c.append(1)
            inx += 1
            res = c
        return res