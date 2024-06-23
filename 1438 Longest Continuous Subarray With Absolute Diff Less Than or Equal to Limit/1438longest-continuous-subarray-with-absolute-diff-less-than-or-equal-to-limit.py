import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        a = []
        m = 0
        for n in nums:
            if n not in a:
                i = len(a) - 1
                while i >= 0:
                    if abs(a[i] - n) > limit:
                        break
                    i -= 1
                a = a[i+1:]
            a.append(n)
            m = max(len(a), m)
        return m