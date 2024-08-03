class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        i = 0
        j = 0

        d = {}
        for k in target:
            d[k] = d.get(k, 0) + 1
        for k in arr:
            if k in d and d[k]:
                d[k] -= 1
            else:
                return False

        return True