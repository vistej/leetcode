class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i, j = 0, len(s) - 1
        a = list(s)
        while i < j:
            if ord(a[i]) < ord(a[j]):
                a[j] = a[i]
            else:
                a[i] = a[j]
            i += 1
            j -= 1
        return ''.join(a)