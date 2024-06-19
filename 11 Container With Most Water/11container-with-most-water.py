class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        a = 0

        while i < j:
            l = j - i
            w = min(height[i], height[j])
            a = max(a, l*w)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return a