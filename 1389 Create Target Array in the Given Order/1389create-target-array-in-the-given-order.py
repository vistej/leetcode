class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        r = []
        for (n, i) in zip(nums, index):
            r.insert(i, n)
        return r