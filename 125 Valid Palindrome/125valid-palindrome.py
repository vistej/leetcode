class Solution:
    def isPalindrome(self, s: str) -> bool:

        x = ''

        for i in s:
            if i.isalpha() or i.isdigit():
                x += i

        return x.lower() == ''.join(reversed(x.lower()))