class Solution:
    def numberOfSteps(self, num: int) -> int:
        st = 0
        while num:
            if not num % 2:
                num = num // 2
            else:
                num -= 1
            st += 1
        return st