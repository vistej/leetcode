class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        c = 0
        if k < numOnes:
            return k
        k -= numOnes
        c += numOnes
        if k < numZeros:
            return c
        k -= numZeros
        if k < numNegOnes:
            return c - k
        return c - numNegOnes