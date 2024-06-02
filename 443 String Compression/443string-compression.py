class Solution:
    def compress(self, chars: List[str]) -> int:
        a = []
        for c in chars:
            if len(a) and a[-1][0] == c:
                a[-1][1] += 1
            else:
                a.append([c, 1])
        print(a)
        i = 0;j = 0
        while j < len(a):
            chars[i] = a[j][0]
            i += 1
            if a[j][1] > 1:
                for p in list(str(a[j][1])):
                    chars[i] = p
                    i += 1
            j += 1
        return i