class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        b = 0
        for char in s:
            b += 1 if char == 'L' else -1
            c += 1 if not b else 0
        return c