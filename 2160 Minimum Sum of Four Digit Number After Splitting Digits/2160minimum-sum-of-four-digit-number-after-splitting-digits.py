class Solution:
    def minimumSum(self, num: int) -> int:
        a = list(str(num))
        a.sort()
        return int(a[0] + a[2]) + int(a[1] + a[3])