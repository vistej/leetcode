class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        md = 0
        heaters.sort()
        def closest(i, j, h):
            if i == j:
                return abs(h - heaters[i])
             
            m = (i + j) >> 1
            if heaters[m] == h:
                return 0
            if m == i or m == j:
                return min(abs(h - heaters[i]), abs(h - heaters[j]))
            elif h > heaters[m]:
                return closest(m, j, h)
            else:
                return closest(i, m, h)

        
        for h in houses:
            d = closest(0, len(heaters) - 1, h)
            md = max(md, d)
        
        return md
