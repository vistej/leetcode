class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        di = 1
        ax = 1
        p = [0, 0]
        r = 0

        od = {}

        for o in obstacles:
            a = str(o[0]) + '_' + str(o[1])
            od[a] = 1
        print(od)
        
        for c in commands:
            if c == -1:
                di = (ax and di) or (not di and not ax)
                ax = abs(ax - 1)
            elif c == -2:
                di = (ax and not di) or (not ax and di)
                ax = abs(ax - 1)
            else:
                d = copy.deepcopy(p)
                for _ in range(c):
                    d[ax] += 1 if di else -1
                    e = str(d[0]) + '_' + str(d[1])
                    if e in od:
                        break
                    else:
                        p = copy.deepcopy(d)
                b = p[0] ** 2 + p[1] ** 2
                r = max(r, b)
        
        return r