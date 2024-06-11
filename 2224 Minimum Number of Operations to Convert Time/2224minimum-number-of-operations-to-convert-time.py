class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hu, mu = [int(x) for x in current.split(":")]
        ho, mo = [int(x) for x in correct.split(":")]
        c = ho - hu
        r = 0
        if mo < mu:
            c -= 1
            r = 60 - mu + mo
        elif mo > mu:
            r = mo - mu
        while r:
            if r >= 15:
                r -= 15
            elif r >= 5:
                r -= 5
            else:
                r -= 1
            c += 1

        return c