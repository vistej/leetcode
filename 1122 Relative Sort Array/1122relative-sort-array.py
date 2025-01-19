class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        r = []
        for i in arr2:
            d[i] = 0
        for i in arr1:
            if i in d:
                d[i] += 1
            else:
                r.append(i)
            
        k = []
        for i in arr2:
            for _ in range(d[i]):
                k.append(i)
        r.sort()
        return k + r