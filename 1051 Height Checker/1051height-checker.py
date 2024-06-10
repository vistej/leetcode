class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        d = sorted(heights)
        return sum([1 for i in range(len(heights)) if heights[i] != d[i]])