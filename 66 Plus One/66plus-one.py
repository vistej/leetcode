class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = [str(x) for x in digits]
        v = int(''.join(d)) + 1
        d = list(str(v))
        return [int(x) for x in d]
        