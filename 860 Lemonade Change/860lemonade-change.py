class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = t = 0
        for b in bills:
            if b == 5:
                f += 1
            elif b == 10:
                t += 1
                if f:
                    f -= 1
                else:
                    return False
            elif b == 20:
                if t:
                    t -= 1
                    if f:
                        f -= 1
                    else:
                        return False
                elif f > 2:
                    f -= 3
                else:
                    return False
        return True