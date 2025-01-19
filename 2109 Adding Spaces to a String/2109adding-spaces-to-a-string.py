class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        off = 0
        res = ''
        for i in range(len(s)):
            if off < len(spaces) and i == spaces[off]:
                res += ' '
                off += 1
            res += s[i]
        
        return res