class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, f, r = len(nums), 0, 0
        fp = [0] * n
        for i in range(n):
            if i >= k:
                f ^= fp[i - k]
            if f == nums[i]:
                if i + k > n:
                    return -1
                fp[i] = 1
                f ^= 1
                r += 1
        return r