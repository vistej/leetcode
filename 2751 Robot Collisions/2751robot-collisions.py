class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if 'R' not in directions or 'L' not in directions:
            return healths
        d = []
        for i in range(len(positions)):
            d.append([positions[i], healths[i], directions[i], i])
        d.sort()
        r = []
        for i in range(len(d)):
            if d[i][2] == 'R':
                r.append([d[i][3], d[i][1], d[i][2]])
            else:
                if r:
                    j = len(r) - 1
                    k = d[i][1]
                    while j >= 0 and k:
                        if r[j][2] == 'L':
                            r.append([d[i][3], k, d[i][2]])
                            break
                        if r[j][1] > k:
                            r[j][1] -= 1
                            if not r[j][1]:
                                del r[j]
                            break
                        elif r[j][1] == k:
                            del r[j]
                            break
                        else:
                            del r[j]
                            k -= 1
                        j -= 1
                    if j == -1:
                        r.append([d[i][3], k, d[i][2]])

                else:
                    r.append([d[i][3], d[i][1], d[i][2]])
                

        r.sort()
        return [p[1] for p in r]