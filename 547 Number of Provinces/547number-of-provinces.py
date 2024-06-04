class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        c = 0
        s = {}
        for i in range(len(isConnected)):
            if not i in s:
                c += 1
                r = [i]
                s[i] = 1
                while r:
                    n = []
                    for p in r:
                        for j,v in enumerate(isConnected[p]):
                            if v and not j in s:
                                n.append(j)
                                s[j] = 1
                    r = n
        return c
