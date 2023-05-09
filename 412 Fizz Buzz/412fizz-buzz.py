class Solution:
    def getVal(self, val):
        res = ''
        if val % 3 == 0:
            res += "Fizz"
        if val % 5 == 0:
            res += "Buzz"
        if not res:
            res = str(val)
        return res
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.getVal(x) for x in range(1, n + 1)]