class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        
        op = 0
        left = 0

        for i in range(len(s)):
            if locked[i] == '0':
                op += 1
            else:
                if s[i] == '(':
                    left += 1
                else:
                    left -= 1
            if left + op < 0:
                return False
        if left > op:
            return False
        
        op, left = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                op += 1
            else:
                if s[i] == ')':
                    left += 1
                else:
                    left -= 1
            if left + op < 0:
                return False
        if left > op:
            return False
        
        return True