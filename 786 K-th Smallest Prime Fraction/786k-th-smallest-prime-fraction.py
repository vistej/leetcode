class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        p = []

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                p.append((arr[i], arr[j], arr[i]/arr[j]))
        
        p.sort(key=lambda x: x[2])

        (x, y, z) = p[k - 1]
        return [x, y]