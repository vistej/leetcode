class Solution:
    def minNumberOfHours(self, ien: int, iex: int, energy: List[int], experience: List[int]) -> int:
        t = 0
        for i in range(len(energy)):
            if ien > energy[i]:
                ien -= energy[i]
            else:
                t += energy[i] - ien + 1
                ien = 1
            if iex > experience[i]:
                iex += experience[i]
            else:
                t += experience[i] - iex + 1
                iex = 2 * experience[i] + 1
        return t