class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        d = {k: v for v, k in enumerate(a)}
        for i in range(len(arr)):
            arr[i] = d[arr[i]] + 1
        
        return arr