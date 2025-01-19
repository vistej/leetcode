class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0 for _ in nums2] for _ in nums1]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                val = nums1[i] * nums2[j]
                if i > 0 and j > 0:
                    val = max(val, val + memo[i - 1][j - 1])
                if i > 0:
                    val = max(val, memo[i - 1][j])  
                if j > 0:
                    val = max(val, memo[i][j - 1])
                memo[i][j] = val          

        return memo[-1][-1]