class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        mods = [0] * (n + 1)

        def getNext(a, n):
            return chr((ord(a) - ord('a') + n) % 26 + ord('a'))

        for b,e,d in shifts:
            v = 1 if d else -1
            mods[b] += v
            mods[e + 1] -= v
        
        for i in range(1, n):
            mods[i] += mods[i - 1]
        
        res = list(s)
        for i in range(n):
            shifts = ((mods[i] % 26) + 26) % 26
            res[i] = getNext(s[i], shifts)
        
        return ''.join(res)