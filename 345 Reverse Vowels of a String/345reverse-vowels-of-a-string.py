class Solution:
    def reverseVowels(self, s: str) -> str:
        a = []
        c = ''
        r = ''
        v = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for i in range(len(s)):
            if s[i].lower() in v:
                c += '_'
                a.append(s[i])
            else:
                c += s[i]

        for i in range(len(c)):
            if c[i] == '_':
                r += a.pop()
            else:
                r+= c[i]
        return r