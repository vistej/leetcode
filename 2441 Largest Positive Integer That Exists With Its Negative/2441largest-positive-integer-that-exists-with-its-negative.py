class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ar = sorted(set(nums))

        i = 0
        j = len(ar) - 1

        while i < j:
            if abs(ar[i]) == ar[j]:
                return ar[j]
            if abs(ar[i]) < ar[j]:
                j -= 1
            else:
                i += 1
        return -1