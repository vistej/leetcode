class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ps = [0] * (len(arr) + 1)
        r = arr[0]
        ps[1] = arr[0]
        for i in range(1, len(arr)):
            ps[i + 1] = ps[i] + arr[i]
            k = 1
            while i + 1 - k >= 0:
                r += ps[i + 1] - ps[i - k + 1]
                k += 2
        return r