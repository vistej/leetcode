class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                r.append(nums[i + 1])
        return r