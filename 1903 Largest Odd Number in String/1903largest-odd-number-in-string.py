class Solution:
    def largestOddNumber(self, num: str) -> str:
        a = list(num)
        i = len(a) - 1
        while i >= 0:
            if int(a[i]) % 2 != 0:
                break
            i -= 1
        
        if i < 0:
            return ""
        return "".join(a[: i + 1])