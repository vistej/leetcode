class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_sentence = ' '.join(word[::-1] for word in words)
        return reversed_sentence