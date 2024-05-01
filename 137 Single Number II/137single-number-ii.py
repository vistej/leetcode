class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        i = {}
        for n in nums:
            s += n
            if n not in i:
                s -= n * 3
                i[n] = 1
        return (-1 * s) // 2
