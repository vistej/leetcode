class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hs = [0, 1, 2, 4, 8]
        ms = [0, 1, 2, 4, 8, 16, 32]
        res = set()

        def dfs(i, j, h, m):
            sh = sum(h)
            sm = sum(m)
            if sh > 11 or sm > 59 or len(h) + len(m) > turnedOn:
                return
            if len(h) + len(m) == turnedOn:
                nm = str(sm) if sm > 9 else '0' + str(sm)
                res.add(str(sh) + ':' + nm)
                return
            if i + 1 < len(hs):
                dfs(i + 1, j, h, m)
                h.append(hs[i + 1])
                dfs(i + 1, j, h, m)
                h.pop()
            if j + 1 < len(ms):
                dfs(i, j + 1, h, m)
                m.append(ms[j + 1])
                dfs(i, j + 1, h, m)
                m.pop()
        
        dfs(0, 0, [], [])

        return list(res)