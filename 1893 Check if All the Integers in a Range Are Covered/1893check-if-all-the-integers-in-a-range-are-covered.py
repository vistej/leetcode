class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        d = {}
        ranges.sort()
        for a, b in ranges:
            for i in range(a, b + 1):
                d[i] = d.get(i, 0) + 1
        
        for i in range(left, right + 1):
            if i not in d:
                return False
        
        return True