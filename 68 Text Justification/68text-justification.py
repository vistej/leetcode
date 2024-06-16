class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cl = 0
        cs = []
        res = []
        for word in words:
            if cl + len(cs) + len(word) > maxWidth:
                for i in range(maxWidth - cl):
                    cs[i % (len(cs) - 1 or 1)] += ' '
                res.append(''.join(cs))
                cs = [word]
                cl = len(word)
            else:
                cl += len(word)
                cs.append(word)
        if cl:
            s = ' '.join(cs).ljust(maxWidth)
            res.append(s)

        return res
