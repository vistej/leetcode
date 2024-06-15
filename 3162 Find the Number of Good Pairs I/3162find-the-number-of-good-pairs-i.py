class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k > 1:
            for i in range(len(nums2)):
                nums2[i] *= k
        c = 0
        for n in nums1:
            for m in nums2:
                if not n%m:
                    c += 1
        return c
        