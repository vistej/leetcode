class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            v1 = nums1[i]
            v2 = nums2[j]
            if v1 == v2:
                return v1
            elif v1 > v2:
                j = j + 1
            else:
                i = i + 1
        return -1