class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = 0
        com = 0
        for i in range(1, n + 1):
            tot = tot + i
        for i in range(n, 0, -1):
            com = com + i
            if tot == com:
                return i
            tot = tot - i
        return -1
        