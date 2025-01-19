class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        for i,c in enumerate(t):
            if c == '?':
                if i == 0:
                    if t[i + 1] != '?' and t[i + 1] >= '4':
                        t[i] = '1'
                    else:
                        t[i] = '2'
                elif i == 1:
                    if t[i - 1] == '2':
                        t[i] = '3'
                    else:
                        t[i] = '9'
                elif i == 3:
                    t[i] = '5'
                elif i == 4:
                    t[i] = '9'
        return ''.join(t)