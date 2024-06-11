class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i = 0
        j = len(colors) - 1
        r = 0
        while i < j:
            if colors[i] != colors[j]:
                r = j - i
                break
            j -= 1
        i = 0
        j = len(colors) - 1
        while i < j:
            if colors[i] != colors[j]:
                r = max(j - i, r)
                break
            i += 1
        return r