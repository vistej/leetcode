class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = 0
        stra = [a for a in s]
        print(stra)
        for i in stra:
            if i == '0':
                zeros = zeros + 1
        ones = len(stra) - zeros

        res = '1' * (ones - 1) + '0' * (zeros) + '1'
        print(res)
        return res


        