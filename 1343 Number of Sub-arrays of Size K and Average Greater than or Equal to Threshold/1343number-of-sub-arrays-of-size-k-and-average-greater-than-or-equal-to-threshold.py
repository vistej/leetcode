class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        v = k * threshold
        c = 0
        s = sum(arr[:k])
        if s >= v:
            c += 1
        for i in range(k, len(arr)):
            s += arr[i] - arr[i - k]
            if s >= v:
                c += 1
        return c