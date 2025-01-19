class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            p, b = position[0], 1
            for i in range(1, len(position)):
                if position[i] - p >= mid:
                    p = position[i]
                    b += 1
            if b >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
