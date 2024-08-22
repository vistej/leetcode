class Solution:
    def findComplement(self, num: int) -> int:
        k = str(bin(num))[2:]
        r = ''
        for c in k:
            if c == '0':
                r += '1'
            else:
                r += '0'
        return int(r, 2)