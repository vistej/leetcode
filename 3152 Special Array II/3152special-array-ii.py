class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        arr = [0]
        e = nums[0] % 2 == 0
        for i in range(1, len(nums)):
            ce = (nums[i] % 2 == 0)
            if e == ce:
                arr.append(arr[-1] + 1)
            else:
                arr.append(arr[i - 1])
                e = ce
        res = []
        for i, j in queries:
            if arr[j] - arr[i]:
                res.append(False)
            else:
                res.append(True)
        
        return res
