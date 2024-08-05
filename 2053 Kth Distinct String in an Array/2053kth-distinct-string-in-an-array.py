class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = {}
        for v in arr:
            a[v] = a.get(v, 0) + 1
        i = 0
        c = 0
        while i < len(arr):
            if a[arr[i]] == 1:
                c += 1
                if c == k:
                    return arr[i]
            i += 1
        return ""