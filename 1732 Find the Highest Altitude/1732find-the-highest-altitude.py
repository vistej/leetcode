class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        c = 0
        for i in gain:
            c += i
            m = max(c,m)
        return m