class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        r = []
        for n in nums1:
            d[n] = d.get(n, 0) + 1
        for n in nums2:
            if n in d and d[n] > 0:
                r.append(n)
                d[n] -= 1
        return r
        