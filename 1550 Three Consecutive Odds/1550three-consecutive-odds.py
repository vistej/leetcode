class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            v = arr[i] % 2
            if i > 0 and v:
                v += arr[i - 1]
            if v == 3:
                return True
            arr[i] = v
        return False