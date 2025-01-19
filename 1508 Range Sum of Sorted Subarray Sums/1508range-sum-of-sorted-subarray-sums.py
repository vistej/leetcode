class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10 ** 9 + 7

        a = []
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                a.append(sum(nums[i:j+1]))
        a.sort()
        return sum(a[left-1:right]) % mod
