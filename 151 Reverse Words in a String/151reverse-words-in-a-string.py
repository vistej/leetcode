class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.lstrip(" ").rstrip(" ").split()[::-1])