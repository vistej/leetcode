class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = {}
        for di in dictionary:
            d[di] = 1
        a = []
        for w in sentence.split(' '):
            r = ''
            f =  False
            for c in w:
                r += c
                if r in d:
                    a.append(r)
                    f = True
                    break
            if not f:
                a.append(w)
        return ' '.join(a)
