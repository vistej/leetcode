class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        s = nums[0]
        e = nums[0]
        r = []
        i = 1
        def apply(s, e, r):
            if s == e:
                r.append(str(s))
            else:
                r.append(str(s) + '->' + str(e))

        while i < len(nums):
            if nums[i] != e + 1:
                apply(s,e,r)
                s = nums[i]
            e = nums[i]
            i += 1
        apply(s,e,r)
        return r

